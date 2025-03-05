"use client";

import React, { useMemo } from "react";
import { useDebounce } from "react-use";
import TextInput from "./text-input";

export type Column<T> = {
  header: React.ReactNode;
  accessor: keyof T;
  key: React.Key;
  sortable?: boolean;
  editHandler?: (
    event: React.ChangeEvent<HTMLInputElement>,
    index: number,
    data: Row<T>[],
  ) => Row<T>[];
  extras?: (value: T) => React.ReactNode;
  formatter?: (value: T) => React.ReactNode;
};

export type Row<T> = T & { [K in keyof T]: React.ReactNode };

export type TableProps<T> = {
  columns: Column<T>[];
  rows: Row<T>[];
  footer?: (rows: Row<T>[]) => { [K in keyof T]: React.ReactNode };
  initialSort?: Sorting<T>;
  pagination?: Pagination;
  search?: Search<T>;
};

export type Search<T> = {
  placeholderText: string;
  searchFn: (search: string, rows: Row<T>[]) => Row<T>[];
};

export type Pagination = {
  type: "expand" | "replace";
  rowsPerPage: number;
};

export type Direction = "asc" | "desc";

export type Sorting<T> = {
  column: keyof T;
  direction: "asc" | "desc";
};

export function Table<T>(props: TableProps<T>) {
  const { columns, rows, footer, initialSort, pagination, search } = props;

  const pageSize = pagination?.rowsPerPage ?? rows.length;
  const [data, setData] = React.useState(rows);
  const [sort, setSort] = React.useState<Sorting<T> | null>(
    initialSort ?? null,
  );
  const [page, setPage] = React.useState(1);

  function changeSort(column: keyof T) {
    if (!sort) {
      setSort({ column, direction: "desc" });
      return;
    }
    if (sort.column === column) {
      setSort({
        column,
        direction: sort.direction === "asc" ? "desc" : "asc",
      });
      return;
    }
    setSort({ column, direction: "desc" });
  }

  function Indicator({ column }: { column: Column<T> }) {
    if (!sort) {
      return <SortingIndicator />;
    }
    if (sort.column === column.accessor) {
      return <SortingIndicator direction={sort.direction} />;
    }
    return <SortingIndicator />;
  }

  useMemo(() => {
    if (sort) {
      const sorting = sort.column;
      const direction = sort.direction === "asc" ? 1 : -1;
      setData((prev) => {
        return prev.slice().sort((a, b) => {
          const x = a[sorting];
          const y = b[sorting];

          // Sort nulls to the end
          if (!x) return -1 * direction;
          if (!y) return 1 * direction;

          if (x < y) {
            return -1 * direction;
          }
          if (x > y) {
            return 1 * direction;
          }
          return 0;
        });
      });
    }
  }, [sort]);

  return (
    <div className="flex flex-col gap-2">
      {search ? (
        <TextInput
          placeholderText={search.placeholderText}
          inputCallback={(searchInput) => {
            setData(search.searchFn(searchInput, rows));
          }}
          debounceMs={333}
        />
      ) : null}
      <div className="max-w-full overflow-x-auto rounded outline outline-1 outline-accent-1">
        <table className="responsive-text-s min-w-full bg-primary">
          <thead className="responsive-text-m">
            <tr>
              {columns.map((column) =>
                column.sortable ? (
                  <th
                    key={column.key}
                    className="border-b border-accent-2 px-4 py-2 text-left"
                  >
                    <div
                      className="inline-flex cursor-pointer items-center gap-2 text-nowrap text-left"
                      onClick={() => changeSort(column.accessor)}
                    >
                      {column.header}
                      <Indicator column={column} />
                    </div>
                  </th>
                ) : (
                  <th
                    key={column.key}
                    className="border-b border-accent-2 px-4 py-2 text-left"
                  >
                    {column.header}
                  </th>
                ),
              )}
            </tr>
          </thead>
          <tbody>
            {data.slice(0, page * pageSize).map((row, rowIndex) => (
              <tr key={rowIndex} className="odd:bg-accent-3">
                {columns.map((column) => (
                  <td key={column.key} className="h-12 text-nowrap px-4">
                    {column.editHandler ? (
                      <input
                        title=""
                        type="text"
                        pattern=""
                        value={String(row[column.accessor])}
                        className="h-4/5 rounded border border-accent-2 border-opacity-20 bg-transparent pl-1"
                        onChange={(event) => {
                          const newData = column.editHandler!(
                            event,
                            rowIndex,
                            data,
                          );
                          setData(newData);
                        }}
                      />
                    ) : (
                      <div className="inline-flex h-full min-w-max items-center gap-2">
                        {column.formatter
                          ? column.formatter(row)
                          : row[column.accessor]}{" "}
                        {column.extras ? column.extras(row) : null}
                      </div>
                    )}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
          {footer ? (
            <>
              <tfoot>
                <tr>
                  {columns.map((column) => (
                    <td
                      key={column.key}
                      className="my-2 text-nowrap border-t border-accent-2 px-4 py-2 text-left"
                    >
                      {footer(data)[column.accessor]}
                    </td>
                  ))}
                </tr>
              </tfoot>
            </>
          ) : null}
        </table>
        {pagination ? (
          <p className="px-4 py-2 text-secondary-2">
            Showing {Math.min(pageSize * page, data.length)} of {data.length}{" "}
            rows
          </p>
        ) : null}
      </div>
      {pagination && pageSize * page < data.length ? (
        <button
          className="mt-2 h-10 w-full rounded border border-secondary-1 hover:border-2 hover:border-secondary-2"
          onClick={() => setPage((prev) => prev + 1)}
        >
          Show more
        </button>
      ) : null}
    </div>
  );
}

function SortingIndicator({ direction }: { direction?: Direction | null }) {
  const asc = (
    <path d="M279 224H41c-21.4 0-32.1-25.9-17-41L143 64c9.4-9.4 24.6-9.4 33.9 0l119 119c15.2 15.1 4.5 41-16.9 41z" />
  );
  const desc = (
    <path d="M41 288h238c21.4 0 32.1 25.9 17 41L177 448c-9.4 9.4-24.6 9.4-33.9 0L24 329c-15.1-15.1-4.4-41 17-41z" />
  );
  const none = (
    <path d="M41 288h238c21.4 0 32.1 25.9 17 41L177 448c-9.4 9.4-24.6 9.4-33.9 0L24 329c-15.1-15.1-4.4-41 17-41zm255-105L177 64c-9.4-9.4-24.6-9.4-33.9 0L24 183c-15.1 15.1-4.4 41 17 41h238c21.4 0 32.1-25.9 17-41z" />
  );

  return (
    <svg
      width="64px"
      height="64px"
      viewBox="-96 0 512 512"
      xmlns="http://www.w3.org/2000/svg"
      className="h-4 w-4 fill-secondary-1"
    >
      {direction === "asc" ? asc : direction === "desc" ? desc : none}
    </svg>
  );
}
