"use client";

import { type Column, Table } from "~/components/datatable";
import type { Item, RerollData } from "./types";
import { ItemImage } from "~/components/images";
import Link from "next/link";
import ChaosOrb from "~/components/currency";
import Tooltip from "~/components/tooltip";

function firstAndLastItems(items: Item[], n: number) {
  const firstThreeItems = items.slice(0, n);
  const lastThreeItems = items.slice(-n);
  return [...firstThreeItems, ...lastThreeItems];
}

export function RerollDataTable({
  rerollData,
  itemType,
  detailsHref,
  isOverview,
}: {
  rerollData: RerollData;
  itemType: "Delirium Orb" | "Catalyst";
  detailsHref?: string;
  isOverview: boolean;
}) {
  const rows = isOverview
    ? firstAndLastItems(rerollData.items, 3)
    : rerollData.items;

  const columns: Column<Item>[] = [
    {
      header: itemType,
      accessor: "name",
      key: "name",
      sortable: !isOverview,
      formatter: (item) => (
        <div className="inline-flex items-center gap-2">
          <ItemImage icon={item.icon} alt={item.name + " image"}></ItemImage>
          <p>{item.name}</p>
        </div>
      ),
    },
    {
      header: "Expected Profit",
      accessor: "expected_reroll_profit",
      key: "expected_reroll_profit",
      sortable: !isOverview,
      formatter: (item) => item.expected_reroll_profit.toFixed(2),
      extras: () => <ChaosOrb />,
    },
    {
      header: "Price",
      accessor: "chaos_value",
      key: "chaos_value",
      sortable: !isOverview,
      formatter: (item) => item.chaos_value.toFixed(2),
      extras: () => <ChaosOrb />,
    },
    {
      header: (
        <div className="inline-flex items-center gap-2">
          <p>Reroll Chance</p>
          <Tooltip icon="question">
            <p>Data from {rerollData.total_weight} rerolls</p>
          </Tooltip>
        </div>
      ),
      accessor: "reroll_weight",
      key: "reroll_weight",
      sortable: !isOverview,
      formatter: (item) =>
        ((100 * item.reroll_weight) / rerollData.total_weight).toFixed(2) + "%",
    },
  ];

  return (
    <div>
      {detailsHref ? (
        <Link href={detailsHref} className="cursor-pointer">
          <Table columns={columns} rows={rows} />
        </Link>
      ) : (
        <Table columns={columns} rows={rows} />
      )}
    </div>
  );
}
