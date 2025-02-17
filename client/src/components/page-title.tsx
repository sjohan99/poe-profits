"use client";

import { usePathname } from "next/navigation";
import { CenterContent } from "./center-content";

const routeTitles: Record<string, string> = {
  "/": "Welcome",
  "/boss": "Bossing",
  "/gems": "Gem Levelling",
  "/faq": "Frequency Asked Questions",
  "/about": "About",
  "/harvest": "Harvest Rerolling",
  "/harvest/delirium_orbs": "Harvest Rerolling: Delirium Orbs",
  "/harvest/catalysts": "Harvest Rerolling: Catalysts",
  "/table": "Table",
};

function findTitle(path: string): string {
  const keys = Object.keys(routeTitles);
  keys.sort((a, b) => b.length - a.length);
  for (const key of keys) {
    if (path.includes(key)) {
      return routeTitles[key]!;
    }
  }
  return "";
}

export default function PageTitle() {
  const pathName = usePathname();
  const title = findTitle(pathName);

  return (
    <CenterContent>
      <h1 className="text-3xl font-bold">{title}</h1>
    </CenterContent>
  );
}
