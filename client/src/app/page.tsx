import Image from "next/image";
import Link from "next/link";
import { fetchData } from "~/services/fetcher";

export default async function HomePage() {
  const leagues = await fetchData<string[]>("metadata/leagues");
  let league = "Standard";
  if (leagues.length > 0) {
    league = leagues[0]!;
  }

  return (
    <main>
      <div className="flex flex-col items-center gap-2 text-center">
        <h1>Welcome to poe-profits!</h1>
        <h3>
          Find profitability statistics regarding bossing, levelling gems, and
          rerolling items using horticrafting.
        </h3>

        <p>
          Navigate the site using the navigation in the top right corner or
          click one of the examples below!
        </p>

        <span className="p-2"></span>

        <Link href={`/${league}/boss`} className="hover:underline">
          <h2>BOSSING</h2>
          <Image
            src="/landing/bossing.png"
            alt="Example"
            width={1280}
            height={966}
            className="w-full lg:max-w-screen-md"
          />
        </Link>

        <Link href={`/${league}/gems`} className="hover:underline">
          <h2>GEM LEVELLING</h2>
          <Image
            src="/landing/gems.png"
            alt="Example"
            width={1605}
            height={743}
            className="w-full lg:max-w-screen-md"
          />
        </Link>
      </div>
    </main>
  );
}
