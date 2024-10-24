import { fetchData } from "@services/fetcher";
import { type Boss } from "./types";
import SummaryDataTable from "./summary-datatable";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Bossing",
  description: "Expected profit from pinnacle bosses",
};

export default async function Page() {
  const bosses = await fetchData<Boss[]>("bosses/summary");

  return (
    <>
      <SummaryDataTable bosses={bosses} />
    </>
  );
}
