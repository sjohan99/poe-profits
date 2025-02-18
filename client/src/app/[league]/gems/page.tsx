import { type Gem } from "./types";
import { fetchData } from "@services/fetcher";
import GemTable from "./gem-datatable";
import type { Metadata } from "next";
import LeagueSelector from "../league-selector";

export const metadata: Metadata = {
  title: "Gem Levelling",
  description: "Expected profit from levelling and corrupting gems",
};

export default async function Page({ params }: { params: { league: string } }) {
  const gemData = await fetchData<Gem[]>("gems/summary", params.league);

  return (
    <>
      <LeagueSelector league={params.league} route="gems"></LeagueSelector>
      <GemTable gemData={gemData}></GemTable>
    </>
  );
}
