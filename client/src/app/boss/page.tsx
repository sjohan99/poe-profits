import { fetchData } from "@services/fetcher";
import { type Boss } from "./types";
import SummaryDataTable from "./summary-datatable";

export default async function Page() {
  const bosses = await fetchData<Boss[]>("bosses/summary");

  return (
    <>
      <SummaryDataTable bosses={bosses} />
    </>
  );
}
