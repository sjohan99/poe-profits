import Link from "next/link";
import { fetchData } from "~/services/fetcher";

export default async function LeagueSelector(params: {
  league: string;
  route: string;
}) {
  const availableLeagues = await fetchData<string[]>("metadata/leagues");
  const league = decodeURIComponent(params.league);

  return (
    <div className="mb-2 flex flex-col gap-y-1 text-center sm:flex-row sm:gap-x-2">
      {availableLeagues.map((availableLeague) => (
        <Link
          key={availableLeague}
          href={`/${availableLeague}/${params.route}`}
          className={
            league === availableLeague
              ? "pointer-events-none rounded border border-secondary-2 bg-accent-1 p-1 font-bold hover:cursor-default"
              : "-m-0 rounded border-secondary-1 bg-accent-1 p-1 hover:-m-px hover:border hover:bg-accent-3"
          }
        >
          {availableLeague}
        </Link>
      ))}
    </div>
  );
}
