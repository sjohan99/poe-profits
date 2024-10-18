import ChaosOrb from "@components/currency";
import { type Item, type Lifeforce } from "./types";
import { QuestionTooltip } from "@components/tooltip";
import React from "react";
import {
  Table,
  TableHeaders,
  TableHeader,
  TableRow,
  TableRows,
} from "@components/table";
import { ItemImage } from "@components/images";

import Link from "next/link";

export type TableProps = {
  items: Item[];
  lifeforce: Lifeforce[];
  total_weight: number;
};

function percentage(value: number, total: number): string {
  return `${((100 * value) / total).toFixed(2)}%`;
}

function expectedProfit(value: number) {
  const color = value > 0 ? "text-green" : "text-red";
  return <p className={color}>{value.toFixed(2)}</p>;
}

export async function FullTable(props: TableProps) {
  const { items, total_weight } = props;

  function itemRow(data: Item) {
    return (
      <TableRow key={data.name} column_sizes={[2, 1, 1, 1]}>
        <div className="flex flex-row items-center gap-2">
          <ItemImage icon={data.icon} alt={data.name} />
          <p className="truncate" title={data.name}>
            {data.name}
          </p>
        </div>
        <div>{expectedProfit(data.expected_reroll_profit)}</div>
        <div>{data.chaos_value.toFixed(2)}</div>
        <div>{percentage(data.reroll_weight, total_weight)}</div>
      </TableRow>
    );
  }

  return (
    <>
      <Table>
        <TableHeaders column_sizes={[2, 1, 1, 1]}>
          <TableHeader>Item</TableHeader>
          <TableHeader>
            Expected Profit <ChaosOrb />
          </TableHeader>
          <TableHeader>
            Price <ChaosOrb />
          </TableHeader>
          <TableHeader>
            Reroll Chance{" "}
            <QuestionTooltip>Data from {total_weight} rerolls</QuestionTooltip>
          </TableHeader>
        </TableHeaders>
        <TableRows column_sizes={[2, 1, 1, 1]}>
          {items.map((item) => itemRow(item))}
        </TableRows>
      </Table>
    </>
  );
}

type OverviewTableProps = {
  tableProps: TableProps;
  title: string;
  link: string;
};

export function OverviewTable(props: OverviewTableProps) {
  const { tableProps, title, link } = props;
  const { items, total_weight } = tableProps;
  const firstThreeItems = items.slice(0, 3);
  const lastThreeItems = items.slice(-3);
  const columns = [2, 1, 1, 1];

  function itemRow(data: Item) {
    return (
      <TableRow key={data.name} column_sizes={columns}>
        <div className="flex flex-row items-center gap-2 truncate">
          <ItemImage icon={data.icon} alt={data.name} />
          <p className="truncate" title={data.name}>
            {data.name}
          </p>
        </div>
        <div>{expectedProfit(data.expected_reroll_profit)}</div>
        <div>{data.chaos_value.toFixed(2)}</div>
        <div>{percentage(data.reroll_weight, total_weight)}</div>
      </TableRow>
    );
  }

  if (items.length <= 6) {
    return FullTable(tableProps);
  }

  return (
    <div className="group rounded hover:bg-accent-3">
      <Link href={link} className="">
        <h2 className="max-w-fit pb-2 text-2xl font-bold group-hover:underline">
          {title}
        </h2>
        <Table>
          <TableHeaders column_sizes={columns}>
            <TableHeader>
              <p className="truncate">Item</p>
            </TableHeader>
            <TableHeader>
              <p className="truncate -sm:hidden">Expected Profit</p>{" "}
              <p className="truncate sm:hidden">Profit</p>{" "}
              <ChaosOrb className="-sm:hidden" />
            </TableHeader>
            <TableHeader>
              <p className="truncate">Price</p>{" "}
              <ChaosOrb className="-sm:hidden" />
            </TableHeader>
            <TableHeader>
              <p className="truncate">Reroll Chance</p>
              <div className="-sm:hidden">
                <QuestionTooltip>
                  Data from {total_weight} rerolls
                </QuestionTooltip>
              </div>
            </TableHeader>
          </TableHeaders>
          <TableRows column_sizes={columns}>
            {firstThreeItems.map((item) => itemRow(item))}
            <TableRow column_sizes={[5]}>
              <div className="flex w-full flex-col items-center gap-1">
                <div className="h-1 w-1 rounded-full bg-accent-2"></div>
                <div className="h-1 w-1 rounded-full bg-accent-2"></div>
                <div className="h-1 w-1 rounded-full bg-accent-2"></div>
              </div>
            </TableRow>
            {lastThreeItems.map((item) => itemRow(item))}
          </TableRows>
        </Table>
      </Link>
    </div>
  );
}
