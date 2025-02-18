import Link from "next/link";
import { fetchData } from "~/services/fetcher";

export default async function LeagueSelector(params: {
  league: string;
  route: string;
}) {
  const availableLeagues = await fetchData<string[]>("metadata/leagues");

  return (
    <div className="mb-2 flex flex-col gap-y-1 text-center sm:flex-row sm:gap-x-2">
      {availableLeagues.map((availableLeague) => (
        <Link
          key={availableLeague}
          href={`/${availableLeague}/${params.route}`}
          className={
            params.league === availableLeague
              ? "rounded border border-secondary-2 bg-accent-1 p-1 font-bold"
              : "rounded bg-accent-1 p-1"
          }
        >
          {availableLeague}
        </Link>
      ))}
    </div>
  );
}
