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
      <div className="flex flex-col gap-2">{children}</div>
    </>
  );
}
