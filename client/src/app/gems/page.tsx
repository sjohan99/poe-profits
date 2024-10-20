import { type Gem } from "./types";
import { fetchData } from "@services/fetcher";
import GemTable from "./gem-datatable";

export default async function Page() {
  const gemData = await fetchData<Gem[]>("gems/summary");

  return (
    <>
      <GemTable gemData={gemData}></GemTable>
    </>
  );
}
