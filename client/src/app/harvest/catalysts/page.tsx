import { fetchData } from "@services/fetcher";
import ProfitInfo from "../profit-info";
import type { RerollData } from "../types";
import { RerollDataTable } from "../datatable";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Harvest: Catalysts",
  description: "Expected profit from rerolling Catalysts using Horticrafting",
};

export default async function Page() {
  const rerollData = await fetchData<RerollData>("harvest/catalysts");

  return (
    <>
      <ProfitInfo></ProfitInfo>
      <RerollDataTable
        rerollData={rerollData}
        itemType="Catalyst"
        isOverview={false}
      ></RerollDataTable>
    </>
  );
}
