import { fetchData } from "@services/fetcher";
import { type Boss } from "./types";
import SummaryDataTable from "./summary-datatable";
import type { Metadata } from "next";
import LeagueSelector from "../league-selector";
import { env } from "~/env";

export const revalidate = env.ISR_REVALIDATE_SECONDS;

export const metadata: Metadata = {
  title: "Bossing",
  description: "Expected profit from pinnacle bosses",
};

export default async function Page({ params }: { params: { league: string } }) {
  const bosses = await fetchData<Boss[]>("bosses/summary", params.league);

  return (
    <>
      <LeagueSelector league={params.league} route="boss"></LeagueSelector>
      <SummaryDataTable bosses={bosses} league={params.league} />
    </>
  );
}
