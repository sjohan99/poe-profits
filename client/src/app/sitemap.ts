import type { MetadataRoute } from "next";
import { env } from "@env";
import { fetchData } from "~/services/fetcher";

const URL = env.SITE_URL;

type BossId = {
  id: string;
};

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const bossInfo = await fetchData<BossId[]>("bosses/summary");

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
      url: `${URL}/about`,
    },
    {
      url: `${URL}/gems`,
    },
    {
      url: `${URL}/harvest`,
    },
    {
      url: `${URL}/harvest/delirium_orbs`,
    },
    {
      url: `${URL}/harvest/catalysts`,
    },
    {
      url: `${URL}/manifest.webmanifest`,
    },
    {
      url: `${URL}/sitemap.xml`,
    },
    {
      url: `${URL}/boss`,
    },
    ...bossInfo.map((boss) => ({
      url: `${URL}/boss/${boss.id}`,
    })),
  ];
}
