import { type ReactNode } from "react";
import { fetchData } from "~/services/fetcher";
import NotFound from "../not-found";

export default async function Layout({
  params,
  children,
}: {
  params: { league: string };
  children: ReactNode;
}) {
  const leagues = await fetchData<string[]>("metadata/leagues");
  if (!leagues.includes(decodeURIComponent(params.league))) {
    return <NotFound />;
  }

  return (
    <>
      <div className="flex flex-col gap-2">
        {params.league.toLowerCase().includes("mercenaries") && (
          <h2 className="text-orange-500">
            Early league! Prices may not yet be available or highly volatile.
          </h2>
        )}
        {children}
      </div>
    </>
  );
}
