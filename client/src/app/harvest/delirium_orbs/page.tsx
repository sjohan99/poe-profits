import { fetchData } from "@services/fetcher";
import ProfitInfo from "../profit-info";
import type { RerollData } from "../types";
import { RerollDataTable } from "../datatable";

export default async function Page() {
  const rerollData = await fetchData<RerollData>("harvest/catalysts");

  return (
    <>
      <ProfitInfo></ProfitInfo>
      <RerollDataTable
        rerollData={rerollData}
        itemType="Delirium Orb"
        isOverview={false}
      ></RerollDataTable>
    </>
  );
}
