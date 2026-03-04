"use client";

import { type Column, Row, Table } from "~/components/datatable";
import { ItemImage } from "~/components/images";
import ChaosOrb from "~/components/currency";
import Tooltip from "~/components/tooltip";
import { type Gem } from "./types";
import { useMemo, useState } from "react";
import { CheckBox } from "~/components/checkbox";

type Filters = {
  showAwakened: boolean;
  showTransfigured: boolean;
};

function filterGems(gems: Gem[], filters: Filters): Gem[] {
  const newGems = gems.filter((gem) => {
    if (!filters.showAwakened && gem.gem_type === "awakened") {
      return false;
    }
    if (!filters.showTransfigured && gem.gem_type === "transfigured") {
      return false;
    }
    return true;
  });
  return [...newGems];
}

function maybeChaosOrb(
  gem: Gem,
  xpAdjustment: boolean,
  field: keyof Gem,
  alternativeField: keyof Gem,
) {
  if (xpAdjustment && gem[alternativeField] !== null) {
    return <ChaosOrb />;
  }
  if (gem[field] !== null) return <ChaosOrb />;
}

function filterOnName(search: string, rows: Row<Gem>[]) {
  return rows.filter((row) => {
    return row.name.toLowerCase().includes(search.toLowerCase());
  });
}

export default function GemTable({ gemData }: { gemData: Gem[] }) {
  const [filters, setFilters] = useState<Filters>({
    showAwakened: true,
    showTransfigured: true,
  });
  const [xpAdjustment, setXpAdjustment] = useState(false);

  const gems = useMemo(() => {
    return filterGems(gemData, filters);
  }, [filters, gemData]);

  const columns: Column<Gem>[] = [
    {
      header: "Gem",
      accessor: "name",
      key: "name",
      sortable: true,
      formatter: (gem) => (
        <div className="inline-flex items-center gap-2">
          <ItemImage icon={gem.img} alt={gem.name + " image"}></ItemImage>
          <p>{gem.name}</p>
        </div>
      ),
    },
    {
      header: "Level Profit",
      accessor: xpAdjustment ? "xp_adjusted_level_profit" : "level_profit",
      key: "level_profit",
      sortable: true,
      formatter: xpAdjustment
        ? (gem) => gem.xp_adjusted_level_profit.toFixed(1)
        : (gem) => gem.level_profit.toFixed(1),
      extras: (gem) =>
        maybeChaosOrb(
          gem,
          xpAdjustment,
          "level_profit",
          "xp_adjusted_level_profit",
        ),
    },
    {
      header: "Level + Corrupt",
      accessor: xpAdjustment ? "xp_adjusted_c_profit" : "level_c_profit",
      key: "level_c_profit",
      sortable: true,
      formatter: xpAdjustment
        ? (gem) => gem.xp_adjusted_c_profit?.toFixed() ?? "N/A"
        : (gem) => gem.level_c_profit?.toFixed() ?? "N/A",
      extras: (gem) =>
        maybeChaosOrb(
          gem,
          xpAdjustment,
          "level_c_profit",
          "xp_adjusted_c_profit",
        ),
    },
    {
      header: "Level + Quality + Corrupt",
      accessor: xpAdjustment ? "xp_adjusted_q_c_profit" : "level_q_c_profit",
      key: "level_q_c_profit",
      sortable: true,
      formatter: xpAdjustment
        ? (gem) =>
            gem.xp_adjusted_q_c_profit
              ? gem.xp_adjusted_q_c_profit.toFixed()
              : "N/A"
        : (gem) =>
            gem.level_q_c_profit ? gem.level_q_c_profit.toFixed() : "N/A",
      extras: (gem) =>
        maybeChaosOrb(
          gem,
          xpAdjustment,
          "level_q_c_profit",
          "xp_adjusted_q_c_profit",
        ),
    },
  ];

  return (
    <div className="flex flex-col gap-y-2">
      <p className="text-lg font-bold">Options:</p>
      <div className="flex flex-col items-start gap-y-2">
        <div className="flex flex-row gap-2">
          <CheckBox
            id="useExperienceAdjustedProfits"
            checked={xpAdjustment}
            onChange={() => setXpAdjustment(!xpAdjustment)}
            label="Use Experience Adjusted Profits"
          />
          <Tooltip icon="question">
            <p>Calculates profit accounting for required experience.</p>
          </Tooltip>
        </div>
        <CheckBox
          id="showAwakenedGems"
          checked={filters.showAwakened}
          onChange={() =>
            setFilters({ ...filters, showAwakened: !filters.showAwakened })
          }
          label="Show Awakened Gems"
        />
        <CheckBox
          id="showTransfiguredGems"
          checked={filters.showTransfigured}
          onChange={() =>
            setFilters({
              ...filters,
              showTransfigured: !filters.showTransfigured,
            })
          }
          label="Show Transfigured Gems"
        />
      </div>
      <Table
        key={`${filters.showAwakened} ${filters.showTransfigured}`}
        columns={columns}
        rows={gems}
        pagination={{ rowsPerPage: 15, type: "expand" }}
        search={{ placeholderText: "Search for a gem", searchFn: filterOnName }}
      />
    </div>
  );
}
