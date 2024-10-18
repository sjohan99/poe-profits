"use client";

import { usePathname } from "next/navigation";
import { CenterContent } from "./center-content";

const routeTitles: Record<string, string> = {
  "/": "Summary",
  "/boss": "Bossing",
  "/gems": "Gem Levelling",
  "/faq": "Frequency Asked Questions",
  "/about": "About",
  "/harvest": "Harvest Rerolling",
  "/harvest/delirium_orbs": "Delirium Orbs",
};

/**
 * Finds the most specific title for a given path by trying all subpaths, starting from the most specific.
 *
 * Example:
 * `"/boss/the_maven"` will try to find a title for `"/boss/the_maven"` and then `"/boss"`.
 *
 * @param path the path of the page
 * @returns The most specific title of the page, if there is one
 */
function findTitle(path: string): string {
  const pathParts = path.split("/");
  for (let i = pathParts.length; i >= 0; i--) {
    const subPath = pathParts.slice(0, i).join("/");
    if (routeTitles[subPath]) {
      return routeTitles[subPath];
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
