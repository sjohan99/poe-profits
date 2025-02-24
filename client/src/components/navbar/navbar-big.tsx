import { type NextFont } from "next/dist/compiled/@next/font";
import { type NavLinkProps } from "./types";
import Link from "next/link";

export default function TopNavBig({
  logoFont,
  links,
  title,
}: {
  logoFont: NextFont;
  links: NavLinkProps[];
  title: string;
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
            <Link
              key={link.text}
              href={link.href}
              prefetch={true}
              className="hover:text-secondary-2"
            >
              {link.text}
            </Link>
          ))}
        </div>
      </nav>
      <div className="flex-none -lg:min-w-0"></div>
    </div>
  );
}
