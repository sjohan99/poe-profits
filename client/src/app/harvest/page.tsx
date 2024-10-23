import { fetchData } from "@services/fetcher";
import type { Overview } from "./types";
import { RerollDataTable } from "./datatable";

export default async function Page() {
  const overview = await fetchData<Overview>("harvest/overview");

  return (
    <>
      <div className="flex max-w-3xl flex-col gap-2 pb-2">
        <p>
          The tables below show what the expected profit from rerolling a single
          item (1x stack), including the cost of lifeforce.
        </p>
        <p className="font-bold italic">
          Tip: click on a table to open its full view
        </p>
      </div>
      <div>
        <RerollDataTable
          rerollData={overview.orbs}
          itemType="Delirium Orb"
          detailsHref="harvest/delirium_orbs"
          isOverview={true}
        ></RerollDataTable>
        <div className="my-5"></div>
        <RerollDataTable
          rerollData={overview.catalysts}
          itemType="Catalyst"
          detailsHref="harvest/catalysts"
          isOverview={true}
        ></RerollDataTable>
      </div>
    </>
  );
}
