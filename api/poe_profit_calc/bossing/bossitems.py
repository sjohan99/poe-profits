from poe_profit_calc.items import Item, PoeNinjaMatcher, PoeWatchMatcher
from poe_profit_calc.sources import PoeNinjaSource, PoeWatchSource
from poe_profit_calc.tradelink import TradeLink


CurioOfPotential = Item(
    "Curio of Potential",
    "CurioofPotential",
    0.05,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Curio of Potential"),
)

AwakenedHextouchSupport = Item(
    "Awakened Hextouch Support",
    "AwakenedHextouchSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Hextouch Support"),
)

AwakenedViciousProjectilesSupport = Item(
    "Awakened Vicious Projectiles Support",
    "AwakenedViciousProjectilesSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Vicious Projectiles Support"),
)

AwakenedCastWhileChannellingSupport = Item(
    "Awakened Cast While Channelling Support",
    "AwakenedCastWhileChannellingSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Cast While Channelling Support"),
)

Voidfletcher = Item(
    "Voidfletcher",
    "Voidfletcher",
    0.25,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Voidfletcher"),
)

DyingSun = Item(
    "Dying Sun",
    "DyingSun",
    0.01,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_FLASK, "Dying Sun"),
)

AlHezminsCrest = Item(
    "Al-Hezmin's Crest",
    "Al-HezminsCrest",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Al-Hezmin's Crest"),
)

DecayingFragment = Item(
    "Decaying Fragment",
    "DecayingFragment",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Decaying Fragment"),
)

TheEternityShroud = Item(
    "The Eternity Shroud",
    "TheEternityShroud",
    0.09,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "The Eternity Shroud"),
)

SoulAscension = Item(
    "Soul Ascension",
    "SoulAscension",
    0.1,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Soul Ascension"),
)

GravensSecret = Item(
    "Graven's Secret",
    "GravensSecret",
    0.16,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Graven's Secret"),
)

AwakenedMeleeSplashSupport = Item(
    "Awakened Melee Splash Support",
    "AwakenedMeleeSplashSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Melee Splash Support"),
)

AwakenedAncestralCallSupport = Item(
    "Awakened Ancestral Call Support",
    "AwakenedAncestralCallSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Ancestral Call Support"),
)

TwoModWatcherEye = Item(
    "Watcher's Eye",
    "WatchersEye",
    0.35,
    PoeWatchMatcher(PoeWatchSource.UNIQUE_JEWEL, "Unidentified Watcher's Eye 85", ilvl=85),
    trade_link=TradeLink("Watcher's Eye", "Prismatic Jewel", identified=False, max_ilvl=85),
)

EchoesOfCreation = Item(
    "Echoes of Creation",
    "EchoesofCreation",
    0.46,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Echoes of Creation"),
)

DissolutionOfTheFlesh = Item(
    "Dissolution of the Flesh",
    "DissolutionoftheFlesh",
    0.02,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_JEWEL, "Dissolution of the Flesh"),
)

MaskOfTheTribunal = Item(
    "Mask of the Tribunal",
    "MaskoftheTribunal",
    0.4,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Mask of the Tribunal"),
)

ScreamingInvitation = Item(
    "Screaming Invitation",
    "ScreamingInvitation",
    0,
    PoeNinjaMatcher(PoeNinjaSource.INVITATION, "Screaming Invitation"),
)

Nimis = Item(
    "Nimis",
    "Nimis",
    0.01,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Nimis"),
)

ForbiddenFlesh = Item(
    "Forbidden Flesh",
    "ForbiddenFlesh",
    0.05,
    PoeWatchMatcher(PoeWatchSource.UNIQUE_JEWEL, "Unidentified Forbidden Flesh", ilvl=86),
    trade_link=TradeLink("Forbidden Flesh", "Cobalt Jewel", identified=False, max_ilvl=86),
)

AwakenedLightningPenetrationSupport = Item(
    "Awakened Lightning Penetration Support",
    "AwakenedLightningPenetrationSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Lightning Penetration Support"),
)

AwakenedColdPenetrationSupport = Item(
    "Awakened Cold Penetration Support",
    "AwakenedColdPenetrationSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Cold Penetration Support"),
)

AwakenedIncreasedAreaOfEffectSupport = Item(
    "Awakened Increased Area of Effect Support",
    "AwakenedIncreasedAreaofEffectSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Increased Area of Effect Support"),
)

Hopeshredder = Item(
    "Hopeshredder",
    "Hopeshredder",
    0.1,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_WEAPON, "Hopeshredder"),
)

OrbOfDominanceElder = Item(
    "Orb of Dominance",
    "OrbofDominanceElder",
    0.05,
    PoeNinjaMatcher(PoeNinjaSource.CURRENCY, "Orb of Dominance"),
)

ForbiddenFlame = Item(
    "Forbidden Flame",
    "ForbiddenFlame",
    0.05,
    PoeWatchMatcher(PoeWatchSource.UNIQUE_JEWEL, "Unidentified Forbidden Flame", ilvl=86),
    trade_link=TradeLink("Forbidden Flame", "Crimson Jewel", identified=False, max_ilvl=86),
)

Cortex = Item(
    "Cortex",
    "Cortex",
    0.01,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_MAP, "Cortex"),
)

CosmicFragment = Item(
    "Cosmic Fragment",
    "CosmicFragment",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Cosmic Fragment"),
)

Voidforge = Item(
    "Voidforge",
    "Voidforge",
    0.01,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_WEAPON, "Voidforge"),
)

ForbiddenFleshUber = Item(
    "Forbidden Flesh",
    "ForbiddenFleshUber",
    0.05,
    PoeWatchMatcher(PoeWatchSource.UNIQUE_JEWEL, "Unidentified Forbidden Flesh", ilvl=87),
    trade_link=TradeLink("Forbidden Flesh", "Cobalt Jewel", identified=False, min_ilvl=87),
)

AwakenedMultistrikeSupport = Item(
    "Awakened Multistrike Support",
    "AwakenedMultistrikeSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Multistrike Support"),
)

AwakenedUnleashSupport = Item(
    "Awakened Unleash Support",
    "AwakenedUnleashSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Unleash Support"),
)

MarkOfTheElder = Item(
    "Mark of the Elder",
    "MarkoftheElder",
    0.35,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Mark of the Elder"),
)

StarForge = Item(
    "Starforge",
    "Starforge",
    0.005,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_WEAPON, "Starforge"),
)

FragmentOfTheMinotaur = Item(
    "Fragment of the Minotaur",
    "FragmentoftheMinotaur",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Fragment of the Minotaur"),
)

BlazingFragment = Item(
    "Blazing Fragment",
    "BlazingFragment",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Blazing Fragment"),
)

RavenousPassion = Item(
    "Ravenous Passion",
    "RavenousPassion",
    0.66,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Ravenous Passion"),
)

ShinyReliquaryKey = Item(
    "Shiny Reliquary Key",
    "ShinyReliquaryKey",
    0.015,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Shiny Reliquary Key"),
)

AwakenedBruitalitySupport = Item(
    "Awakened Brutality Support",
    "AwakenedBrutalitySupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Brutality Support"),
)

AwakenedDeadlyAilmentsSupport = Item(
    "Awakened Deadly Ailments Support",
    "AwakenedDeadlyAilmentsSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Deadly Ailments Support"),
)

AwakenedSpellCascadeSupport = Item(
    "Awakened Spell Cascade Support",
    "AwakenedSpellCascadeSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Spell Cascade Support"),
)

TheGulf = Item(
    "The Gulf",
    "TheGulf",
    0.04,
    PoeNinjaMatcher(PoeNinjaSource.DIVINATION_CARD, "The Gulf"),
)

Disintegrator = Item(
    "Disintegrator",
    "Disintegrator",
    0.01,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_WEAPON, "Disintegrator"),
)

EldritchOrbOfAnnulment = Item(
    "Eldritch Orb of Annulment",
    "EldritchOrbofAnnulment",
    0.05,
    PoeNinjaMatcher(PoeNinjaSource.CURRENCY, "Eldritch Orb of Annulment"),
)

CurioOfDecay = Item(
    "Curio of Decay",
    "CurioofDecay",
    0.05,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Curio of Decay"),
)

SynthesisingFragment = Item(
    "Synthesising Fragment",
    "SynthesisingFragment",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Synthesising Fragment"),
)

OrbOfConflict = Item(
    "Orb of Conflict",
    "OrbofConflict",
    0.35,
    PoeNinjaMatcher(PoeNinjaSource.CURRENCY, "Orb of Conflict"),
)

TheMavensWrit = Item(
    "The Maven's Writ",
    "TheMavensWrit",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "The Maven's Writ"),
)

AwakenedEnlightenSupport = Item(
    "Awakened Enlighten Support",
    "AwakenedEnlightenSupport",
    0.00166,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Enlighten Support"),
)

AwakenedArrowNovaSupport = Item(
    "Awakened Arrow Nova Support",
    "AwakenedArrowNovaSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Arrow Nova Support"),
)

Shimmeron = Item(
    "Shimmeron",
    "Shimmeron",
    0.1,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_WEAPON, "Shimmeron"),
)

CosmicReliquaryKey = Item(
    "Cosmic Reliquary Key",
    "CosmicReliquaryKey",
    0.01,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Cosmic Reliquary Key"),
)

ExceptionalEldritchEmber = Item(
    "Exceptional Eldritch Ember",
    "ExceptionalEldritchEmber",
    0.15,
    PoeNinjaMatcher(PoeNinjaSource.CURRENCY, "Exceptional Eldritch Ember"),
)

VisceralReliquaryKey = Item(
    "Visceral Reliquary Key",
    "VisceralReliquaryKey",
    0.01,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Visceral Reliquary Key"),
)

AwakeningFragment = Item(
    "Awakening Fragment",
    "AwakeningFragment",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Awakening Fragment"),
)

IncandescentInvitation = Item(
    "Incandescent Invitation",
    "IncandescentInvitation",
    0,
    PoeNinjaMatcher(PoeNinjaSource.INVITATION, "Incandescent Invitation"),
)

AshesOfTheStars = Item(
    "Ashes of the Stars",
    "AshesoftheStars",
    0.33,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Ashes of the Stars"),
)

AwakenedFirePenetrationSupport = Item(
    "Awakened Fire Penetration Support",
    "AwakenedFirePenetrationSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Fire Penetration Support"),
)

AwakenedVoidManipulationSupport = Item(
    "Awakened Void Manipulation Support",
    "AwakenedVoidManipulationSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Void Manipulation Support"),
)

AwakenedEnhanceSupport = Item(
    "Awakened Enhance Support",
    "AwakenedEnhanceSupport",
    0.00166,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Enhance Support"),
)

TheBurdenOfTruth = Item(
    "The Burden of Truth",
    "TheBurdenofTruth",
    0.15,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "The Burden of Truth"),
)

HandsOfTheHighTemplar = Item(
    "Hands of the High Templar",
    "HandsoftheHighTemplar",
    0.45,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Hands of the High Templar"),
)

RationalDoctrine = Item(
    "Rational Doctrine",
    "RationalDoctrine",
    0.02,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_JEWEL, "Rational Doctrine"),
)

DroxsCrest = Item(
    "Drox's Crest",
    "DroxsCrest",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Drox's Crest"),
)

FragmentOfTerror = Item(
    "Fragment of Terror",
    "FragmentofTerror",
    0.5,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Fragment of Terror"),
)

DecayingReliquaryKey = Item(
    "Decaying Reliquary Key",
    "DecayingReliquaryKey",
    0.015,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Decaying Reliquary Key"),
)

ViridisVeil = Item(
    "Viridi's Veil",
    "ViridisVeil",
    0.55,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Viridi's Veil"),
)

OlesyasDelight = Item(
    "Olesya's Delight",
    "OlesyasDelight",
    0.16,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Olesya's Delight"),
)

ArnsAnguish = Item(
    "Arn's Anguish",
    "ArnsAnguish",
    0.16,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Arn's Anguish"),
)

AwakenedChainSupport = Item(
    "Awakened Chain Support",
    "AwakenedChainSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Chain Support"),
)

ThreeModWatcherEye = Item(
    "Watcher's Eye",
    "WatchersEyeUber",
    0.35,
    PoeWatchMatcher(PoeWatchSource.UNIQUE_JEWEL, "Unidentified Watcher's Eye 86+", ilvl=86),
    trade_link=TradeLink("Watcher's Eye", "Prismatic Jewel", identified=False, min_ilvl=86),
)

OrbOfDominanceShaper = Item(
    "Orb of Dominance",
    "OrbofDominanceShaper",
    0.01,
    PoeNinjaMatcher(PoeNinjaSource.CURRENCY, "Orb of Dominance"),
)

TheHook = Item(
    "The Hook",
    "TheHook",
    0.05,
    PoeNinjaMatcher(PoeNinjaSource.DIVINATION_CARD, "The Hook"),
)

VeritaniasCrest = Item(
    "Veritania's Crest",
    "VeritaniasCrest",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Veritania's Crest"),
)

TheAnnihilatingLight = Item(
    "The Annihilating Light",
    "TheAnnihilatingLight",
    0.475,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_WEAPON, "The Annihilating Light"),
)

FragmentOfKnowledge = Item(
    "Fragment of Knowledge",
    "FragmentofKnowledge",
    0.5,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Fragment of Knowledge"),
)

CurioOfConsumption = Item(
    "Curio of Consumption",
    "CurioofConsumption",
    0.05,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Curio of Consumption"),
)

AwakenedGenerositySupport = Item(
    "Awakened Generosity Support",
    "AwakenedGenerositySupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Generosity Support"),
)

AwakenedGreaterMultipleProjectilesSupport = Item(
    "Awakened Greater Multiple Projectiles Support",
    "AwakenedGreaterMultipleProjectilesSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Greater Multiple Projectiles Support"),
)

ThreadOfHopeMassive = Item(
    "Thread of Hope",
    "ThreadofHopeMassive",
    0.55,
    PoeWatchMatcher(
        source=PoeWatchSource.UNIQUE_JEWEL, name="Unidentified Thread of Hope", ilvl=87
    ),
)

ThreadOfHope = Item(
    "Thread of Hope",
    "ThreadofHope",
    0.02,
    PoeWatchMatcher(
        source=PoeWatchSource.UNIQUE_JEWEL, name="Unidentified Thread of Hope", ilvl=86
    ),
    trade_link=TradeLink("Thread of Hope", "Crimson Jewel", identified=False, max_ilvl=86),
)

EldritchExaltedOrb = Item(
    "Eldritch Exalted Orb",
    "EldritchExaltedOrb",
    0.05,
    PoeNinjaMatcher(PoeNinjaSource.CURRENCY, "Eldritch Exalted Orb"),
)

EldritchChaosOrb = Item(
    "Eldritch Chaos Orb",
    "EldritchChaosOrb",
    0.05,
    PoeNinjaMatcher(PoeNinjaSource.CURRENCY, "Eldritch Chaos Orb"),
)

FragmentOfEnslavement = Item(
    "Fragment of Enslavement",
    "FragmentofEnslavement",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Fragment of Enslavement"),
)

OfferingToTheSerpent = Item(
    "Offering to the Serpent",
    "OfferingtotheSerpent",
    0.45,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Offering to the Serpent"),
)

GraceOfTheGoddess = Item(
    "Grace of the Goddess",
    "GraceoftheGoddess",
    0.005,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_WEAPON, "Grace of the Goddess"),
)

DoppelgangerGuise = Item(
    "Doppelgänger Guise",
    "DoppelgängerGuise",
    0.06,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Doppelgänger Guise"),
)

LegacyOfFury = Item(
    "Legacy of Fury",
    "LegacyofFury",
    0.45,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Legacy of Fury"),
)

AwakenedBlasphemySupport = Item(
    "Awakened Blasphemy Support",
    "AwakenedBlasphemySupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Blasphemy Support"),
)

Indigon = Item(
    "Indigon",
    "Indigon",
    0.04,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Indigon"),
)

EntropicDevastation = Item(
    "Entropic Devastation",
    "EntropicDevastation",
    0.2,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Entropic Devastation"),
)

Dawnstrider = Item(
    "Dawnstrider",
    "Dawnstrider",
    0.65,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Dawnstrider"),
)

ForgottenReliquaryKey = Item(
    "Forgotten Reliquary Key",
    "ForgottenReliquaryKey",
    0.015,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Forgotten Reliquary Key"),
)

CrystallisedOmniscience = Item(
    "Crystallised Omniscience",
    "CrystallisedOmniscience",
    0.025,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Crystallised Omniscience"),
)

FragmentOfShape = Item(
    "Fragment of Shape",
    "FragmentofShape",
    0.5,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Fragment of Shape"),
)

AnnihilationsApproach = Item(
    "Annihilation's Approach",
    "AnnihilationsApproach",
    0.25,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Annihilation's Approach"),
)

AwakenedSpellEchoSupport = Item(
    "Awakened Spell Echo Support",
    "AwakenedSpellEchoSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Spell Echo Support"),
)

AwakenedControlledDestructionSupport = Item(
    "Awakened Controlled Destruction Support",
    "AwakenedControlledDestructionSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Controlled Destruction Support"),
)

AwakenersOrb = Item(
    "Awakener's Orb",
    "AwakenersOrb",
    0.15,
    PoeNinjaMatcher(PoeNinjaSource.CURRENCY, "Awakener's Orb"),
)

Impresence = Item(
    "Impresence",
    "Impresence",
    0.2,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Impresence"),
)

ShapersTouch = Item(
    "Shaper's Touch",
    "ShapersTouch",
    0.56,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Shaper's Touch"),
)

FragmentOfTheChimera = Item(
    "Fragment of the Chimera",
    "FragmentoftheChimera",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Fragment of the Chimera"),
)

FragmentOfEradication = Item(
    "Fragment of Eradication",
    "FragmentofEradication",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Fragment of Eradication"),
)

Perepiteia = Item(
    "Perepiteia",
    "Perepiteia",
    0.45,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Perepiteia"),
)

CircleOfAmbition = Item(
    "Circle of Ambition",
    "CircleofAmbition",
    0.17,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Circle of Ambition"),
)

ImpossibleEscape = Item(
    "Impossible Escape",
    "ImpossibleEscape",
    0.33,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_JEWEL, "Impossible Escape"),
)

Echoforge = Item(
    "Echoforge",
    "Echoforge",
    0.01,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_WEAPON, "Echoforge"),
)

AwakenedAddedChaosDamageSupport = Item(
    "Awakened Added Chaos Damage Support",
    "AwakenedAddedChaosDamageSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Added Chaos Damage Support"),
)

AwakenedBurningDamageSupport = Item(
    "Awakened Burning Damage Support",
    "AwakenedBurningDamageSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Burning Damage Support"),
)

MarkOfTheShaper = Item(
    "Mark of the Shaper",
    "MarkoftheShaper",
    0.35,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Mark of the Shaper"),
)

BlashphemersGrasp = Item(
    "Blasphemer's Grasp",
    "BlasphemersGrasp",
    0.25,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Blasphemer's Grasp"),
)

VoidWalker = Item(
    "Voidwalker",
    "Voidwalker",
    0.33,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Voidwalker"),
)

TheApostate = Item(
    "The Apostate",
    "TheApostate",
    0.08,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "The Apostate"),
)

CurioOfAbsorption = Item(
    "Curio of Absorption",
    "CurioofAbsorption",
    0.05,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Curio of Absorption"),
)

DevouringFragment = Item(
    "Devouring Fragment",
    "DevouringFragment",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Devouring Fragment"),
)

ForbiddenFlameUber = Item(
    "Forbidden Flame",
    "ForbiddenFlameUber",
    0.05,
    PoeWatchMatcher(PoeWatchSource.UNIQUE_JEWEL, "Unidentified Forbidden Flame", ilvl=87),
    trade_link=TradeLink("Forbidden Flame", "Crimson Jewel", identified=False, min_ilvl=87),
)

AwakenedUnboundAilmentsSupport = Item(
    "Awakened Unbound Ailments Support",
    "AwakenedUnboundAilmentsSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Unbound Ailments Support"),
)

AwakenedElementalFocusSupport = Item(
    "Awakened Elemental Focus Support",
    "AwakenedElementalFocusSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Elemental Focus Support"),
)

OriathsEnd = Item(
    "Oriath's End",
    "OriathsEnd",
    0.09,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_FLASK, "Oriath's End"),
)

AFateWorseThanDeath = Item(
    "A Fate Worse Than Death",
    "AFateWorseThanDeath",
    0.05,
    PoeNinjaMatcher(PoeNinjaSource.DIVINATION_CARD, "A Fate Worse Than Death"),
)

OrbOfDominanceSirus = Item(
    "Orb of Dominance",
    "OrbofDominanceSirus",
    0.05,
    PoeNinjaMatcher(PoeNinjaSource.CURRENCY, "Orb of Dominance"),
)

SolsticeVigil = Item(
    "Solstice Vigil",
    "SolsticeVigil",
    0.1,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Solstice Vigil"),
)

FragmentOfPurification = Item(
    "Fragment of Purification",
    "FragmentofPurification",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Fragment of Purification"),
)

GarbOfTheEphemeral = Item(
    "Garb of the Ephemeral",
    "GarboftheEphemeral",
    0.08,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Garb of the Ephemeral"),
)

TheGluttonousTide = Item(
    "The Gluttonous Tide",
    "TheGluttonousTide",
    0.5,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_WEAPON, "The Gluttonous Tide"),
)

FragmentOfEmptiness = Item(
    "Fragment of Emptiness",
    "FragmentofEmptiness",
    0.5,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Fragment of Emptiness"),
)

Progenesis = Item(
    "Progenesis",
    "Progenesis",
    0.11,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_FLASK, "Progenesis"),
)

AwakenedForkSupport = Item(
    "Awakened Fork Support",
    "AwakenedForkSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Fork Support"),
)

AwakenedCastOnCriticalStrikeSupport = Item(
    "Awakened Cast On Critical Strike Support",
    "AwakenedCastOnCriticalStrikeSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Cast On Critical Strike Support"),
)

VoidOfTheElements = Item(
    "Void of the Elements",
    "VoidoftheElements",
    0.04,
    PoeNinjaMatcher(PoeNinjaSource.DIVINATION_CARD, "Void of the Elements"),
)

CyclopeanCoil = Item(
    "Cyclopean Coil",
    "CyclopeanCoil",
    0.25,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Cyclopean Coil"),
)

Dawnbreaker = Item(
    "Dawnbreaker",
    "Dawnbreaker",
    0.33,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Dawnbreaker"),
)

CallOfTheVoid = Item(
    "Call of the Void",
    "CalloftheVoid",
    0.5,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "Call of the Void"),
)

RealityFragment = Item(
    "Reality Fragment",
    "RealityFragment",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Reality Fragment"),
)

TheCelestialBrace = Item(
    "The Celestial Brace",
    "TheCelestialBrace",
    0.25,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "The Celestial Brace"),
)

AwakenedEmpowerSupport = Item(
    "Awakened Empower Support",
    "AwakenedEmpowerSupport",
    0.00166,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Empower Support"),
)

AwakenedMinionDamageSupport = Item(
    "Awakened Minion Damage Support",
    "AwakenedMinionDamageSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Minion Damage Support"),
)

AwakenedAddedColdDamageSupport = Item(
    "Awakened Added Cold Damage Support",
    "AwakenedAddedColdDamageSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Added Cold Damage Support"),
)

TheSaviour = Item(
    "The Saviour",
    "TheSaviour",
    0.01,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_WEAPON, "The Saviour"),
)

TheTidesOfTime = Item(
    "The Tides of Time",
    "TheTidesofTime",
    0.33,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ACCESSORY, "The Tides of Time"),
)

FragmentOfConstriction = Item(
    "Fragment of Constriction",
    "FragmentofConstriction",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Fragment of Constriction"),
)

BottledFaith = Item(
    "Bottled Faith",
    "BottledFaith",
    0.02,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_FLASK, "Bottled Faith"),
)

BaransCrest = Item(
    "Baran's Crest",
    "BaransCrest",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Baran's Crest"),
)

MeldingOfTheFlesh = Item(
    "Melding of the Flesh",
    "MeldingoftheFlesh",
    0.02,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_JEWEL, "Melding of the Flesh"),
    trade_link=TradeLink("Melding of the Flesh", "Cobalt Jewel", identified=False),
)

InextricableFate = Item(
    "Inextricable Fate",
    "InextricableFate",
    0.5,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Inextricable Fate"),
)

AwakenedSwiftAfflictionSupport = Item(
    "Awakened Swift Affliction Support",
    "AwakenedSwiftAfflictionSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Swift Affliction Support"),
)

AwakenedAddedFireDamageSupport = Item(
    "Awakened Added Fire Damage Support",
    "AwakenedAddedFireDamageSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Added Fire Damage Support"),
)

TheTempestRising = Item(
    "The Tempest Rising",
    "TheTempestRising",
    0.35,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "The Tempest Rising"),
)

Nebuloch = Item(
    "Nebuloch",
    "Nebuloch",
    0.1,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_WEAPON, "Nebuloch"),
)

FragmentOfThePhoenix = Item(
    "Fragment of the Phoenix",
    "FragmentofthePhoenix",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Fragment of the Phoenix"),
)

Nebulis = Item(
    "Nebulis",
    "Nebulis",
    0.33,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_WEAPON, "Nebulis"),
)

TheDevourerOfMinds = Item(
    "The Devourer of Minds",
    "TheDevourerofMinds",
    0.3,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "The Devourer of Minds"),
)

ArchiveReliquaryKey = Item(
    "Archive Reliquary Key",
    "ArchiveReliquaryKey",
    0.015,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Archive Reliquary Key"),
)

AwakenedMeleePhysicalDamageSupport = Item(
    "Awakened Melee Physical Damage Support",
    "AwakenedMeleePhysicalDamageSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Melee Physical Damage Support"),
)

AwakenedElementalDamageWithAttacksSupport = Item(
    "Awakened Elemental Damage with Attacks Support",
    "AwakenedElementalDamagewithAttacksSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Elemental Damage with Attacks Support"),
)

AwakenedAddedLightningDamageSupport = Item(
    "Awakened Added Lightning Damage Support",
    "AwakenedAddedLightningDamageSupport",
    0.00735,
    PoeNinjaMatcher(PoeNinjaSource.SKILL_GEM, "Awakened Added Lightning Damage Support"),
)

CrownOfTheInwardEye = Item(
    "Crown of the Inward Eye",
    "CrownoftheInwardEye",
    0.38,
    PoeNinjaMatcher(PoeNinjaSource.UNIQUE_ARMOUR, "Crown of the Inward Eye"),
)

SublimeVision = Item(
    "Sublime Vision",
    "SublimeVision",
    0.025,
    PoeWatchMatcher(PoeWatchSource.UNIQUE_JEWEL, "Unidentified Sublime Vision", ilvl=87),
    trade_link=TradeLink("Sublime Vision", "Prismatic Jewel", identified=False),
)

FragmentOfTheHydra = Item(
    "Fragment of the Hydra",
    "FragmentoftheHydra",
    0,
    PoeNinjaMatcher(PoeNinjaSource.FRAGMENT, "Fragment of the Hydra"),
)

ExceptionalEldritchIchor = Item(
    "Exceptional Eldritch Ichor",
    "ExceptionalEldritchIchor",
    0.15,
    PoeNinjaMatcher(PoeNinjaSource.CURRENCY, "Exceptional Eldritch Ichor"),
)
