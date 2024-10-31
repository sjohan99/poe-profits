import random
from collections import Counter


def simulate_kills(items, num_kills):
    total_value = 0
    for _ in range(num_kills):
        for probability, value in items:
            if random.random() < probability:
                total_value += value
    return total_value


def calculate_profit_probability(items, entrance_fee, num_kills=10, num_simulations=1000000):
    results = Counter()
    total_profit = 0

    for _ in range(num_simulations):
        total_value = simulate_kills(items, num_kills)
        profit = total_value - (entrance_fee * num_kills)
        results[profit > 0] += 1
        total_profit += profit

    profit_probability = results[True] / num_simulations
    expected_profit = total_profit / num_simulations

    return expected_profit, profit_probability


if __name__ == "__main__":

    true = True
    null = None
    false = False

    i = [
        {
            "name": "Eldritch Orb of Annulment",
            "price": 55,
            "droprate": 0.05,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvRWxkcml0Y2hBbm51bG1lbnRPcmIiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/cd03411d81/EldritchAnnulmentOrb.png",
        },
        {
            "name": "Archive Reliquary Key",
            "price": 354,
            "droprate": 0.015,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvTWFwcy9TZWFyaW5nRXhhcmNoRm9pbCIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/bb895c1f5d/SearingExarchFoil.png",
        },
        {
            "name": "Annihilation's Approach",
            "price": 100,
            "droprate": 0.25,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQXJtb3Vycy9Cb290cy9VYmVyU2VhcmluZ0V4YXJjaEJvb3QiLCJ3IjoyLCJoIjoyLCJzY2FsZSI6MX1d/705e9f657f/UberSearingExarchBoot.png",
        },
        {
            "name": "The Annihilating Light",
            "price": 10.3,
            "droprate": 0.475,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvV2VhcG9ucy9Ud29IYW5kV2VhcG9ucy9TdGF2ZXMvSW50cmVwaWR1c0RvbG9yZW0iLCJ3IjoyLCJoIjo0LCJzY2FsZSI6MSwicmVsaWMiOjd9XQ/1faee27d95/IntrepidusDolorem.png",
        },
        {
            "name": "Crystallised Omniscience",
            "price": 149.94,
            "droprate": 0.025,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQW11bGV0cy9Bc2NlbmRhbmNlQW11bGV0IiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/60368620d5/AscendanceAmulet.png",
        },
        {
            "name": "Exceptional Eldritch Ember",
            "price": 150,
            "droprate": 0.15,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvQ2xlYW5zaW5nRmlyZU9yYlJhbms0IiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/920113641f/CleansingFireOrbRank4.png",
        },
        {
            "name": "Forbidden Flame",
            "price": 4500,
            "droprate": 0.05,
            "reliable": false,
            "trade_link": "https://www.pathofexile.com/trade/search/Settlers?q=%7B%22query%22%3A%20%7B%22status%22%3A%20%7B%22option%22%3A%20%22online%22%7D%2C%20%22name%22%3A%20%22Forbidden%20Flame%22%2C%20%22type%22%3A%20%22Crimson%20Jewel%22%2C%20%22stats%22%3A%20%5B%7B%22type%22%3A%20%22and%22%2C%20%22filters%22%3A%20%5B%5D%7D%5D%2C%20%22filters%22%3A%20%7B%22misc_filters%22%3A%20%7B%22filters%22%3A%20%7B%22identified%22%3A%20%7B%22option%22%3A%20%22false%22%7D%2C%20%22ilvl%22%3A%20%7B%22min%22%3A%2087%7D%7D%7D%7D%7D%2C%20%22sort%22%3A%20%7B%22price%22%3A%20%22asc%22%7D%7D",
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvSmV3ZWxzL1B1enpsZVBpZWNlSmV3ZWxfQ2xlYW5zaW5nRmlyZSIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/ddfe57ac90/PuzzlePieceJewel_CleansingFire.png",
        },
        {
            "name": "Eldritch Exalted Orb",
            "price": 9,
            "droprate": 0.05,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvRWxkcml0Y2hFeGFsdGVkT3JiIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/56026bffa3/EldritchExaltedOrb.png",
        },
        {
            "name": "The Celestial Brace",
            "price": 30,
            "droprate": 0.25,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQXJtb3Vycy9HbG92ZXMvVWJlclNlYXJpbmdFeGFyY2hHbG92ZXMiLCJ3IjoyLCJoIjoyLCJzY2FsZSI6MX1d/47d365fea7/UberSearingExarchGloves.png",
        },
        {
            "name": "Eldritch Chaos Orb",
            "price": 59.79,
            "droprate": 0.05,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvRWxkcml0Y2hDaGFvc09yYiIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/afdc1d40be/EldritchChaosOrb.png",
        },
        {
            "name": "Curio of Absorption",
            "price": 778.19,
            "droprate": 0.05,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQW11bGV0cy9QaW5uYWNsZUZyYWdtZW50RXhhcmNoIiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/0da90fe2d1/PinnacleFragmentExarch.png",
        },
    ]

    items = [(item["droprate"], item["price"]) for item in i]

    entrance_fee = 225
    num_kills = 250
    num_simulations = 10000  # Adjust this for more accuracy or faster runtime

    expected_profit, profit_chance = calculate_profit_probability(
        items, entrance_fee, num_kills, num_simulations
    )

    print(f"Number of kills: {num_kills}")
    print(f"Number of simulations: {num_simulations}")
    print(f"Expected profit: {expected_profit:.2f}")
    print(f"Probability of making a profit: {profit_chance:.2%}")

    # Optional: Run multiple times to see consistency
    print("\nRunning multiple times to check consistency:")
    for _ in range(5):
        expected_profit, profit_chance = calculate_profit_probability(
            items, entrance_fee, num_kills, num_simulations
        )
        print(f"Expected profit: {expected_profit:.2f}, Profit chance: {profit_chance:.2%}")
