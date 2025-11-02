import { fetchData } from "@services/fetcher";
import { type Boss } from "./types";
import SummaryDataTable from "./summary-datatable";
import type { Metadata } from "next";
import LeagueSelector from "../league-selector";
import { env } from "~/env";

export const dynamic = "force-static";
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
      <DroprateWarning league={params.league} />
      <SummaryDataTable bosses={bosses} league={params.league} />
    </>
  );
}

function DroprateWarning({ league }: { league: string }) {
  if (!league.toLowerCase().includes("keepers")) return null;
  return (
    <div>
      <h2 className="text-orange-500">
        New league warning: Drop rates may have changed and item prices are
        volatile.
      </h2>
      <h2 className="text-orange-300">
        Known issues: Incarnation bosses have not been updated for the new
        Keepers league yet.
      </h2>
    </div>
  );
}
