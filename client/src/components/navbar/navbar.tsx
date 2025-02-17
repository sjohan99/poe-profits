import { type NextFont } from "next/dist/compiled/@next/font";
import { type NavLinkProps } from "./types";
import TopNavBig from "./navbar-big";
import TopNavSmall from "./navbar-small";
import { fetchData } from "~/services/fetcher";

const title = "poe-profits";

export default async function Topnav({ logoFont }: { logoFont: NextFont }) {
  const leagues = await fetchData<string[]>("metadata/leagues");
  let league = "Standard";
  if (leagues.length > 0) {
    league = leagues[0]!;
  }

  const navLinks: NavLinkProps[] = [
    { href: `/${league}/boss`, text: "Bosses" },
    { href: `/${league}/gems`, text: "Gems" },
    { href: `/${league}/harvest`, text: "Harvest" },
    { href: "/faq", text: "FAQ" },
  ];

  return (
    <div>
      <TopNavBig logoFont={logoFont} links={navLinks} title={title} />
      <TopNavSmall logoFont={logoFont} links={navLinks} title={title} />
    </div>
  );
}
