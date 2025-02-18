import "~/styles/globals.css";
import { Chakra_Petch, Quicksand } from "next/font/google";
import { Analytics } from "@vercel/analytics/react";
import { SpeedInsights } from "@vercel/speed-insights/next";
import { CenterContent } from "~/components/center-content";
import PageTitle from "@components/page-title";
import Footer from "./footer";
import TopNav from "@components/navbar/navbar";
import { env } from "~/env";

const quicksand = Quicksand({
  weight: "400",
  subsets: ["latin"],
  display: "swap",
});

const chakraPetch = Chakra_Petch({
  weight: "400",
  subsets: ["latin"],
  display: "swap",
});

export const metadata = {
  title: {
    template: "poe-profits | %s",
    default: "poe-profits",
  },
  description:
    "poe-profits helps you understand the profitability of various Path of Exile mechanics",
  icons: [{ rel: "favicon", url: "/favicon.ico" }],
  metadataBase: new URL(env.SITE_URL),
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${quicksand.className}`}>
      <body className="flex min-h-screen flex-col justify-between">
        <div className="min-h-screen">
          <TopNav logoFont={chakraPetch} />
          <PageTitle />
          <CenterContent background="bg-primary">{children}</CenterContent>
        </div>
        <div>
          <CenterContent skipPadX={true}>
            <div className="border-t border-accent-1 pb-3"></div>
            <div className="px-3">
              <Footer></Footer>
            </div>
          </CenterContent>
        </div>
        <Analytics></Analytics>
        <SpeedInsights></SpeedInsights>
      </body>
    </html>
  );
}
