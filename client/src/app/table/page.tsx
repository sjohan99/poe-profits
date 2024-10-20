"use client";

import React from "react";
import ChaosOrb from "~/components/currency";

function HeaderComponent() {
  return <p>Header Component</p>;
}

type Column<T> = {
  header: React.ReactNode;
  accessor: keyof T;
  key: React.Key;
  sortable?: boolean;
};

type ExampleT = {
  name: string | React.ReactNode;
  age: number;
  email: string;
};

const exampleData: ExampleT[] = [
  { name: "John Doe", age: 28, email: "john@example.com" },
  { name: "Jane Smith", age: 34, email: "jane@example.com" },
  {
    name: "Mike Johnsonaaaaaa",
    age: 45,
    email: "mike@example.com",
  },
  { name: "John Doe", age: 28, email: "john@example.com" },
  { name: "John Doe", age: 24, email: "john@example.com" },
  { name: "John Doe", age: 84, email: "john@example.com" },
  { name: "John Doe", age: 8, email: "john@example.com" },
];

export default function Page() {
  const columns: Column<ExampleT>[] = [
    { header: <HeaderComponent />, accessor: "name", key: "name" },
    {
      header: <HeaderComponent />,
      accessor: "age",
      key: "age",
      sortable: true,
    },
    {
      header: <HeaderComponent />,
      accessor: "email",
      key: "email",
      sortable: true,
    },
  ];

  return <Table columns={columns} rows={exampleData} />;
}

type Row<T> = { [K in keyof T]: React.ReactNode };

type TableProps<T> = {
  columns: Column<T>[];
  rows: Row<T>[];
  initialSort?: Sorting<T>;
};

type Direction = "asc" | "desc";

type Sorting<T> = {
  column: Column<T>;
  direction: "asc" | "desc";
};

function Table<T>(props: TableProps<T>) {
  const { columns, rows, initialSort } = props;

  const [data, setData] = React.useState(rows);
  const [sort, setSort] = React.useState<Sorting<T> | null>(
    initialSort ?? null,
  );

  function changeSort(column: Column<T>) {
    console.log("changeSort", column);

    if (!sort) {
      setSort({ column, direction: "asc" });
      return;
    }
    if (sort.column === column) {
      setSort({
        column,
        direction: sort.direction === "asc" ? "desc" : "asc",
      });
      return;
    }
    setSort({ column, direction: "asc" });
  }

  function Indicator({ column }: { column: Column<T> }) {
    if (!sort) {
      return <SortingIndicator />;
    }
    if (sort.column === column) {
      return <SortingIndicator direction={sort.direction} />;
    }
    return <SortingIndicator />;
  }

  React.useEffect(() => {
    if (sort) {
      const sorting = sort.column.accessor;
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
    <div className="max-w-full overflow-x-auto">
      <table className="min-w-full bg-primary">
        <thead className="">
          <tr>
            {columns.map((column) =>
              column.sortable ? (
                <th
                  key={column.key}
                  className="border-b border-accent-2 px-4 py-2 text-left"
                >
                  <div
                    className="inline-flex cursor-pointer items-center gap-2 text-nowrap text-left"
                    onClick={() => changeSort(column)}
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
          {data.map((row, rowIndex) => (
            <tr key={rowIndex} className="odd:bg-accent-3">
              {columns.map((column) => (
                <td key={column.key} className="text-nowrap px-4 py-2">
                  <p className="inline-flex min-w-max items-center gap-2">
                    {row[column.accessor]} <ChaosOrb />
                  </p>
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
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
      height="64"
      viewBox="-96 0 512 512"
      xmlns="http://www.w3.org/2000/svg"
      className="h-4 w-4 fill-secondary-1"
    >
      {direction === "asc" ? asc : direction === "desc" ? desc : none}
    </svg>
  );
}
