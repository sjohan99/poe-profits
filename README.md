# poe-profits

poe-profits is a Path of Exile tool which helps you calculate and understand the profitability of:

- bossing
- levelling gems
- harvest rerolling

Visit the website [here!](https://poe-profits.com/)

## Issues and feature requests

If you have any issues or feature requests, please [open an issue](https://github.com/sjohan99/poe-profits/issues/new).

## Development

If you want to run the project locally, you can do so by following these steps:

1. Clone the repository
2. Navigate to the [api directory](/api/) and follow the instructions there
3. Navigate to the [client directory](/client/) and follow the instructions there
4. Run the client and api simultaneously

## Contributing

If you want to contribute to the project, you are more than welcome to do so but please open an issue first with your suggestion and we can discuss it further.

### Updating drop rates

If you think the boss item drop rates are incorrect you can either:

- Notify me by [opening an issue](https://github.com/sjohan99/poe-profits/issues/new) and I will update them given that the data seems reliable.
- Make a pull request with your changes. To update the drop rates you need to modify the [bosses.py](api/poe_profit_calc/bossing/bosses.py) file. The drop rates are specified as follows:

```python
BossItem(
    "Item Name", # the name of the item
    "Internal Item ID",
    0.1, # <--- drop rate (0.1 = 10%) UPDATE THIS
    Matcher(PoeNinjaEndpoint.UNIQUE_ARMOUR, "Item Name"),
)
```

## Acknowledgements

Thanks to

- [poe.watch](https://poe.watch/) for providing price data. **Big thanks to [Mxrk](https://github.com/Mxrk) for updating the poe.watch API according to my specific needs!**
- [poe.ninja](https://poe.ninja/) for providing price data
- [poegems.com](https://poegems.com/) for providing a list of all gems
- [poewiki.net](https://www.poewiki.net/) for providing drop rate and gem data
