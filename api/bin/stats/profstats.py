import math
from scipy import stats


def calculate_profit_probability(items, entrance_fee, num_kills=100):
    expected_value = sum(p * v for p, v in items)
    expected_profit_per_kill = expected_value - entrance_fee
    expected_total_profit = expected_profit_per_kill * num_kills

    # Bernoulli trial variance = v^2 * p * (1 - p)
    variance = sum((v**2) * p * (1 - p) for p, v in items) * num_kills
    print((variance / num_kills) ** 0.5)
    std_dev = math.sqrt(variance)

    z_score = -expected_total_profit / std_dev
    profit_probability = 1 - stats.norm.cdf(z_score)

    return expected_total_profit, profit_probability


if __name__ == "__main__":

    true = True
    null = None
    false = False

    i = [
        {
            "name": "Shaper's Touch",
            "price": 5,
            "droprate": 0.56,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQXJtb3Vycy9HbG92ZXMvU2hhcGVyc0dsb3ZlcyIsInciOjIsImgiOjIsInNjYWxlIjoxfV0/633aead741/ShapersGloves.png",
        },
        {
            "name": "Fragment of Knowledge",
            "price": 40,
            "droprate": 0.5,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvTWFwcy9VYmVyRWxkZXIwNCIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/4a2bab8955/UberElder04.png",
        },
        {
            "name": "Dying Sun",
            "price": 1063.86,
            "droprate": 0.01,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzksMTQseyJmIjoiMkRJdGVtcy9GbGFza3MvU2hhcGVyc0ZsYXNrIiwidyI6MSwiaCI6Miwic2NhbGUiOjEsImxldmVsIjoxLCJmaSI6dHJ1ZX1d/62bf1c1b8c/ShapersFlask.png",
        },
        {
            "name": "Solstice Vigil",
            "price": 5,
            "droprate": 0.1,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQW11bGV0cy9TaGFwZXJzUHJlc2VuY2UiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/57d45e4009/ShapersPresence.png",
        },
        {
            "name": "Voidwalker",
            "price": 5,
            "droprate": 0.33,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQXJtb3Vycy9Cb290cy9Dcm9zc2luZ1RoZVZvaWQiLCJ3IjoyLCJoIjoyLCJzY2FsZSI6MX1d/f3747eb0f4/CrossingTheVoid.png",
        },
        {
            "name": "Fragment of Shape",
            "price": 45,
            "droprate": 0.5,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvTWFwcy9VYmVyRWxkZXIwMyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/dd71531c9f/UberElder03.png",
        },
        {
            "name": "Orb of Dominance",
            "price": 652.34,
            "droprate": 0.01,
            "reliable": true,
            "trade_link": null,
            "img": "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvTWF2ZW5PcmIiLCJ3IjoxLCJoIjoxLCJzY2FsZSI6MX1d/8396ed7d8d/MavenOrb.png",
        },
    ]

    items = [(item["droprate"], item["price"]) for item in i]

    entrance_fee = 500

    # for n in range(1, 100):
    #     expected_profit, profit_chance = calculate_profit_probability(items, entrance_fee, n)
    #     print(f"Probability of making a profit after {n} kills: {profit_chance:.2%}")
    num_kills = 100
    expected_profit, profit_chance = calculate_profit_probability(items, entrance_fee, num_kills)

    # print(f"Expected profit after {num_kills} kills: {expected_profit:.2f}")
    # print(f"Expected profit per kill: {expected_profit / num_kills:.2f}")
    print(f"Probability of making a profit: {profit_chance:.2%}")
