from dataclasses import dataclass
from poe_profit_calc.items import Item
from poe_profit_calc.bossing.bossitems import *


@dataclass
class Boss:
    """Poe boss information.

    Attributes:
        name (str): Boss name.
        entrance_items (dict[Item, int]): Items required to enter the boss fight, with the item as the key and the quantity as the value.
        drops (List[ItemInfo]): All Items that the boss drops.
    """

    name: str
    entrance_items: dict[Item, int]
    drops: set[Item]

    def items(self):
        return self.drops.union(set(self.entrance_items))


TheSearingExarch = Boss(
    name="The Searing Exarch",
    entrance_items={IncandescentInvitation: 1},
    drops={
        Dawnbreaker,
        Dawnstrider,
        DissolutionOfTheFlesh,
        ForbiddenFlame,
        ExceptionalEldritchEmber,
        EldritchOrbOfAnnulment,
        EldritchChaosOrb,
        EldritchExaltedOrb,
    },
)


TheSearingExarchUber = Boss(
    name="The Searing Exarch (Uber)",
    entrance_items={BlazingFragment: 5},
    drops={
        TheAnnihilatingLight,
        AnnihilationsApproach,
        TheCelestialBrace,
        CrystallisedOmniscience,
        ArchiveReliquaryKey,
        CurioOfAbsorption,
        ForbiddenFlameUber,
        ExceptionalEldritchEmber,
        EldritchOrbOfAnnulment,
        EldritchChaosOrb,
        EldritchExaltedOrb,
    },
)


TheEaterOfWorlds = Boss(
    name="The Eater of Worlds",
    entrance_items={ScreamingInvitation: 1},
    drops={
        TheGluttonousTide,
        InextricableFate,
        MeldingOfTheFlesh,
        ForbiddenFlesh,
        ExceptionalEldritchIchor,
        EldritchOrbOfAnnulment,
        EldritchChaosOrb,
        EldritchExaltedOrb,
    },
)


TheEaterOfWorldsUber = Boss(
    name="The Eater of Worlds (Uber)",
    entrance_items={DevouringFragment: 5},
    drops={
        Nimis,
        RavenousPassion,
        AshesOfTheStars,
        VisceralReliquaryKey,
        CurioOfConsumption,
        ForbiddenFleshUber,
        ExceptionalEldritchIchor,
        EldritchOrbOfAnnulment,
        EldritchChaosOrb,
        EldritchExaltedOrb,
    },
)


TheShaper = Boss(
    name="The Shaper",
    entrance_items={
        FragmentOfTheHydra: 1,
        FragmentOfTheMinotaur: 1,
        FragmentOfThePhoenix: 1,
        FragmentOfTheChimera: 1,
    },
    drops={
        ShapersTouch,
        VoidWalker,
        SolsticeVigil,
        DyingSun,
        FragmentOfKnowledge,
        FragmentOfShape,
        OrbOfDominanceShaper,
    },
)


TheShaperUber = Boss(
    name="The Shaper (Uber)",
    entrance_items={
        CosmicFragment: 5,
    },
    drops={
        EchoesOfCreation,
        TheTidesOfTime,
        EntropicDevastation,
        StarForge,
        SublimeVision,
        CosmicReliquaryKey,
        FragmentOfKnowledge,
        FragmentOfShape,
        OrbOfDominanceShaper,
    },
)


TheElder = Boss(
    name="The Elder",
    entrance_items={
        FragmentOfPurification: 1,
        FragmentOfConstriction: 1,
        FragmentOfEnslavement: 1,
        FragmentOfEradication: 1,
    },
    drops={
        FragmentOfTerror,
        FragmentOfEmptiness,
        BlashphemersGrasp,
        CyclopeanCoil,
        Nebuloch,
        Hopeshredder,
        Shimmeron,
        Impresence,
        OrbOfDominanceElder,
        TwoModWatcherEye,
    },
)


TheElderUber = Boss(
    name="The Elder (Uber)",
    entrance_items={
        FragmentOfKnowledge: 1,
        FragmentOfTerror: 1,
        FragmentOfEmptiness: 1,
        FragmentOfShape: 1,
    },
    drops={
        MarkOfTheShaper,
        MarkOfTheElder,
        Voidfletcher,
        Indigon,
        Disintegrator,
        ThreeModWatcherEye,
        OrbOfDominanceElder,
        TheGulf,
        VoidOfTheElements,
    },
)


TheElderUberUber = Boss(
    name="The Elder (Uber Uber)",
    entrance_items={
        DecayingFragment: 5,
    },
    drops={
        CallOfTheVoid,
        TheDevourerOfMinds,
        SoulAscension,
        TheEternityShroud,
        Voidforge,
        SublimeVision,
        Impresence,
        DecayingReliquaryKey,
        CurioOfDecay,
        ThreeModWatcherEye,
        OrbOfDominanceElder,
        TheGulf,
        VoidOfTheElements,
    },
)


Venarius = Boss(
    name="Venarius",
    entrance_items={
        Cortex: 1,
    },
    drops={
        OfferingToTheSerpent,
        Perepiteia,
        GarbOfTheEphemeral,
        BottledFaith,
        TheHook,
    },
)


VenariusUber = Boss(
    name="Venarius (Uber)",
    entrance_items={
        SynthesisingFragment: 5,
    },
    drops={
        MaskOfTheTribunal,
        Nebulis,
        CircleOfAmbition,
        TheApostate,
        RationalDoctrine,
        ForgottenReliquaryKey,
        TheHook,
    },
)


Sirus = Boss(
    name="Sirus, Awakener of Worlds",
    entrance_items={
        DroxsCrest: 1,
        VeritaniasCrest: 1,
        BaransCrest: 1,
        AlHezminsCrest: 1,
    },
    drops={
        HandsOfTheHighTemplar,
        CrownOfTheInwardEye,
        TheBurdenOfTruth,
        ThreadOfHope,
        OrbOfDominanceSirus,
        AwakenersOrb,
        AFateWorseThanDeath,
    },
)


SirusUber = Boss(
    name="Sirus, Awakener of Worlds (Uber)",
    entrance_items={
        AwakeningFragment: 5,
    },
    drops={
        ThreadOfHopeMassive,
        TheTempestRising,
        OriathsEnd,
        TheSaviour,
        OrbOfDominanceSirus,
        AwakenersOrb,
        AFateWorseThanDeath,
    },
)


TheMaven = Boss(
    name="The Maven",
    entrance_items={
        TheMavensWrit: 1,
    },
    drops={
        LegacyOfFury,
        GravensSecret,
        ArnsAnguish,
        OlesyasDelight,
        DoppelgangerGuise,
        Echoforge,
        OrbOfConflict,
        AwakenedAddedColdDamageSupport,
        AwakenedArrowNovaSupport,
        AwakenedCastOnCriticalStrikeSupport,
        AwakenedChainSupport,
        AwakenedColdPenetrationSupport,
        AwakenedDeadlyAilmentsSupport,
        AwakenedForkSupport,
        AwakenedGreaterMultipleProjectilesSupport,
        AwakenedSwiftAfflictionSupport,
        AwakenedViciousProjectilesSupport,
        AwakenedVoidManipulationSupport,
        AwakenedAddedChaosDamageSupport,
        AwakenedAddedLightningDamageSupport,
        AwakenedBlasphemySupport,
        AwakenedCastWhileChannellingSupport,
        AwakenedControlledDestructionSupport,
        AwakenedElementalFocusSupport,
        AwakenedHextouchSupport,
        AwakenedIncreasedAreaOfEffectSupport,
        AwakenedLightningPenetrationSupport,
        AwakenedMinionDamageSupport,
        AwakenedSpellCascadeSupport,
        AwakenedSpellEchoSupport,
        AwakenedUnboundAilmentsSupport,
        AwakenedUnleashSupport,
        AwakenedAddedFireDamageSupport,
        AwakenedAncestralCallSupport,
        AwakenedBruitalitySupport,
        AwakenedBurningDamageSupport,
        AwakenedElementalDamageWithAttacksSupport,
        AwakenedFirePenetrationSupport,
        AwakenedGenerositySupport,
        AwakenedMeleePhysicalDamageSupport,
        AwakenedMeleeSplashSupport,
        AwakenedMultistrikeSupport,
    },
)


TheMavenUber = Boss(
    name="The Maven (Uber)",
    entrance_items={
        RealityFragment: 5,
    },
    drops={
        ViridisVeil,
        ImpossibleEscape,
        Progenesis,
        GraceOfTheGoddess,
        ShinyReliquaryKey,
        CurioOfPotential,
        OrbOfConflict,
        AwakenedAddedColdDamageSupport,
        AwakenedArrowNovaSupport,
        AwakenedCastOnCriticalStrikeSupport,
        AwakenedChainSupport,
        AwakenedColdPenetrationSupport,
        AwakenedDeadlyAilmentsSupport,
        AwakenedForkSupport,
        AwakenedGreaterMultipleProjectilesSupport,
        AwakenedSwiftAfflictionSupport,
        AwakenedViciousProjectilesSupport,
        AwakenedVoidManipulationSupport,
        AwakenedAddedChaosDamageSupport,
        AwakenedAddedLightningDamageSupport,
        AwakenedBlasphemySupport,
        AwakenedCastWhileChannellingSupport,
        AwakenedControlledDestructionSupport,
        AwakenedElementalFocusSupport,
        AwakenedHextouchSupport,
        AwakenedIncreasedAreaOfEffectSupport,
        AwakenedLightningPenetrationSupport,
        AwakenedMinionDamageSupport,
        AwakenedSpellCascadeSupport,
        AwakenedSpellEchoSupport,
        AwakenedUnboundAilmentsSupport,
        AwakenedUnleashSupport,
        AwakenedAddedFireDamageSupport,
        AwakenedAncestralCallSupport,
        AwakenedBruitalitySupport,
        AwakenedBurningDamageSupport,
        AwakenedElementalDamageWithAttacksSupport,
        AwakenedFirePenetrationSupport,
        AwakenedGenerositySupport,
        AwakenedMeleePhysicalDamageSupport,
        AwakenedMeleeSplashSupport,
        AwakenedMultistrikeSupport,
        AwakenedEnlightenSupport,
        AwakenedEnhanceSupport,
        AwakenedEmpowerSupport,
    },
)
