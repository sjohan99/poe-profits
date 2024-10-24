import { type Gem } from "./types";
import { fetchData } from "@services/fetcher";
import GemTable from "./gem-datatable";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Gem Levelling",
  description: "Expected profit from levelling and corrupting gems",
};

export default async function Page() {
  const gemData = await fetchData<Gem[]>("gems/summary");

  return (
    <>
      <GemTable gemData={gemData}></GemTable>
    </>
  );
}
