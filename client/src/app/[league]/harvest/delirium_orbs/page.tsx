import { fetchData } from "@services/fetcher";
import ProfitInfo from "../profit-info";
import type { RerollData } from "../types";
import { RerollDataTable } from "../datatable";
import type { Metadata } from "next";
import LeagueSelector from "../../league-selector";
import { env } from "~/env";

export const revalidate = env.ISR_REVALIDATE_SECONDS;

export const metadata: Metadata = {
  title: "Harvest: Delirium Orbs",
  description:
    "Expected profit from rerolling currency items using Horticrafting",
};

export default async function Page({ params }: { params: { league: string } }) {
  const rerollData = await fetchData<RerollData>("harvest/orbs", params.league);

  return (
    <>
      <LeagueSelector
        league={params.league}
        route="harvest/delirium_orbs"
      ></LeagueSelector>
      <ProfitInfo></ProfitInfo>
      <RerollDataTable
        rerollData={rerollData}
        itemType="Delirium Orb"
        isOverview={false}
      ></RerollDataTable>
    </>
  );
}
