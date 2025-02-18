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
            {boss.name}
          </Link>
          {boss.reliable ? null : (
            <Tooltip icon="info">
              <p>Boss contains items with unreliable prices</p>
            </Tooltip>
          )}
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
