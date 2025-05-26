from poe_profit_calc.vendor.parse import Orb, Catalyst
from .orbs import orb_weights, PRIMAL_LIFEFORCE_PER_ORB_REROLL
from .catalysts import catalyst_weights, VIVID_LIFEFORCE_PER_CATALYST_REROLL

RerollableItem = Orb | Catalyst


def calculate_profits(
    items: set[RerollableItem], lifeforce_cost: float, lifeforce_amount: int
) -> dict[RerollableItem, float]:
    """
    Calculates the expected profit for from rerolling each item in `items`

    Parameters:
        items (set[RerollableItem]): All items to be considered in the calculation.
        lifeforce_cost (float): The cost of 1 lifeforce of the given type in chaos orbs.
        lifeforce_amount (int): The amount of lifeforce required to reroll an item.
    Returns:
        A dictionary mapping each item to its expected profit from rerolling (a single item).
    """
    item_profits = {}
    total_item_weight = sum([item.reroll_weight for item in items])
    for item in items:
        other_items = items - {item}
        other_items_weight = total_item_weight - item.reroll_weight
        expected_new_value = sum(
            [
                (item2.reroll_weight / other_items_weight) * item2.chaos_value
                for item2 in other_items
            ]
        )
        cost = item.chaos_value + lifeforce_cost * 30
        item_profits[item] = expected_new_value - cost
    return item_profits
