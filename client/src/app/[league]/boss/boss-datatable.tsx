"use client";

import { type Column, type Row, Table } from "~/components/datatable";
import type { DetailedBossInfo, Item } from "./types";
import { ItemImage } from "~/components/images";
import ChaosOrb from "~/components/currency";
import Tooltip from "~/components/tooltip";
import { type ChangeEvent, useMemo, useState } from "react";
import TextInput from "~/components/text-input";
import CalculateProbability from "./calculate-probability";

function bossInfoToRows(bossInfo: DetailedBossInfo): Item[] {
  const rows: Item[] = [];
  for (const drop of bossInfo.drops) {
    rows.push({
      ...drop,
      price: Math.round(drop.price),
      value: Math.round(drop.price) * (drop.droprate ?? 0),
      type: "drop",
    });
  }
  for (const item of bossInfo.entrance_items) {
    rows.push({
      name: item.name,
      price: Math.round(item.price),
      droprate: null,
      value: Math.round(-item.price) * item.quantity,
      reliable: true,
      trade_link: null,
      img: item.img,
      type: "entrance",
      quantity: item.quantity,
    });
  }
  return rows;
}

function createItemName(item: Item): string {
  return item.quantity && item.quantity > 1
    ? `${item.name} x${item.quantity}`
    : item.name;
}

export default function BossDataTable({ boss }: { boss: DetailedBossInfo }) {
  const rows = bossInfoToRows(boss);

  const [visibleRows, setVisibleRows] = useState(rows);
  const [cutoff, setCutoff] = useState(0);

  const profit = useMemo(() => {
    let profit = 0;
    let revenue = 0;
    for (const row of visibleRows) {
      if (row.type === "drop") {
        revenue += row.value;
      }
      profit += row.value;
    }
    for (const row of visibleRows) {
      if (row.type === "drop") row.share = row.value / revenue;
    }

    return profit;
  }, [visibleRows]);

  function omitBelow(amount: string) {
    if (amount === "") {
      setVisibleRows(rows);
      setCutoff(0);
    } else {
      const cutoff = parseInt(amount);
      const itemsAboveCutoff = rows.filter(
        (row) => row.type === "entrance" || row.price > cutoff,
      );
      setVisibleRows([...itemsAboveCutoff]);
      setCutoff(cutoff);
    }
  }

  function changePrice(
    event: ChangeEvent<HTMLInputElement>,
    index: number,
    data: Row<Item>[],
  ): Row<Item>[] {
    const v = event.target.value;
    const customPrice = v === "" ? 0 : parseInt(v);
    if (isNaN(customPrice)) {
      return data;
    }
    const row = data[index];
    if (row === undefined) {
      return data;
    }
    row.type === "entrance"
      ? (row.value = -customPrice * (row.quantity ?? 1))
      : (row.value = customPrice * (row.droprate ?? 0));

    row.price = customPrice;

    setVisibleRows(data);
    return [...data];
  }

  function total() {
    return {
      name: <p className="font-bold">Total</p>,
      price: "",
      droprate: "",
      value: (
        <div className="inline-flex items-center gap-2 font-bold">
          <p>{Math.round(profit)}</p>
          <ChaosOrb />
        </div>
      ),
      reliable: "",
      trade_link: "",
      img: "",
      type: "",
      quantity: "",
    };
  }

  const columns: Column<Item>[] = [
    {
      header: "Item",
      accessor: "name",
      key: "name",
      sortable: true,
      formatter: (item) => (
        <div className="inline-flex items-center gap-2">
          <ItemImage icon={item.img} alt={item.name + " image"}></ItemImage>
          {!item.reliable && item.trade_link ? (
            <>
              <a
                href={item.trade_link}
                target="_blank"
                rel="noreferrer noopener"
                className="truncate text-link hover:underline"
                title={item.name}
              >
                {createItemName(item)}
              </a>
              <Tooltip icon="info">
                <p>Item price is unreliable</p>
              </Tooltip>
            </>
          ) : (
            <p>{createItemName(item)}</p>
          )}
        </div>
      ),
    },
    {
      header: (
        <div className="inline-flex items-center gap-2">
          <p>Price</p>
          <ChaosOrb />
        </div>
      ),
      accessor: "price",
      key: "price",
      sortable: true,
      editHandler: changePrice,
    },
    {
      header: "Drop rate",
      accessor: "droprate",
      key: "droprate",
      sortable: true,
      formatter: (item) =>
        item.droprate ? (item.droprate * 100).toFixed(2) + "%" : "N/A",
    },
    {
      header: "Value",
      accessor: "value",
      key: "value",
      sortable: true,
      formatter: (item) => <p>{item.value.toFixed(2)}</p>,
      extras: () => <ChaosOrb />,
    },
    {
      header: "Profit Share",
      accessor: "share",
      key: "share",
      sortable: true,
      formatter: (item) =>
        item.share ? (item.share * 100).toFixed(2) + "%" : "N/A",
    },
  ];

  return (
    <div className="flex flex-col gap-2">
      <CalculateProbability items={visibleRows} />
      <div className="flex flex-col gap-2">
        <h3>Filters:</h3>
        <div className="flex flex-row items-center gap-2">
          <p className="flex min-w-max">Omit items below</p>
          <div className="max-w-14">
            <TextInput
              textPosition="center"
              inputCallback={omitBelow}
              debounceMs={500}
              restriction={"number"}
            ></TextInput>
          </div>
          <ChaosOrb />
        </div>
      </div>
      <Table
        key={cutoff}
        columns={columns}
        rows={visibleRows}
        initialSort={{ column: "value", direction: "desc" }}
        footer={total}
      />
    </div>
  );
}
