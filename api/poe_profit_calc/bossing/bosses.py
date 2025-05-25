from dataclasses import dataclass
from poe_profit_calc.fetch import PoeWatchEndpoint, PoeNinjaEndpoint, PoeEndpoint
from poe_profit_calc.bossing.bossitems import BossItem, Matcher


@dataclass
class Boss:
    name: str
    short_name: str
    entrance_items: dict[BossItem, int]
    drops: set[BossItem]

    def items(self):
        return self.drops.union(set(self.entrance_items))

    def get_endpoints(self) -> set[PoeEndpoint]:
        return {item.matcher.source for item in self.items()}


TheSearingExarch = Boss(
    name="The Searing Exarch",
    short_name="Exarch",
    entrance_items={
        BossItem(
            "Incandescent Invitation",
            "IncandescentInvitation",
            0,
            Matcher(PoeNinjaEndpoint.INVITATION, "Incandescent Invitation"),
        ): 1
    },
    drops={
        BossItem(
            "Dawnbreaker",
            "Dawnbreaker",
            0.33,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Dawnbreaker"),
        ),
        BossItem(
            "Dawnstrider",
            "Dawnstrider",
            0.65,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Dawnstrider"),
        ),
        BossItem(
            "Dissolution of the Flesh",
            "DissolutionoftheFlesh",
            0.02,
            Matcher(PoeNinjaEndpoint.UNIQUE_JEWEL, "Dissolution of the Flesh"),
        ),
        BossItem(
            "Forbidden Flame",
            "ForbiddenFlame",
            0.05,
            Matcher(PoeWatchEndpoint.UNIQUE_JEWEL, "Unidentified Forbidden Flame", ilvl=86),
        ),
        BossItem(
            "Exceptional Eldritch Ember",
            "ExceptionalEldritchEmber",
            0.15,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Exceptional Eldritch Ember"),
        ),
        BossItem(
            "Eldritch Orb of Annulment",
            "EldritchOrbofAnnulment",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Eldritch Orb of Annulment"),
        ),
        BossItem(
            "Eldritch Chaos Orb",
            "EldritchChaosOrb",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Eldritch Chaos Orb"),
        ),
        BossItem(
            "Eldritch Exalted Orb",
            "EldritchExaltedOrb",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Eldritch Exalted Orb"),
        ),
    },
)


TheSearingExarchUber = Boss(
    name="The Searing Exarch (Uber)",
    short_name="Exarch (Uber)",
    entrance_items={
        BossItem(
            "Blazing Fragment",
            "BlazingFragment",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Blazing Fragment"),
        ): 5
    },
    drops={
        BossItem(
            "The Annihilating Light",
            "TheAnnihilatingLight",
            0.475,
            Matcher(PoeNinjaEndpoint.UNIQUE_WEAPON, "The Annihilating Light"),
        ),
        BossItem(
            "Annihilation's Approach",
            "AnnihilationsApproach",
            0.25,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Annihilation's Approach"),
        ),
        BossItem(
            "The Celestial Brace",
            "TheCelestialBrace",
            0.25,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "The Celestial Brace"),
        ),
        BossItem(
            "Crystallised Omniscience",
            "CrystallisedOmniscience",
            0.025,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Crystallised Omniscience"),
        ),
        BossItem(
            "Archive Reliquary Key",
            "ArchiveReliquaryKey",
            0.015,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Archive Reliquary Key"),
        ),
        BossItem(
            "Curio of Absorption",
            "CurioofAbsorption",
            0.05,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Curio of Absorption"),
        ),
        BossItem(
            "Forbidden Flame",
            "ForbiddenFlameUber",
            0.05,
            Matcher(PoeWatchEndpoint.UNIQUE_JEWEL, "Unidentified Forbidden Flame", ilvl=87),
        ),
        BossItem(
            "Exceptional Eldritch Ember",
            "ExceptionalEldritchEmber",
            0.15,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Exceptional Eldritch Ember"),
        ),
        BossItem(
            "Eldritch Orb of Annulment",
            "EldritchOrbofAnnulment",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Eldritch Orb of Annulment"),
        ),
        BossItem(
            "Eldritch Chaos Orb",
            "EldritchChaosOrb",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Eldritch Chaos Orb"),
        ),
        BossItem(
            "Eldritch Exalted Orb",
            "EldritchExaltedOrb",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Eldritch Exalted Orb"),
        ),
    },
)


TheEaterOfWorlds = Boss(
    name="The Eater of Worlds",
    short_name="Eater",
    entrance_items={
        BossItem(
            "Screaming Invitation",
            "ScreamingInvitation",
            0,
            Matcher(PoeNinjaEndpoint.INVITATION, "Screaming Invitation"),
        ): 1
    },
    drops={
        BossItem(
            "The Gluttonous Tide",
            "TheGluttonousTide",
            0.5,
            Matcher(PoeNinjaEndpoint.UNIQUE_WEAPON, "The Gluttonous Tide"),
        ),
        BossItem(
            "Inextricable Fate",
            "InextricableFate",
            0.5,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Inextricable Fate"),
        ),
        BossItem(
            "Melding of the Flesh",
            "MeldingoftheFlesh",
            0.02,
            Matcher(PoeNinjaEndpoint.UNIQUE_JEWEL, "Melding of the Flesh"),
        ),
        BossItem(
            "Forbidden Flesh",
            "ForbiddenFlesh",
            0.05,
            Matcher(PoeWatchEndpoint.UNIQUE_JEWEL, "Unidentified Forbidden Flesh", ilvl=86),
        ),
        BossItem(
            "Exceptional Eldritch Ichor",
            "ExceptionalEldritchIchor",
            0.15,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Exceptional Eldritch Ichor"),
        ),
        BossItem(
            "Eldritch Orb of Annulment",
            "EldritchOrbofAnnulment",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Eldritch Orb of Annulment"),
        ),
        BossItem(
            "Eldritch Chaos Orb",
            "EldritchChaosOrb",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Eldritch Chaos Orb"),
        ),
        BossItem(
            "Eldritch Exalted Orb",
            "EldritchExaltedOrb",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Eldritch Exalted Orb"),
        ),
    },
)


TheEaterOfWorldsUber = Boss(
    name="The Eater of Worlds (Uber)",
    short_name="Eater (Uber)",
    entrance_items={
        BossItem(
            "Devouring Fragment",
            "DevouringFragment",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Devouring Fragment"),
        ): 5
    },
    drops={
        BossItem(
            "Nimis",
            "Nimis",
            0.01,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Nimis"),
        ),
        BossItem(
            "Ravenous Passion",
            "RavenousPassion",
            0.66,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Ravenous Passion"),
        ),
        BossItem(
            "Ashes of the Stars",
            "AshesoftheStars",
            0.33,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Ashes of the Stars"),
        ),
        BossItem(
            "Visceral Reliquary Key",
            "VisceralReliquaryKey",
            0.01,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Visceral Reliquary Key"),
        ),
        BossItem(
            "Curio of Consumption",
            "CurioofConsumption",
            0.05,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Curio of Consumption"),
        ),
        BossItem(
            "Forbidden Flesh",
            "ForbiddenFleshUber",
            0.05,
            Matcher(PoeWatchEndpoint.UNIQUE_JEWEL, "Unidentified Forbidden Flesh", ilvl=87),
        ),
        BossItem(
            "Exceptional Eldritch Ichor",
            "ExceptionalEldritchIchor",
            0.15,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Exceptional Eldritch Ichor"),
        ),
        BossItem(
            "Eldritch Orb of Annulment",
            "EldritchOrbofAnnulment",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Eldritch Orb of Annulment"),
        ),
        BossItem(
            "Eldritch Chaos Orb",
            "EldritchChaosOrb",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Eldritch Chaos Orb"),
        ),
        BossItem(
            "Eldritch Exalted Orb",
            "EldritchExaltedOrb",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Eldritch Exalted Orb"),
        ),
    },
)


TheShaper = Boss(
    name="The Shaper",
    short_name="Shaper",
    entrance_items={
        BossItem(
            "Fragment of the Hydra",
            "FragmentoftheHydra",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of the Hydra"),
        ): 1,
        BossItem(
            "Fragment of the Minotaur",
            "FragmentoftheMinotaur",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of the Minotaur"),
        ): 1,
        BossItem(
            "Fragment of the Phoenix",
            "FragmentofthePhoenix",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of the Phoenix"),
        ): 1,
        BossItem(
            "Fragment of the Chimera",
            "FragmentoftheChimera",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of the Chimera"),
        ): 1,
    },
    drops={
        BossItem(
            "Shaper's Touch",
            "ShapersTouch",
            0.56,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Shaper's Touch"),
        ),
        BossItem(
            "Voidwalker",
            "Voidwalker",
            0.33,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Voidwalker"),
        ),
        BossItem(
            "Solstice Vigil",
            "SolsticeVigil",
            0.1,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Solstice Vigil"),
        ),
        BossItem(
            "Dying Sun",
            "DyingSun",
            0.01,
            Matcher(PoeNinjaEndpoint.UNIQUE_FLASK, "Dying Sun"),
        ),
        BossItem(
            "Fragment of Knowledge",
            "FragmentofKnowledge",
            0.5,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Knowledge"),
        ),
        BossItem(
            "Fragment of Shape",
            "FragmentofShape",
            0.5,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Shape"),
        ),
        BossItem(
            "Orb of Dominance",
            "OrbofDominanceShaper",
            0.01,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Orb of Dominance"),
        ),
    },
)


TheShaperUber = Boss(
    name="The Shaper (Uber)",
    short_name="Shaper (Uber)",
    entrance_items={
        BossItem(
            "Cosmic Fragment",
            "CosmicFragment",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Cosmic Fragment"),
        ): 5,
    },
    drops={
        BossItem(
            "Echoes of Creation",
            "EchoesofCreation",
            0.46,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Echoes of Creation"),
        ),
        BossItem(
            "The Tides of Time",
            "TheTidesofTime",
            0.33,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "The Tides of Time"),
        ),
        BossItem(
            "Entropic Devastation",
            "EntropicDevastation",
            0.2,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Entropic Devastation"),
        ),
        BossItem(
            "Starforge",
            "Starforge",
            0.005,
            Matcher(PoeNinjaEndpoint.UNIQUE_WEAPON, "Starforge"),
        ),
        BossItem(
            "Sublime Vision",
            "SublimeVision",
            0.025,
            Matcher(PoeWatchEndpoint.UNIQUE_JEWEL, "Unidentified Sublime Vision", ilvl=87),
        ),
        BossItem(
            "Cosmic Reliquary Key",
            "CosmicReliquaryKey",
            0.01,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Cosmic Reliquary Key"),
        ),
        BossItem(
            "Fragment of Knowledge",
            "FragmentofKnowledge",
            0.5,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Knowledge"),
        ),
        BossItem(
            "Fragment of Shape",
            "FragmentofShape",
            0.5,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Shape"),
        ),
        BossItem(
            "Orb of Dominance",
            "OrbofDominanceShaper",
            0.01,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Orb of Dominance"),
        ),
    },
)


TheElder = Boss(
    name="The Elder",
    short_name="Elder",
    entrance_items={
        BossItem(
            "Fragment of Purification",
            "FragmentofPurification",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Purification"),
        ): 1,
        BossItem(
            "Fragment of Constriction",
            "FragmentofConstriction",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Constriction"),
        ): 1,
        BossItem(
            "Fragment of Enslavement",
            "FragmentofEnslavement",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Enslavement"),
        ): 1,
        BossItem(
            "Fragment of Eradication",
            "FragmentofEradication",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Eradication"),
        ): 1,
    },
    drops={
        BossItem(
            "Fragment of Terror",
            "FragmentofTerror",
            0.5,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Terror"),
        ),
        BossItem(
            "Fragment of Emptiness",
            "FragmentofEmptiness",
            0.5,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Emptiness"),
        ),
        BossItem(
            "Blasphemer's Grasp",
            "BlasphemersGrasp",
            0.25,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Blasphemer's Grasp"),
        ),
        BossItem(
            "Cyclopean Coil",
            "CyclopeanCoil",
            0.25,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Cyclopean Coil"),
        ),
        BossItem(
            "Nebuloch",
            "Nebuloch",
            0.1,
            Matcher(PoeNinjaEndpoint.UNIQUE_WEAPON, "Nebuloch"),
        ),
        BossItem(
            "Hopeshredder",
            "Hopeshredder",
            0.1,
            Matcher(PoeNinjaEndpoint.UNIQUE_WEAPON, "Hopeshredder"),
        ),
        BossItem(
            "Shimmeron",
            "Shimmeron",
            0.1,
            Matcher(PoeNinjaEndpoint.UNIQUE_WEAPON, "Shimmeron"),
        ),
        BossItem(
            "Impresence",
            "Impresence",
            0.2,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Impresence"),
        ),
        BossItem(
            "Orb of Dominance",
            "OrbofDominanceElder",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Orb of Dominance"),
        ),
        BossItem(
            "Watcher's Eye",
            "WatchersEye",
            0.35,
            Matcher(PoeWatchEndpoint.UNIQUE_JEWEL, "Unidentified Watcher's Eye 85", ilvl=85),
        ),
    },
)


TheElderUber = Boss(
    name="The Elder (Uber)",
    short_name="Elder (Uber)",
    entrance_items={
        BossItem(
            "Fragment of Knowledge",
            "FragmentofKnowledge",
            0.5,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Knowledge"),
        ): 1,
        BossItem(
            "Fragment of Terror",
            "FragmentofTerror",
            0.5,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Terror"),
        ): 1,
        BossItem(
            "Fragment of Emptiness",
            "FragmentofEmptiness",
            0.5,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Emptiness"),
        ): 1,
        BossItem(
            "Fragment of Shape",
            "FragmentofShape",
            0.5,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Fragment of Shape"),
        ): 1,
    },
    drops={
        BossItem(
            "Mark of the Shaper",
            "MarkoftheShaper",
            0.35,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Mark of the Shaper"),
        ),
        BossItem(
            "Mark of the Elder",
            "MarkoftheElder",
            0.35,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Mark of the Elder"),
        ),
        BossItem(
            "Voidfletcher",
            "Voidfletcher",
            0.25,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Voidfletcher"),
        ),
        BossItem(
            "Indigon",
            "Indigon",
            0.04,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Indigon"),
        ),
        BossItem(
            "Disintegrator",
            "Disintegrator",
            0.01,
            Matcher(PoeNinjaEndpoint.UNIQUE_WEAPON, "Disintegrator"),
        ),
        BossItem(
            "Watcher's Eye",
            "WatchersEyeUber",
            0.35,
            Matcher(PoeWatchEndpoint.UNIQUE_JEWEL, "Unidentified Watcher's Eye 86+", ilvl=86),
        ),
        BossItem(
            "Orb of Dominance",
            "OrbofDominanceElder",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Orb of Dominance"),
        ),
        BossItem(
            "The Gulf",
            "TheGulf",
            0.04,
            Matcher(PoeNinjaEndpoint.DIVINATION_CARD, "The Gulf"),
        ),
        BossItem(
            "Void of the Elements",
            "VoidoftheElements",
            0.04,
            Matcher(PoeNinjaEndpoint.DIVINATION_CARD, "Void of the Elements"),
        ),
    },
)


TheElderUberUber = Boss(
    name="The Elder (Uber Uber)",
    short_name="Elder (Uber Uber)",
    entrance_items={
        BossItem(
            "Decaying Fragment",
            "DecayingFragment",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Decaying Fragment"),
        ): 5,
    },
    drops={
        BossItem(
            "Call of the Void",
            "CalloftheVoid",
            0.5,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Call of the Void"),
        ),
        BossItem(
            "The Devourer of Minds",
            "TheDevourerofMinds",
            0.3,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "The Devourer of Minds"),
        ),
        BossItem(
            "Soul Ascension",
            "SoulAscension",
            0.1,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Soul Ascension"),
        ),
        BossItem(
            "The Eternity Shroud",
            "TheEternityShroud",
            0.09,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "The Eternity Shroud"),
        ),
        BossItem(
            "Voidforge",
            "Voidforge",
            0.01,
            Matcher(PoeNinjaEndpoint.UNIQUE_WEAPON, "Voidforge"),
        ),
        BossItem(
            "Sublime Vision",
            "SublimeVision",
            0.025,
            Matcher(PoeWatchEndpoint.UNIQUE_JEWEL, "Unidentified Sublime Vision", ilvl=87),
        ),
        BossItem(
            "Impresence",
            "Impresence",
            0.2,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Impresence"),
        ),
        BossItem(
            "Decaying Reliquary Key",
            "DecayingReliquaryKey",
            0.015,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Decaying Reliquary Key"),
        ),
        BossItem(
            "Curio of Decay",
            "CurioofDecay",
            0.05,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Curio of Decay"),
        ),
        BossItem(
            "Watcher's Eye",
            "WatchersEyeUber",
            0.35,
            Matcher(PoeWatchEndpoint.UNIQUE_JEWEL, "Unidentified Watcher's Eye 86+", ilvl=86),
        ),
        BossItem(
            "Orb of Dominance",
            "OrbofDominanceElder",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Orb of Dominance"),
        ),
        BossItem(
            "The Gulf",
            "TheGulf",
            0.04,
            Matcher(PoeNinjaEndpoint.DIVINATION_CARD, "The Gulf"),
        ),
        BossItem(
            "Void of the Elements",
            "VoidoftheElements",
            0.04,
            Matcher(PoeNinjaEndpoint.DIVINATION_CARD, "Void of the Elements"),
        ),
    },
)


Venarius = Boss(
    name="Venarius",
    short_name="Venarius",
    entrance_items={
        BossItem(
            "Cortex",
            "Cortex",
            0.01,
            Matcher(PoeNinjaEndpoint.UNIQUE_MAP, "Cortex"),
        ): 1,
    },
    drops={
        BossItem(
            "Offering to the Serpent",
            "OfferingtotheSerpent",
            0.45,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Offering to the Serpent"),
        ),
        BossItem(
            "Perepiteia",
            "Perepiteia",
            0.45,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Perepiteia"),
        ),
        BossItem(
            "Garb of the Ephemeral",
            "GarboftheEphemeral",
            0.08,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Garb of the Ephemeral"),
        ),
        BossItem(
            "Bottled Faith",
            "BottledFaith",
            0.02,
            Matcher(PoeNinjaEndpoint.UNIQUE_FLASK, "Bottled Faith"),
        ),
        BossItem(
            "The Hook",
            "TheHook",
            0.05,
            Matcher(PoeNinjaEndpoint.DIVINATION_CARD, "The Hook"),
        ),
    },
)


VenariusUber = Boss(
    name="Venarius (Uber)",
    short_name="Venarius (Uber)",
    entrance_items={
        BossItem(
            "Synthesising Fragment",
            "SynthesisingFragment",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Synthesising Fragment"),
        ): 5,
    },
    drops={
        BossItem(
            "Mask of the Tribunal",
            "MaskoftheTribunal",
            0.4,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Mask of the Tribunal"),
        ),
        BossItem(
            "Nebulis",
            "Nebulis",
            0.33,
            Matcher(PoeNinjaEndpoint.UNIQUE_WEAPON, "Nebulis"),
        ),
        BossItem(
            "Circle of Ambition",
            "CircleofAmbition",
            0.17,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Circle of Ambition"),
        ),
        BossItem(
            "The Apostate",
            "TheApostate",
            0.08,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "The Apostate"),
        ),
        BossItem(
            "Rational Doctrine",
            "RationalDoctrine",
            0.02,
            Matcher(PoeNinjaEndpoint.UNIQUE_JEWEL, "Rational Doctrine"),
        ),
        BossItem(
            "Forgotten Reliquary Key",
            "ForgottenReliquaryKey",
            0.015,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Forgotten Reliquary Key"),
        ),
        BossItem(
            "The Hook",
            "TheHook",
            0.05,
            Matcher(PoeNinjaEndpoint.DIVINATION_CARD, "The Hook"),
        ),
    },
)


Sirus = Boss(
    name="Sirus, Awakener of Worlds",
    short_name="Sirus",
    entrance_items={
        BossItem(
            "Drox's Crest",
            "DroxsCrest",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Drox's Crest"),
        ): 1,
        BossItem(
            "Veritania's Crest",
            "VeritaniasCrest",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Veritania's Crest"),
        ): 1,
        BossItem(
            "Baran's Crest",
            "BaransCrest",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Baran's Crest"),
        ): 1,
        BossItem(
            "Al-Hezmin's Crest",
            "Al-HezminsCrest",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Al-Hezmin's Crest"),
        ): 1,
    },
    drops={
        BossItem(
            "Hands of the High Templar",
            "HandsoftheHighTemplar",
            0.45,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Hands of the High Templar"),
        ),
        BossItem(
            "Crown of the Inward Eye",
            "CrownoftheInwardEye",
            0.38,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Crown of the Inward Eye"),
        ),
        BossItem(
            "The Burden of Truth",
            "TheBurdenofTruth",
            0.15,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "The Burden of Truth"),
        ),
        BossItem(
            "Thread of Hope",
            "ThreadofHope",
            0.02,
            Matcher(
                source=PoeWatchEndpoint.UNIQUE_JEWEL, name="Unidentified Thread of Hope", ilvl=86
            ),
        ),
        BossItem(
            "Orb of Dominance",
            "OrbofDominanceSirus",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Orb of Dominance"),
        ),
        BossItem(
            "Awakener's Orb",
            "AwakenersOrb",
            0.15,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Awakener's Orb"),
        ),
        BossItem(
            "A Fate Worse Than Death",
            "AFateWorseThanDeath",
            0.05,
            Matcher(PoeNinjaEndpoint.DIVINATION_CARD, "A Fate Worse Than Death"),
        ),
    },
)


SirusUber = Boss(
    name="Sirus, Awakener of Worlds (Uber)",
    short_name="Sirus (Uber)",
    entrance_items={
        BossItem(
            "Awakening Fragment",
            "AwakeningFragment",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Awakening Fragment"),
        ): 5,
    },
    drops={
        BossItem(
            "Thread of Hope",
            "ThreadofHopeMassive",
            0.55,
            Matcher(
                source=PoeWatchEndpoint.UNIQUE_JEWEL, name="Unidentified Thread of Hope", ilvl=87
            ),
        ),
        BossItem(
            "The Tempest Rising",
            "TheTempestRising",
            0.35,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "The Tempest Rising"),
        ),
        BossItem(
            "Oriath's End",
            "OriathsEnd",
            0.09,
            Matcher(PoeNinjaEndpoint.UNIQUE_FLASK, "Oriath's End"),
        ),
        BossItem(
            "The Saviour",
            "TheSaviour",
            0.01,
            Matcher(PoeNinjaEndpoint.UNIQUE_WEAPON, "The Saviour"),
        ),
        BossItem(
            "Orb of Dominance",
            "OrbofDominanceSirus",
            0.05,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Orb of Dominance"),
        ),
        BossItem(
            "Awakener's Orb",
            "AwakenersOrb",
            0.15,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Awakener's Orb"),
        ),
        BossItem(
            "A Fate Worse Than Death",
            "AFateWorseThanDeath",
            0.05,
            Matcher(PoeNinjaEndpoint.DIVINATION_CARD, "A Fate Worse Than Death"),
        ),
    },
)


TheMaven = Boss(
    name="The Maven",
    short_name="Maven",
    entrance_items={
        BossItem(
            "The Maven's Writ",
            "TheMavensWrit",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "The Maven's Writ"),
        ): 1,
    },
    drops={
        BossItem(
            "Legacy of Fury",
            "LegacyofFury",
            0.45,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Legacy of Fury"),
        ),
        BossItem(
            "Graven's Secret",
            "GravensSecret",
            0.16,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Graven's Secret"),
        ),
        BossItem(
            "Arn's Anguish",
            "ArnsAnguish",
            0.16,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Arn's Anguish"),
        ),
        BossItem(
            "Olesya's Delight",
            "OlesyasDelight",
            0.16,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Olesya's Delight"),
        ),
        BossItem(
            "Doppelgänger Guise",
            "DoppelgängerGuise",
            0.06,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Doppelgänger Guise"),
        ),
        BossItem(
            "Echoforge",
            "Echoforge",
            0.01,
            Matcher(PoeNinjaEndpoint.UNIQUE_WEAPON, "Echoforge"),
        ),
        BossItem(
            "Orb of Conflict",
            "OrbofConflict",
            0.35,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Orb of Conflict"),
        ),
        BossItem(
            "Awakened Added Cold Damage Support",
            "AwakenedAddedColdDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Added Cold Damage Support"),
        ),
        BossItem(
            "Awakened Arrow Nova Support",
            "AwakenedArrowNovaSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Arrow Nova Support"),
        ),
        BossItem(
            "Awakened Cast On Critical Strike Support",
            "AwakenedCastOnCriticalStrikeSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Cast On Critical Strike Support"),
        ),
        BossItem(
            "Awakened Chain Support",
            "AwakenedChainSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Chain Support"),
        ),
        BossItem(
            "Awakened Cold Penetration Support",
            "AwakenedColdPenetrationSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Cold Penetration Support"),
        ),
        BossItem(
            "Awakened Deadly Ailments Support",
            "AwakenedDeadlyAilmentsSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Deadly Ailments Support"),
        ),
        BossItem(
            "Awakened Fork Support",
            "AwakenedForkSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Fork Support"),
        ),
        BossItem(
            "Awakened Greater Multiple Projectiles Support",
            "AwakenedGreaterMultipleProjectilesSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Greater Multiple Projectiles Support"),
        ),
        BossItem(
            "Awakened Swift Affliction Support",
            "AwakenedSwiftAfflictionSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Swift Affliction Support"),
        ),
        BossItem(
            "Awakened Vicious Projectiles Support",
            "AwakenedViciousProjectilesSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Vicious Projectiles Support"),
        ),
        BossItem(
            "Awakened Void Manipulation Support",
            "AwakenedVoidManipulationSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Void Manipulation Support"),
        ),
        BossItem(
            "Awakened Added Chaos Damage Support",
            "AwakenedAddedChaosDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Added Chaos Damage Support"),
        ),
        BossItem(
            "Awakened Added Lightning Damage Support",
            "AwakenedAddedLightningDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Added Lightning Damage Support"),
        ),
        BossItem(
            "Awakened Blasphemy Support",
            "AwakenedBlasphemySupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Blasphemy Support"),
        ),
        BossItem(
            "Awakened Cast While Channelling Support",
            "AwakenedCastWhileChannellingSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Cast While Channelling Support"),
        ),
        BossItem(
            "Awakened Controlled Destruction Support",
            "AwakenedControlledDestructionSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Controlled Destruction Support"),
        ),
        BossItem(
            "Awakened Elemental Focus Support",
            "AwakenedElementalFocusSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Elemental Focus Support"),
        ),
        BossItem(
            "Awakened Hextouch Support",
            "AwakenedHextouchSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Hextouch Support"),
        ),
        BossItem(
            "Awakened Increased Area of Effect Support",
            "AwakenedIncreasedAreaofEffectSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Increased Area of Effect Support"),
        ),
        BossItem(
            "Awakened Lightning Penetration Support",
            "AwakenedLightningPenetrationSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Lightning Penetration Support"),
        ),
        BossItem(
            "Awakened Minion Damage Support",
            "AwakenedMinionDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Minion Damage Support"),
        ),
        BossItem(
            "Awakened Spell Cascade Support",
            "AwakenedSpellCascadeSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Spell Cascade Support"),
        ),
        BossItem(
            "Awakened Spell Echo Support",
            "AwakenedSpellEchoSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Spell Echo Support"),
        ),
        BossItem(
            "Awakened Unbound Ailments Support",
            "AwakenedUnboundAilmentsSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Unbound Ailments Support"),
        ),
        BossItem(
            "Awakened Unleash Support",
            "AwakenedUnleashSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Unleash Support"),
        ),
        BossItem(
            "Awakened Added Fire Damage Support",
            "AwakenedAddedFireDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Added Fire Damage Support"),
        ),
        BossItem(
            "Awakened Ancestral Call Support",
            "AwakenedAncestralCallSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Ancestral Call Support"),
        ),
        BossItem(
            "Awakened Brutality Support",
            "AwakenedBrutalitySupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Brutality Support"),
        ),
        BossItem(
            "Awakened Burning Damage Support",
            "AwakenedBurningDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Burning Damage Support"),
        ),
        BossItem(
            "Awakened Elemental Damage with Attacks Support",
            "AwakenedElementalDamagewithAttacksSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Elemental Damage with Attacks Support"),
        ),
        BossItem(
            "Awakened Fire Penetration Support",
            "AwakenedFirePenetrationSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Fire Penetration Support"),
        ),
        BossItem(
            "Awakened Generosity Support",
            "AwakenedGenerositySupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Generosity Support"),
        ),
        BossItem(
            "Awakened Melee Physical Damage Support",
            "AwakenedMeleePhysicalDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Melee Physical Damage Support"),
        ),
        BossItem(
            "Awakened Melee Splash Support",
            "AwakenedMeleeSplashSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Melee Splash Support"),
        ),
        BossItem(
            "Awakened Multistrike Support",
            "AwakenedMultistrikeSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Multistrike Support"),
        ),
    },
)


TheMavenUber = Boss(
    name="The Maven (Uber)",
    short_name="Maven (Uber)",
    entrance_items={
        BossItem(
            "Reality Fragment",
            "RealityFragment",
            0,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Reality Fragment"),
        ): 5,
    },
    drops={
        BossItem(
            "Viridi's Veil",
            "ViridisVeil",
            0.55,
            Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Viridi's Veil"),
        ),
        BossItem(
            "Impossible Escape",
            "ImpossibleEscape",
            0.33,
            Matcher(PoeNinjaEndpoint.UNIQUE_JEWEL, "Impossible Escape"),
        ),
        BossItem(
            "Progenesis",
            "Progenesis",
            0.11,
            Matcher(PoeNinjaEndpoint.UNIQUE_FLASK, "Progenesis"),
        ),
        BossItem(
            "Grace of the Goddess",
            "GraceoftheGoddess",
            0.005,
            Matcher(PoeNinjaEndpoint.UNIQUE_WEAPON, "Grace of the Goddess"),
        ),
        BossItem(
            "Shiny Reliquary Key",
            "ShinyReliquaryKey",
            0.015,
            Matcher(PoeNinjaEndpoint.FRAGMENT, "Shiny Reliquary Key"),
        ),
        BossItem(
            "Curio of Potential",
            "CurioofPotential",
            0.05,
            Matcher(PoeNinjaEndpoint.UNIQUE_ACCESSORY, "Curio of Potential"),
        ),
        BossItem(
            "Orb of Conflict",
            "OrbofConflict",
            0.35,
            Matcher(PoeNinjaEndpoint.CURRENCY, "Orb of Conflict"),
        ),
        BossItem(
            "Awakened Added Cold Damage Support",
            "AwakenedAddedColdDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Added Cold Damage Support"),
        ),
        BossItem(
            "Awakened Arrow Nova Support",
            "AwakenedArrowNovaSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Arrow Nova Support"),
        ),
        BossItem(
            "Awakened Cast On Critical Strike Support",
            "AwakenedCastOnCriticalStrikeSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Cast On Critical Strike Support"),
        ),
        BossItem(
            "Awakened Chain Support",
            "AwakenedChainSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Chain Support"),
        ),
        BossItem(
            "Awakened Cold Penetration Support",
            "AwakenedColdPenetrationSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Cold Penetration Support"),
        ),
        BossItem(
            "Awakened Deadly Ailments Support",
            "AwakenedDeadlyAilmentsSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Deadly Ailments Support"),
        ),
        BossItem(
            "Awakened Fork Support",
            "AwakenedForkSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Fork Support"),
        ),
        BossItem(
            "Awakened Greater Multiple Projectiles Support",
            "AwakenedGreaterMultipleProjectilesSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Greater Multiple Projectiles Support"),
        ),
        BossItem(
            "Awakened Swift Affliction Support",
            "AwakenedSwiftAfflictionSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Swift Affliction Support"),
        ),
        BossItem(
            "Awakened Vicious Projectiles Support",
            "AwakenedViciousProjectilesSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Vicious Projectiles Support"),
        ),
        BossItem(
            "Awakened Void Manipulation Support",
            "AwakenedVoidManipulationSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Void Manipulation Support"),
        ),
        BossItem(
            "Awakened Added Chaos Damage Support",
            "AwakenedAddedChaosDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Added Chaos Damage Support"),
        ),
        BossItem(
            "Awakened Added Lightning Damage Support",
            "AwakenedAddedLightningDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Added Lightning Damage Support"),
        ),
        BossItem(
            "Awakened Blasphemy Support",
            "AwakenedBlasphemySupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Blasphemy Support"),
        ),
        BossItem(
            "Awakened Cast While Channelling Support",
            "AwakenedCastWhileChannellingSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Cast While Channelling Support"),
        ),
        BossItem(
            "Awakened Controlled Destruction Support",
            "AwakenedControlledDestructionSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Controlled Destruction Support"),
        ),
        BossItem(
            "Awakened Elemental Focus Support",
            "AwakenedElementalFocusSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Elemental Focus Support"),
        ),
        BossItem(
            "Awakened Hextouch Support",
            "AwakenedHextouchSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Hextouch Support"),
        ),
        BossItem(
            "Awakened Increased Area of Effect Support",
            "AwakenedIncreasedAreaofEffectSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Increased Area of Effect Support"),
        ),
        BossItem(
            "Awakened Lightning Penetration Support",
            "AwakenedLightningPenetrationSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Lightning Penetration Support"),
        ),
        BossItem(
            "Awakened Minion Damage Support",
            "AwakenedMinionDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Minion Damage Support"),
        ),
        BossItem(
            "Awakened Spell Cascade Support",
            "AwakenedSpellCascadeSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Spell Cascade Support"),
        ),
        BossItem(
            "Awakened Spell Echo Support",
            "AwakenedSpellEchoSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Spell Echo Support"),
        ),
        BossItem(
            "Awakened Unbound Ailments Support",
            "AwakenedUnboundAilmentsSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Unbound Ailments Support"),
        ),
        BossItem(
            "Awakened Unleash Support",
            "AwakenedUnleashSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Unleash Support"),
        ),
        BossItem(
            "Awakened Added Fire Damage Support",
            "AwakenedAddedFireDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Added Fire Damage Support"),
        ),
        BossItem(
            "Awakened Ancestral Call Support",
            "AwakenedAncestralCallSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Ancestral Call Support"),
        ),
        BossItem(
            "Awakened Brutality Support",
            "AwakenedBrutalitySupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Brutality Support"),
        ),
        BossItem(
            "Awakened Burning Damage Support",
            "AwakenedBurningDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Burning Damage Support"),
        ),
        BossItem(
            "Awakened Elemental Damage with Attacks Support",
            "AwakenedElementalDamagewithAttacksSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Elemental Damage with Attacks Support"),
        ),
        BossItem(
            "Awakened Fire Penetration Support",
            "AwakenedFirePenetrationSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Fire Penetration Support"),
        ),
        BossItem(
            "Awakened Generosity Support",
            "AwakenedGenerositySupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Generosity Support"),
        ),
        BossItem(
            "Awakened Melee Physical Damage Support",
            "AwakenedMeleePhysicalDamageSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Melee Physical Damage Support"),
        ),
        BossItem(
            "Awakened Melee Splash Support",
            "AwakenedMeleeSplashSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Melee Splash Support"),
        ),
        BossItem(
            "Awakened Multistrike Support",
            "AwakenedMultistrikeSupport",
            0.00735,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Multistrike Support"),
        ),
        BossItem(
            "Awakened Enlighten Support",
            "AwakenedEnlightenSupport",
            0.00166,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Enlighten Support"),
        ),
        BossItem(
            "Awakened Enhance Support",
            "AwakenedEnhanceSupport",
            0.00166,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Enhance Support"),
        ),
        BossItem(
            "Awakened Empower Support",
            "AwakenedEmpowerSupport",
            0.00166,
            Matcher(PoeNinjaEndpoint.SKILL_GEM, "Awakened Empower Support"),
        ),
    },
)
