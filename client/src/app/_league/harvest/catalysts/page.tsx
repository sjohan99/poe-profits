import { fetchData } from "@services/fetcher";
import ProfitInfo from "../profit-info";
import type { RerollData } from "../types";
import { RerollDataTable } from "../datatable";
import type { Metadata } from "next";
import LeagueSelector from "../../league-selector";
import { env } from "~/env";

export const dynamic = "force-static";
export const revalidate = env.ISR_REVALIDATE_SECONDS;

export const metadata: Metadata = {
  title: "Harvest: Catalysts",
  description: "Expected profit from rerolling Catalysts using Horticrafting",
};

export default async function Page({ params }: { params: { league: string } }) {
  const rerollData = await fetchData<RerollData>(
    "harvest/catalysts",
    params.league,
  );

  return (
    <>
      <LeagueSelector
        league={params.league}
        route="harvest/catalysts"
      ></LeagueSelector>
      <ProfitInfo></ProfitInfo>
      <RerollDataTable
        rerollData={rerollData}
        itemType="Catalyst"
        isOverview={false}
      ></RerollDataTable>
    </>
  );
}
