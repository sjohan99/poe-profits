import type { MetadataRoute } from "next";
import { env } from "@env";
import { fetchData } from "~/services/fetcher";

const URL = env.SITE_URL;

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const leauges = await fetchData<string[]>("metadata/leagues");

  return [
    {
      url: URL,
    },
    {
      url: `${URL}/about`,
    },
    {
      url: `${URL}/faq`,
    },
    {
      url: `${URL}/manifest.webmanifest`,
    },
    {
      url: `${URL}/sitemap.xml`,
    },
    ...leauges.flatMap((league) => [
      {
        url: `${URL}/${league}/boss`,
      },
      {
        url: `${URL}/${league}/gems`,
      },
      {
        url: `${URL}/${league}/harvest`,
      },
      {
        url: `${URL}/${league}/harvest/delirium_orbs`,
      },
      {
        url: `${URL}/${league}/harvest/catalysts`,
      },
    ]),
  ];
}
