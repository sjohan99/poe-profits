import { fetchData } from "@services/fetcher";
import { type Boss } from "./types";
import SummaryDataTable from "./summary-datatable";
import type { Metadata } from "next";
import LeagueSelector from "../league-selector";

export const metadata: Metadata = {
  title: "Bossing",
  description: "Expected profit from pinnacle bosses",
};

export default async function Page({ params }: { params: { league: string } }) {
  const bosses = await fetchData<Boss[]>("bosses/summary", params.league);

  return (
    <>
      {params.league.toLowerCase().includes("mercenaries") && (
        <h2 className="text-orange-500">
          <span className="text-orange-300">Searing Exarch</span> and{" "}
          <span className="text-orange-300">Maven</span> drop rates have changed
          in 3.26. Their drop rates are being estimated and may be inaccurate.
        </h2>
      )}
      <LeagueSelector league={params.league} route="boss"></LeagueSelector>
      <SummaryDataTable bosses={bosses} league={params.league} />
    </>
  );
}
