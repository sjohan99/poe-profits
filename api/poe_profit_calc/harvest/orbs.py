import msgspec
import logging

PRIMAL_LIFEFORCE_PER_ORB_REROLL = 30

orb_weights = {
    "Abyssal Delirium Orb": 35,
    "Armoursmith's Delirium Orb": 736,
    "Blacksmith's Delirium Orb": 698,
    "Blighted Delirium Orb": 50,
    "Cartographer's Delirium Orb": 85,
    "Diviner's Delirium Orb": 161,
    "Fine Delirium Orb": 605,
    "Foreboding Delirium Orb": 99,
    "Fossilised Delirium Orb": 31,
    "Fragmented Delirium Orb": 53,
    "Jeweller's Delirium Orb": 765,
    "Obscured Delirium Orb": 26,
    "Singular Delirium Orb": 74,
    "Skittering Delirium Orb": 24,
    "Thaumaturge's Delirium Orb": 47,
    "Timeless Delirium Orb": 41,
    "Whispering Delirium Orb": 93,
}
