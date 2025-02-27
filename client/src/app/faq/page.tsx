import { type ReactNode } from "react";
import BlueLink from "@components/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "FAQ",
};

function Question({
  question,
  children,
}: {
  question: string;
  children: ReactNode;
}) {
  /**
   * Creates an id from the question.
   *
   * Example:
   * `"How are boss profits calculated?"` -> `"how-are-boss-profits-calculated"`
   * @returns {string} - The id of the question
   */
  function createId() {
    const q = question.replace(/[^a-zA-Z ]/g, "");
    return q.toLowerCase().replace(/ /g, "-");
  }

  return (
    <div className="flex flex-col gap-2" id={createId()}>
      <h2>{question}</h2>
      {children}
    </div>
  );
}

function PoeNinjaLink() {
  return (
    <a
      href="https://poe.ninja"
      target="_blank"
      rel="noreferrer noopener"
      className="truncate text-link hover:underline"
      title="poe.ninja"
    >
      poe.ninja
    </a>
  );
}

export default function Page() {
  return (
    <main className="flex max-w-3xl flex-col gap-10">
      <Question question="How are boss profits calculated?">
        <p>
          The &quot;value&quot; of a boss is the average profit per kill. It is
          calculated as follows:
        </p>
        <p>Item Value = Price * Droprate</p>
        <p>Boss Value = Sum of all Item Values - Entry Cost</p>
      </Question>
      <Question question="Where do the drop rates come from?">
        <p>
          I use the drop rates listed on the{" "}
          <BlueLink href="https://www.poewiki.net/" text="wiki"></BlueLink>.
          These might not be 100% accurate but they are the best I could find.
          If you think they are wrong, feel free to open an issue on{" "}
          <BlueLink
            href="https://github.com/sjohan99/poe-profits/issues"
            text="Github"
          ></BlueLink>
          !
        </p>
      </Question>
      <Question question="How are gem profits calculated?">
        <span>
          The &quot;Level profit&quot; is the price-difference between the game
          at level 1 and its max (uncorrupted) level.
          <p>
            &quot;Level + Corrupt&quot; is the expected profit from levelling a
            gem from level 1 and corrupting a gem from.
          </p>
          <p>
            &quot;Level + Quality + Corrupt&quot; is the expected profit from
            levelling a gem from level 1, making it 20% quality, and then
            corrupting it.
          </p>
        </span>
      </Question>
      <Question question='What is "Experience Adjusted Profits?"'>
        <p>
          This makes the profit normalized with respect to the required
          experience to level a gem to max level. Awakened and exceptional gems
          are generally more profitable to level at a per gem basis. However
          they also require around 5x more experience to reach max level
          compared to a normal / transfigured gem.
        </p>
      </Question>
      <Question question='Why are some bosses and items marked with "unreliable prices?"'>
        <p>
          All prices for this project are pulled from <PoeNinjaLink />. Some
          items are not priced correctly due to them not being priced as
          unidentified (i.e. Sublime Vision) and/or where there are multiple
          versions of the same item (i.e. Watcher&apos;s eye).
        </p>
        <p>
          This can lead to wildly inaccurate prices. As of writing Sublime
          Vision is priced as 130c when it is actually 14000c. To combat this
          I&apos;ve marked all such items as unreliable and added a trade-link
          to the item and possibility to (locally) update the price of the items
          by editing the price in the price column.
        </p>
      </Question>
      <Question question="X item has the wrong price!">
        <p>
          Currently all item prices are fetched from pulled form{" "}
          <PoeNinjaLink /> so if those prices are wrong then the prices on this
          site will be as well.
        </p>
        <p>
          With the addition of Faustus (Currency Exchange) some item prices will
          generally be slightly off since items traded on the Currency Exchange
          is not publicly available.
        </p>
      </Question>
    </main>
  );
}
