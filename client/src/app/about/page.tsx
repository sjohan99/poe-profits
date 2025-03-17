import BlueLink from "~/components/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "About",
};

export default function Page() {
  return (
    <main className="flex max-w-3xl flex-col gap-5">
      <div className="flex flex-col gap-2">
        <h2>Purpose</h2>
        <p>
          This is a hobby project of mine which I hope can be useful to some
          people. There are similar tools but I created this for fun and because
          they were outdated or had disappeared.
        </p>
      </div>
      <div className="flex flex-col gap-2">
        <h2>Acknowledgements</h2>
        <p>This site is made possible by:</p>
        <ul className="list-inside list-disc">
          <li>
            <BlueLink href="https://poe.watch/" text="poe.watch"></BlueLink> for
            providing price data. Big thanks to poe.watch creator Mark for
            specifically updating the API according to my needs!
          </li>
          <li>
            <BlueLink href="https://poe.ninja/" text="poe.ninja"></BlueLink> for
            providing price data
          </li>
          <li>
            <BlueLink href="https://poegems.com/" text="poegems.com"></BlueLink>{" "}
            for providing a list of all gems
          </li>
          <li>
            <BlueLink
              href="https://www.poewiki.net/"
              text="poewiki.net"
            ></BlueLink>{" "}
            for providing drop rate and gem data
          </li>
        </ul>
      </div>
      <div className="flex flex-col gap-2">
        <h2>Contact</h2>
        <p>
          If there are any issues or you have any suggestions, feel free to open
          an issue on{" "}
          <BlueLink
            href="https://github.com/sjohan99/poe-profits/issues"
            text="Github"
          ></BlueLink>
          .
        </p>
      </div>
    </main>
  );
}
