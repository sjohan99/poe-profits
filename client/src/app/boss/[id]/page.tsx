import { fetchData } from "@services/fetcher";
import { type DetailedBossInfo } from "../types";
import BossDataTable from "../boss-datatable";

export default async function Page({ params }: { params: { id: string } }) {
  const bossInfo = await fetchData<DetailedBossInfo[]>("bosses/all");
  const boss = bossInfo.find((b) => b.id === params.id);

  return (
    <>
      {boss ? (
        <>
          {" "}
          <>
            <h1 className="mb-2 text-3xl font-bold">{boss.name}</h1>
            <BossDataTable boss={boss}></BossDataTable>
          </>
        </>
      ) : (
        <h1>Not found</h1>
      )}
    </>
  );
}
