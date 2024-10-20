"use client";

import { type NextFont } from "next/dist/compiled/@next/font";
import Link from "next/link";
import { useState } from "react";
import { CenterContent } from "~/components/center-content";

type NavLinkProps = {
  href: string;
  text: string;
};

const navLinks: NavLinkProps[] = [
  { href: "/boss", text: "Bosses" },
  { href: "/gems", text: "Gems" },
  { href: "/harvest", text: "Harvest" },
  { href: "/faq", text: "FAQ" },
];

const title = "poe-profits";

export default function Topnav({ logoFont }: { logoFont: NextFont }) {
  return (
    <div>
      <TopNavBig logoFont={logoFont} links={navLinks} />
      <TopNavSmall logoFont={logoFont} links={navLinks} />
    </div>
  );
}

function TopNavBig({
  logoFont,
  links,
}: {
  logoFont: NextFont;
  links: NavLinkProps[];
}) {
  return (
    <div className="flex h-20 w-full justify-center border-b-2 border-secondary-1 bg-accent-1 -2xl:px-3 -lg:hidden">
      <div className="flex-none -lg:min-w-0"></div>
      <nav className="flex max-w-screen-2xl grow items-center justify-between text-2xl font-semibold">
        <Link
          href="/"
          className={
            logoFont.className + " text-3xl font-bold italic text-white"
          }
        >
          {title}
        </Link>

        <div className="flex gap-x-10 -lg:hidden">
          {links.map((link) => (
            <Link key={link.text} href={link.href}>
              {link.text}
            </Link>
          ))}
        </div>
      </nav>
      <div className="flex-none -lg:min-w-0"></div>
    </div>
  );
}

function TopNavSmall({
  logoFont,
  links,
}: {
  logoFont: NextFont;
  links: NavLinkProps[];
}) {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  function Cross() {
    return (
      <svg
        width="32px"
        height="32px"
        viewBox="0 0 24 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        onClick={() => setIsMenuOpen(!isMenuOpen)}
        className="cursor-pointer"
      >
        <path
          d="M19 5L5 19M5.00001 5L19 19"
          stroke="#000000"
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
          className="stroke-secondary-1"
        />
      </svg>
    );
  }

  function Burger() {
    return (
      <svg
        width="32px"
        height="32px"
        viewBox="0 0 24 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        onClick={() => setIsMenuOpen(!isMenuOpen)}
        className="cursor-pointer"
      >
        <path
          d="M4 18L20 18"
          stroke="#000000"
          strokeWidth="2"
          strokeLinecap="round"
          className="stroke-secondary-1"
        />
        <path
          d="M4 12L20 12"
          stroke="#000000"
          strokeWidth="2"
          strokeLinecap="round"
          className="stroke-secondary-1"
        />
        <path
          d="M4 6L20 6"
          stroke="#000000"
          strokeWidth="2"
          strokeLinecap="round"
          className="stroke-secondary-1"
        />
      </svg>
    );
  }

  function Menu() {
    if (!isMenuOpen) return null;

    return (
      <div>
        <div className="flex flex-col items-center justify-end gap-4 pt-3 text-xl font-semibold">
          {links.map((link) => (
            <Link key={link.text} href={link.href}>
              {link.text}
            </Link>
          ))}
        </div>
        <CenterContent childrenContainerClassName="pb-0">
          <div className="border-t border-accent-1"></div>
        </CenterContent>
      </div>
    );
  }

  return (
    <div className="lg:hidden">
      <div className="grid min-h-20 w-full grid-cols-6 border-b-2 border-secondary-1 bg-accent-1 -2xl:px-3">
        <div className="col-span-5 flex max-w-screen-2xl grow items-center justify-between text-2xl font-semibold">
          <Link
            href="/"
            className={
              logoFont.className + " text-3xl font-bold italic text-white"
            }
          >
            {title}
          </Link>
        </div>
        <div className="flex items-center justify-end">
          {isMenuOpen ? <Cross /> : <Burger />}
        </div>
      </div>
      <Menu />
    </div>
  );
}
