import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "poe-profits",
    short_name: "poe-profits",
    description:
      "poe-profits helps you understand the profitability of various Path of Exile mechanics",
    start_url: "/",
    background_color: "#012533",
    icons: [
      {
        src: "/favicon.ico",
        sizes: "any",
        type: "image/x-icon",
      },
    ],
  };
}
