from bin.stats.profstats import calculate_profit_probability as cpp_stats
from bin.stats.profsim import calculate_profit_probability as cpp_sim
from bin.stats.profsim import simulate_kills
import matplotlib.pyplot as plt

true = True
false = False
null = None

ENTRANCE_FEE = 500
NUM_KILLS = 100
NUM_SIMULATIONS = 2500

ITEMS = [
    {
        "name": "Awakened Added Cold Damage Support",
        "price": 20,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0FkZGVkQ29sZERhbWFnZVBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/8fef150dd7/AddedColdDamagePlus.png",
    },
    {
        "name": "Awakened Arrow Nova Support",
        "price": 28.8,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0dyZWVuUmFpblBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/84da19af8c/GreenRainPlus.png",
    },
    {
        "name": "Awakened Increased Area of Effect Support",
        "price": 530.6,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0luY3JlYXNlZEFPRVBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/360e9e4ed5/IncreasedAOEPlus.png",
    },
    {
        "name": "Orb of Conflict",
        "price": 275.05,
        "droprate": 0.35,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvQ29uZmxpY3RPcmJSYW5rMSIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/e1919976c3/ConflictOrbRank1.png",
    },
    {
        "name": "Curio of Potential",
        "price": 151.6,
        "droprate": 0.05,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQW11bGV0cy9QaW5uYWNsZUZyYWdtZW50TWF2ZW4iLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/53c751ef5d/PinnacleFragmentMaven.png",
    },
    {
        "name": "Awakened Blasphemy Support",
        "price": 30,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0F1cmlmeVBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/fbdc11b158/AurifyPlus.png",
    },
    {
        "name": "Awakened Spell Cascade Support",
        "price": 272.88,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL1NwZWxsQ2FzY2FkZVBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/7a316ceb5c/SpellCascadePlus.png",
    },
    {
        "name": "Awakened Spell Echo Support",
        "price": 8034.8,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0VjaG9QbHVzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/9cccabda03/EchoPlus.png",
    },
    {
        "name": "Awakened Unbound Ailments Support",
        "price": 40,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL1VuYm91bmRBaWxtZW50UGx1cyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/41b8082cb4/UnboundAilmentPlus.png",
    },
    {
        "name": "Awakened Enhance Support",
        "price": 20996.6,
        "droprate": 0.00166,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL2VuaGFuY2VwbHVzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/d3de7b3bd1/enhanceplus.png",
    },
    {
        "name": "Awakened Elemental Focus Support",
        "price": 100,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0VsZW1lbnRhbEZvY3VzUGx1cyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/a84d493e28/ElementalFocusPlus.png",
    },
    {
        "name": "Awakened Multistrike Support",
        "price": 44373.32,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL011bHRpcGxlQXR0YWNrc1BsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/c32ddc2121/MultipleAttacksPlus.png",
    },
    {
        "name": "Awakened Melee Splash Support",
        "price": 10,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL1NwbGFzaFBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/8c6dd76bf4/SplashPlus.png",
    },
    {
        "name": "Awakened Cast While Channelling Support",
        "price": 29,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0Nhc3RXaGlsZUNoYW5uZWxpbmdQbHVzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/b6365df6cb/CastWhileChannelingPlus.png",
    },
    {
        "name": "Awakened Generosity Support",
        "price": 50,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0dlbmVyb3NpdHlQbHVzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/14d887c794/GenerosityPlus.png",
    },
    {
        "name": "Grace of the Goddess",
        "price": 1212.8,
        "droprate": 0.005,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9PbmVIYW5kV2VhcG9ucy9XYW5kcy9VYmVyTWF2ZW5XYW5kIiwidyI6MSwiaCI6Mywic2NhbGUiOjF9XQ/1e06b23a5b/UberMavenWand.png",
    },
    {
        "name": "Awakened Fire Penetration Support",
        "price": 10,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0ZpcmVQZW5ldHJhdGlvblBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/b1308cf253/FirePenetrationPlus.png",
    },
    {
        "name": "Awakened Burning Damage Support",
        "price": 35,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0luY3JlYXNlZEJ1cm5EdXJhdGlvblBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/021c221c69/IncreasedBurnDurationPlus.png",
    },
    {
        "name": "Awakened Empower Support",
        "price": 27288,
        "droprate": 0.00166,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0VtcG93ZXJQbHVzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/eb0e6f91ed/EmpowerPlus.png",
    },
    {
        "name": "Impossible Escape",
        "price": 24.5,
        "droprate": 0.33,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvSmV3ZWxzL01pbmRib3JlUGVhcmwiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/367683a1bb/MindborePearl.png",
    },
    {
        "name": "Awakened Deadly Ailments Support",
        "price": 20,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0RlYWRseUFpbG1lbnRzUGx1cyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/68c620c3dc/DeadlyAilmentsPlus.png",
    },
    {
        "name": "Awakened Enlighten Support",
        "price": 68371.6,
        "droprate": 0.00166,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0VubGlnaHRlbnBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/7ec7d0544d/Enlightenplus.png",
    },
    {
        "name": "Awakened Void Manipulation Support",
        "price": 110,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL1ZvaWRNYW5pcHVsYXRpb25QbHVzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/9223d42a35/VoidManipulationPlus.png",
    },
    {
        "name": "Awakened Minion Damage Support",
        "price": 25,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL01pbmlvbkRhbWFnZVBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/5a905affec/MinionDamagePlus.png",
    },
    {
        "name": "Shiny Reliquary Key",
        "price": 0,
        "droprate": 0.015,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvTWFwcy9NYXZlbkZvaWwiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/114c341a3c/MavenFoil.png",
    },
    {
        "name": "Awakened Greater Multiple Projectiles Support",
        "price": 4396.4,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0dyZWF0ZXJNdWx0aXBsZVByb2plY3RpbGVzUGx1cyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/720eb18ad1/GreaterMultipleProjectilesPlus.png",
    },
    {
        "name": "Awakened Hextouch Support",
        "price": 19,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0N1cnNlT25IaXRQbHVzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/bae0341d74/CurseOnHitPlus.png",
    },
    {
        "name": "Awakened Unleash Support",
        "price": 118.58,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL1VubGVhc2hQbHVzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/107949fc2b/UnleashPlus.png",
    },
    {
        "name": "Awakened Elemental Damage with Attacks Support",
        "price": 454.8,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL1dlYXBvbkVsZW1lbnRhbERhbWFnZVBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/2d6aa43759/WeaponElementalDamagePlus.png",
    },
    {
        "name": "Awakened Swift Affliction Support",
        "price": 45,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL1N1cHBvcnRSYXBpZERlY2F5UGx1cyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/275f8da8d1/SupportRapidDecayPlus.png",
    },
    {
        "name": "Awakened Added Lightning Damage Support",
        "price": 30,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0FkZGVkTGlnaHRuaW5nRGFtYWdlUGx1cyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/12f4edd322/AddedLightningDamagePlus.png",
    },
    {
        "name": "Awakened Ancestral Call Support",
        "price": 70,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL01pcmFnZVN0cmlrZVBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/f7a05689d9/MirageStrikePlus.png",
    },
    {
        "name": "Awakened Chain Support",
        "price": 120,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0NoYWluUGx1cyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/b328b4615c/ChainPlus.png",
    },
    {
        "name": "Awakened Fork Support",
        "price": 727.68,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0ZvcmtQbHVzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/664ffa6acd/ForkPlus.png",
    },
    {
        "name": "Awakened Lightning Penetration Support",
        "price": 60,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0xpZ2h0bmluZ1BlbmV0cmF0aW9uUGx1cyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/163f40e5e5/LightningPenetrationPlus.png",
    },
    {
        "name": "Awakened Brutality Support",
        "price": 25,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0JydXRhbGl0eVBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/9553670260/BrutalityPlus.png",
    },
    {
        "name": "Awakened Vicious Projectiles Support",
        "price": 15,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL1JhbmdlZFBoeXNpY2FsQXR0YWNrRGFtYWdlUGx1cyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/982ca84dbe/RangedPhysicalAttackDamagePlus.png",
    },
    {
        "name": "Awakened Cast On Critical Strike Support",
        "price": 120,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0Nhc3RPbkNyaXRQbHVzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/928b624b08/CastOnCritPlus.png",
    },
    {
        "name": "Progenesis",
        "price": 2198.2,
        "droprate": 0.11,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzksMTQseyJmIjoiMkRJdGVtcy9GbGFza3MvVWJlck1hdmVuRmxhc2siLCJ3IjoxLCJoIjoyLCJzY2FsZSI6MSwibGV2ZWwiOjEsImZpIjp0cnVlfV0/1883213ee8/UberMavenFlask.png",
    },
    {
        "name": "Awakened Controlled Destruction Support",
        "price": 15,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0NvbnRyb2xsZWREZXN0cnVjdGlvblBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/e545c985d0/ControlledDestructionPlus.png",
    },
    {
        "name": "Awakened Added Chaos Damage Support",
        "price": 15,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0FkZGVkQ2hhb3NEYW1hZ2VQbHVzIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/61d2d11bfb/AddedChaosDamagePlus.png",
    },
    {
        "name": "Awakened Melee Physical Damage Support",
        "price": 40,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0luY3JlYXNlZFBoeXNjaWFsRGFtYWdlUGx1cyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/b5d08a6777/IncreasedPhyscialDamagePlus.png",
    },
    {
        "name": "Viridi's Veil",
        "price": 20,
        "droprate": 0.55,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQXJtb3Vycy9IZWxtZXRzL0NvbnN0cmljdGluZ0Nyb3duIiwidyI6MiwiaCI6Miwic2NhbGUiOjF9XQ/04ee655ca5/ConstrictingCrown.png",
    },
    {
        "name": "Awakened Cold Penetration Support",
        "price": 10,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0NvbGRQZW5ldHJhdGlvblBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/52ac74cbd4/ColdPenetrationPlus.png",
    },
    {
        "name": "Awakened Added Fire Damage Support",
        "price": 10,
        "droprate": 0.00735,
        "reliable": true,
        "trade_link": null,
        "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvR2Vtcy9TdXBwb3J0L1N1cHBvcnRQbHVzL0FkZGVkRmlyZURhbWFnZVBsdXMiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/c1135da118/AddedFireDamagePlus.png",
    },
]

items = [(item["droprate"], item["price"]) for item in ITEMS]

# expected_profit, profit_chance = cpp_stats(items, ENTRANCE_FEE, NUM_KILLS)
# print(f"Statistical probability of making a profit: {profit_chance:.2%}")

# for _ in range(10):
#     simulated_profit, simulated_chance = cpp_sim(items, ENTRANCE_FEE, NUM_KILLS, NUM_SIMULATIONS)
#     print(f"Simulated probability of making a profit: {simulated_chance:.2%}")


def inspect_distribution():
    SIMULATIONS = 100000
    values = [simulate_kills(items, NUM_KILLS) for _ in range(SIMULATIONS)]

    plt.hist(values, bins="auto", alpha=0.7, rwidth=0.85)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title(f"{SIMULATIONS} simulations of {NUM_KILLS} kills")
    plt.grid(axis="y", alpha=0.75)
    plt.show()


# inspect_distribution()


def compare_probabilities():
    statistical_profit_probabilities = []
    simulated_profit_probabilities = []
    ticks = []
    for num_kills in range(10, 501, 10):
        ticks.append(num_kills)
        _, profit_chance = cpp_stats(items, ENTRANCE_FEE, num_kills)
        statistical_profit_probabilities.append(profit_chance)

        _, simulated_chance = cpp_sim(items, ENTRANCE_FEE, num_kills, NUM_SIMULATIONS)
        simulated_profit_probabilities.append(simulated_chance)
    plot_profit_probabilities(
        statistical_profit_probabilities, simulated_profit_probabilities, ticks
    )


def plot_profit_probabilities(
    statistical_profit_probabilities, simulated_profit_probabilities, ticks
):

    plt.plot(
        ticks,
        statistical_profit_probabilities,
        label="Statistical Profit Probabilities",
    )
    plt.plot(ticks, simulated_profit_probabilities, label="Simulated Profit Probabilities")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Line Plot of Profit Probabilities")
    plt.legend()
    plt.grid()
    plt.show()


compare_probabilities()
