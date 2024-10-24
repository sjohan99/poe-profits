import { fetchData } from "@services/fetcher";
import ProfitInfo from "../profit-info";
import type { RerollData } from "../types";
import { RerollDataTable } from "../datatable";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Harvest: Delirium Orbs",
  description:
    "Expected profit from rerolling currency items using Horticrafting",
};

export default async function Page() {
  const rerollData = await fetchData<RerollData>("harvest/orbs");

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
