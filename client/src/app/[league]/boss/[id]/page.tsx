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
