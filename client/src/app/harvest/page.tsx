import { fetchData } from "@services/fetcher";
import { type TableProps, OverviewTable } from "./table";

type Overview = {
  orbs: TableProps;
  catalysts: TableProps;
};

export default async function Page() {
  const data = await fetchData<Overview>("harvest/overview");

  return (
    <>
      <div>
        <OverviewTable
          tableProps={data.orbs}
          title="Delirium Orbs"
          link="harvest/delirium_orbs"
        ></OverviewTable>
        <div className="my-5 rounded-full border-2 border-accent-1"></div>
        <OverviewTable
          tableProps={data.catalysts}
          title="Catalysts"
          link="harvest/catalysts"
        ></OverviewTable>
      </div>
    </>
  );
}
