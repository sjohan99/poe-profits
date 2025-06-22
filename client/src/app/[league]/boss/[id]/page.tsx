import { fetchData } from "@services/fetcher";
import { type DetailedBossInfo } from "../types";
import BossDataTable from "../boss-datatable";
import type { Metadata } from "next";
import LeagueSelector from "../../league-selector";

export async function generateMetadata({
  params,
}: {
  params: { id: string; league: string };
}): Promise<Metadata> {
  const bossInfo = await fetchData<DetailedBossInfo[]>(
    "bosses/all",
    params.league,
  );
  const boss = bossInfo.find((b) => b.id === params.id);

  return {
    title: `${boss ? boss.name : "boss not found"}`,
    description: boss ? `Expected profit from ${boss.name}` : undefined,
  };
}

function DroprateWarning({
  league,
  boss,
}: {
  league: string;
  boss: DetailedBossInfo;
}) {
  if (!league.toLowerCase().includes("mercenaries")) return null;
  if (
    !["exarch", "maven"].some((name) => boss.name.toLowerCase().includes(name))
  ) {
    return null;
  }
  return (
    <h2 className="text-orange-500">
      <span className="text-orange-300">{boss.name}</span> drop rates have
      changed in 3.26. Their drop rates are being estimated and may be
      inaccurate.
    </h2>
  );
}

export default async function Page({
  params,
}: {
  params: { id: string; league: string };
}) {
  const bossInfo = await fetchData<DetailedBossInfo[]>(
    "bosses/all",
    params.league,
  );
  const boss = bossInfo.find((b) => b.id === params.id);

  return (
    <>
      {boss ? (
        <>
          <DroprateWarning league={params.league} boss={boss} />
          <LeagueSelector
            league={params.league}
            route={`boss/${params.id}`}
          ></LeagueSelector>
          <h1 className="mb-2 text-3xl font-bold">{boss.name}</h1>
          <BossDataTable boss={boss}></BossDataTable>
        </>
      ) : (
        <h1>Not found</h1>
      )}
    </>
  );
}
