export default async function ProfitInfo() {
  return (
    <div className="flex max-w-3xl flex-col gap-2 pb-2">
      <p>
        This table shows the expected profit from rerolling a single item, with
        the cost of lifeforce is included in the calculation.
      </p>
      <p>
        Theoretically, any item with a positive expected profit will be
        profitable to reroll.
      </p>
      <p className="font-bold italic">
        Note that bulk and Faustus prices might differ, which can affect the
        profitability of rerolling.
      </p>
    </div>
  );
}
