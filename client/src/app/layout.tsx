import "~/styles/globals.css";
import { Roboto_Slab, Chakra_Petch } from "next/font/google";
import { Analytics } from "@vercel/analytics/react";
import { SpeedInsights } from "@vercel/speed-insights/next";
import { CenterContent } from "~/components/center-content";
import PageTitle from "@components/page-title";
import Footer from "./footer";
import TopNav from "./navbar";

const robotoSlab = Roboto_Slab({
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
  title: "Path of Exile Profit Calculator",
  icons: [{ rel: "favicon", url: "/favicon.ico" }],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${robotoSlab.className}`}>
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
