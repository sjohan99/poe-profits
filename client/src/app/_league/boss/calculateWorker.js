/**
 * @param {import("./types").Item[]} items
 * @param {number} kills
 */
function simulateKills(items, kills) {
  let totalValue = 0;
  for (let i = 0; i < kills; i++) {
    for (const item of items) {
      if (
        item.type === "drop" &&
        item.droprate != null &&
        Math.random() <= item.droprate
      ) {
        totalValue += item.price;
      }
    }
  }
  return totalValue;
}

/**
 * @param {import("./types").Item[]} items
 * @param {number} kills
 * @param {number} simulations
 * @returns {number}
 */
function calculateLikelihoodToProfit(items, kills, simulations) {
  let profitableSimulations = 0;
  const entrance_cost = items
    .filter((item) => item.type === "entrance")
    .reduce((acc, item) => acc + item.price * (item.quantity ?? 0), 0);
  const entrance_cost_for_all_kills = entrance_cost * kills;
  for (let i = 0; i < simulations; i++) {
    const value = simulateKills(items, kills);
    const profit = value - entrance_cost_for_all_kills;
    if (profit > 0) {
      profitableSimulations++;
    }
    /** @type {import("./types").InProgressMessage} */
    const progressMessage = {
      type: "in-progress",
      simulationsDone: i + 1,
      simulationsTotal: simulations,
    };
    self.postMessage(progressMessage);
  }

  const profitProbability = profitableSimulations / simulations;
  return profitProbability;
}
/**
 * @param {MessageEvent<import("./types").BeginMessage>} e
 */
self.onmessage = function (e) {
  const { items, kills, simulations } = e.data;
  const result = calculateLikelihoodToProfit(items, kills, simulations);
  /** @type {import("./types").DoneMessage} */
  const doneMessage = { type: "done", probability: result };
  self.postMessage(doneMessage);
};
