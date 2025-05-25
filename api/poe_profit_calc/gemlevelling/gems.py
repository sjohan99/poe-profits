from collections import defaultdict
from dataclasses import dataclass, field
from poe_profit_calc.gemlevelling.gemxp import GEM_MAX_LEVEL_EXPERIENCE
from enum import Enum
import logging
from typing import Tuple
import msgspec

IGNORE_GEMS = {
    "Portal",
    "Detonate Mines",
    "Vaal Impurity of Fire",
    "Vaal Impurity of Ice",
    "Vaal Impurity of Lightning",
    "Vaal Breach",
    "Vaal Domination",
    "Blood and Sand",
    "Brand Recall",
    "Convocation",
    "Awakened Empower Support",
    "Awakened Enhance Support",
    "Awakened Enlighten Support",
}

"""
Non-transfigured gems which include "of" in their name.
"""
NORMAL_OF_GEMS = {
    "Vaal Impurity of Fire",
    "Vaal Impurity of Ice",
    "Vaal Impurity of Lightning",
    "Vaal Rain of Arrows" "Wave of Conviction",
    "Sigil of Power",
    "Purity of Fire",
    "Purity of Ice",
    "Purity of Lightning",
    "Purity of Elements",
    "Orb of Storms",
    "Rain of Arrows",
    "Herald of Purity",
    "Herald of Agony",
    "Herald of Ash",
    "Herald of Ice",
    "Herald of Thunder",
    "Eye of Winter",
    "Fist of War Support",
    "Increased Area of Effect Support",
}

EXCEPTIONAL_GEMS = {
    "Empower Support",
    "Enhance Support",
    "Enlighten Support",
}

VAAL_LEVEL_UP_CHANCE = 0.125
VAAL_23_QUALITY_CHANCE = 0.1
VAAL_CHANGE_CHANCE = 0.25
VAAL_OTHER = VAAL_LEVEL_UP_CHANCE + VAAL_23_QUALITY_CHANCE + VAAL_CHANGE_CHANCE


class GemType(Enum):
    NORMAL = "normal"
    VAAL = "vaal"
    AWAKENED = "awakened"
    EXCEPTIONAL = "exceptional"
    TRANSFIGURED = "transfigured"


NORMAL_GEM_XP = 340_000_000


class Gem(msgspec.Struct, frozen=True, cache_hash=True):
    name: str
    chaosValue: float
    gemLevel: int = 1
    gemQuality: int = 0
    corrupted: bool = False
    icon: str | None = None
    max_experience: int = msgspec.field(default=0)
    max_level: int = msgspec.field(default=0)
    value_per_xp: float = msgspec.field(default=0)
    type: GemType = msgspec.field(default=GemType.NORMAL)

    def __post_init__(self):
        max_level, max_experience = get_max_level_xp(self.name)
        msgspec.structs.force_setattr(self, "max_experience", max_experience)
        msgspec.structs.force_setattr(self, "max_level", max_level)
        if self.max_experience != 0:  # Avoid division by zero, gems without max xp e.g. Portal
            msgspec.structs.force_setattr(
                self, "value_per_xp", self.chaosValue / self.max_experience
            )
        gem_type = GemType.NORMAL
        if self.name in EXCEPTIONAL_GEMS:
            gem_type = GemType.EXCEPTIONAL
        elif self.name.startswith("Vaal"):
            gem_type = GemType.VAAL
        elif self.name.startswith("Awakened"):
            gem_type = GemType.AWAKENED
        elif "of" in self.name and self.name not in NORMAL_OF_GEMS:
            gem_type = GemType.TRANSFIGURED
        msgspec.structs.force_setattr(self, "type", gem_type)

    def __hash__(self) -> int:
        return hash(f"{self.name}{self.corrupted}{self.gemLevel}{self.gemQuality}")


class GemData(msgspec.Struct):
    lines: set[Gem]


def get_max_level_xp(gem: str) -> Tuple[int, int]:
    xp = GEM_MAX_LEVEL_EXPERIENCE.get(
        gem.replace("'", ""), 2_000_000_000
    )  # 2b safe default (approx woke gem xp)
    if xp == 2_000_000_000 and gem not in IGNORE_GEMS:
        logging.info(f"Could not find max xp for {gem}, setting xp to 2 billion")
    if gem in EXCEPTIONAL_GEMS:
        return 3, xp
    if gem.startswith("Awakened"):
        return 5, xp
    return 20, xp


def parse(json_b: bytes) -> set[Gem]:
    try:
        parsed = msgspec.json.decode(json_b, type=GemData)
        return parsed.lines
    except msgspec.DecodeError:
        return set()


def omit_double_corrupted_and_ignored_gems(gems: set[Gem]) -> set[Gem]:
    should_omit = lambda gem: any(
        [
            gem.name in IGNORE_GEMS,
            gem.gemLevel == gem.max_level + 1 and gem.gemQuality > 20,
            gem.name.startswith("Vaal") and gem.gemLevel == gem.max_level + 1,
            gem.name.startswith("Vaal") and gem.gemQuality > 20,
        ]
    )
    return {gem for gem in gems if not should_omit(gem)}


def group_gems(gems: set[Gem]) -> dict[str, set[Gem]]:
    d = defaultdict(set)
    for gem in gems:
        name = gem.name[5:] if gem.type == GemType.VAAL else gem.name
        d[name].add(gem)
    return d


@dataclass
class GemProfit:
    gem: Gem
    level_profit: float
    level_c_profit: float | None
    level_q_c_profit: float | None
    vaal_orb_profit: float | None
    vaal_orb_20q_profit: float | None
    vaal_level_profit: float | None = None
    xp_adjusted_level_profit: float = field(init=False)
    xp_adjusted_c_profit: float | None = field(init=False)
    xp_adjusted_q_c_profit: float | None = field(init=False)

    def __post_init__(self):
        ratio = NORMAL_GEM_XP / self.gem.max_experience
        self.xp_adjusted_level_profit = self.level_profit * ratio
        self.xp_adjusted_c_profit = self.level_c_profit * ratio if self.level_c_profit else None
        self.xp_adjusted_q_c_profit = (
            self.level_q_c_profit * ratio if self.level_q_c_profit else None
        )


def create_profitability_report(gems: set[Gem]) -> list[GemProfit]:
    gems = omit_double_corrupted_and_ignored_gems(gems)
    gem_groups = group_gems(gems)
    report_data = []
    for k, v in gem_groups.items():
        if profitability := calculate_profitability(k, v):
            report_data.append(profitability)
        else:
            logging.debug(f"Could not calculate profitability for {k}")
    if len(report_data) < len(gem_groups) / 2:
        logging.warning(
            f"Could only calculate profitability for {len(report_data)} gems out of {len(gem_groups)}"
        )
    return report_data


def calculate_profitability(gem_name: str, gem_group: set[Gem]) -> GemProfit | None:
    max_level, _ = get_max_level_xp(gem_name)
    max_plus = max_level + 1
    g_1_0q_v = None
    g_max_0q_v = None
    g_max_20q_v = None
    g_1_0q = None
    g_1_20q = None
    g_max_0q = None
    g_max_0q_c = None
    g_max_20q = None
    g_max_20q_c = None
    g_max_plus_0q_c = None
    g_max_plus_20q_c = None
    g_max_23q_c = None
    for gem in gem_group:
        if gem.gemLevel == 1 and gem.gemQuality == 0 and gem.corrupted and gem.type == GemType.VAAL:
            g_1_0q_v = gem
        elif (
            gem.gemLevel == max_level
            and gem.gemQuality == 0
            and gem.corrupted
            and gem.type == GemType.VAAL
        ):
            g_max_0q_v = gem
        elif (
            gem.gemLevel == max_level
            and gem.gemQuality == 20
            and gem.corrupted
            and gem.type == GemType.VAAL
        ):
            g_max_20q_v = gem
        elif gem.gemLevel == 1 and gem.gemQuality == 0 and not gem.corrupted:
            g_1_0q = gem
        elif gem.gemLevel == 1 and gem.gemQuality == 20 and not gem.corrupted:
            g_1_20q = gem
        elif gem.gemLevel == max_level and gem.gemQuality == 0 and not gem.corrupted:
            g_max_0q = gem
        elif gem.gemLevel == max_level and gem.gemQuality == 0 and gem.corrupted:
            g_max_0q_c = gem
        elif gem.gemLevel == max_level and gem.gemQuality == 20 and not gem.corrupted:
            g_max_20q = gem
        elif gem.gemLevel == max_level and gem.gemQuality == 20 and gem.corrupted:
            g_max_20q_c = gem
        elif gem.gemLevel == max_plus and gem.gemQuality == 0 and gem.corrupted:
            g_max_plus_0q_c = gem
        elif gem.gemLevel == max_plus and gem.gemQuality == 20 and gem.corrupted:
            g_max_plus_20q_c = gem
        elif gem.gemLevel == max_level and gem.gemQuality == 23 and gem.corrupted:
            g_max_23q_c = gem

    vaal_orb_0q_profit = calculate_vaal_orb_profit_0q(
        g_max_0q, g_max_0q_c, g_max_plus_0q_c, g_max_0q_v
    )
    vaal_orb_20q_profit = calculate_vaal_orb_profit_20q(
        g_max_20q, g_max_20q_c, g_max_plus_20q_c, g_max_23q_c, g_max_20q_v
    )
    if not (g_max_0q and g_1_0q):
        if (g_max_20q and g_1_20q) and max_level < 20:
            g_1_0q = g_1_20q
            g_max_0q = g_max_20q
        else:
            return None

    level_profit = g_max_0q.chaosValue - g_1_0q.chaosValue
    level_corrupt_profit = (
        level_profit + vaal_orb_0q_profit if vaal_orb_0q_profit is not None else None
    )
    level_quality_corrupt_profit = (
        level_profit + vaal_orb_20q_profit if vaal_orb_20q_profit is not None else None
    )
    if g_max_0q_v and g_1_0q_v:
        vaal_level_profit = g_max_0q_v.chaosValue - g_1_0q_v.chaosValue
    else:
        vaal_level_profit = None

    return GemProfit(
        g_1_0q,
        level_profit,
        level_corrupt_profit,
        level_quality_corrupt_profit,
        vaal_orb_0q_profit,
        vaal_orb_20q_profit,
        vaal_level_profit,
    )


def calculate_vaal_orb_profit_0q(g_max_0q, g_max_0q_c, g_max_plus_0q_c, g_max_0q_v=None):
    if not all([g_max_0q, g_max_0q_c, g_max_plus_0q_c]):
        return None
    if g_max_0q_v:
        expected_value_after_vaal = (
            VAAL_CHANGE_CHANCE * g_max_0q_v.chaosValue
            + VAAL_LEVEL_UP_CHANCE * g_max_plus_0q_c.chaosValue
            + (1 - VAAL_LEVEL_UP_CHANCE - VAAL_CHANGE_CHANCE) * g_max_0q_c.chaosValue
        )
    else:
        expected_value_after_vaal = (
            VAAL_LEVEL_UP_CHANCE * g_max_plus_0q_c.chaosValue
            + (1 - VAAL_LEVEL_UP_CHANCE) * g_max_0q_c.chaosValue
        )
    return expected_value_after_vaal - g_max_0q.chaosValue


def calculate_vaal_orb_profit_20q(
    g_max_20q, g_max_20q_c, g_max_plus_20q_c, g_max_23q_c, g_max_20q_v=None
):
    if not all([g_max_20q, g_max_20q_c, g_max_plus_20q_c, g_max_23q_c]):
        return None
    if g_max_20q_v:
        expected_value_after_vaal = (
            VAAL_CHANGE_CHANCE * g_max_20q_v.chaosValue
            + VAAL_LEVEL_UP_CHANCE * g_max_plus_20q_c.chaosValue
            + VAAL_23_QUALITY_CHANCE * g_max_23q_c.chaosValue
            + (1 - VAAL_LEVEL_UP_CHANCE - VAAL_CHANGE_CHANCE - VAAL_23_QUALITY_CHANCE)
            * g_max_20q_c.chaosValue
        )
    else:
        expected_value_after_vaal = (
            VAAL_LEVEL_UP_CHANCE * g_max_plus_20q_c.chaosValue
            + VAAL_23_QUALITY_CHANCE * g_max_23q_c.chaosValue
            + (1 - VAAL_LEVEL_UP_CHANCE - VAAL_CHANGE_CHANCE) * g_max_20q_c.chaosValue
        )
    return expected_value_after_vaal - g_max_20q.chaosValue
