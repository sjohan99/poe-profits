"use client";

import { type Column, Table } from "~/components/datatable";
import { type Boss } from "./types";
import { ItemImage } from "~/components/images";
import Link from "next/link";
import ChaosOrb from "~/components/currency";
import Tooltip from "~/components/tooltip";

export default function SummaryDataTable({
  bosses,
  league,
}: {
  bosses: Boss[];
  league: string;
}) {
  const columns: Column<Boss>[] = [
    {
      header: "Boss",
      accessor: "name",
      key: "name",
      sortable: true,
      formatter: (boss) => (
        <div className="inline-flex items-center gap-2">
          <ItemImage icon={boss.img} alt={boss.name + " image"}></ItemImage>
          <Link href={`/${league}/boss/${boss.id}`} className="hover:underline">
            <p className="-sm:hidden">{boss.name}</p>
            <p className="sm:hidden">{boss.short_name}</p>
          </Link>
          <div className={boss.n_items_not_found === 0 ? "hidden" : ""}>
            <Tooltip icon="info">
              <p>{boss.n_items_not_found} items missing price data</p>
            </Tooltip>
          </div>
        </div>
      ),
    },
    {
      header: "Profit per kill",
      accessor: "value",
      key: "value",
      sortable: true,
      formatter: (boss) => boss.value.toFixed(2),
      extras: () => <ChaosOrb />,
    },
  ];

  return <Table columns={columns} rows={bosses} />;
}
