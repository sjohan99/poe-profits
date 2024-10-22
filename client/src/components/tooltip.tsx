"use client";

import { useEffect, useRef, type ReactNode } from "react";

export type TooltipProps = {
  children: ReactNode;
  icon: "info" | "question";
};

export default function Tooltip({ children, icon }: TooltipProps): JSX.Element {
  const tooltipRef = useRef<HTMLDivElement>(null);
  const tooltipTriggerRef = useRef<HTMLDivElement>(null);

  /**
   * Moves the tooltip left or right of the triggering box, depending on available space.
   * If there is not enough space on either side, the tooltip will be centered
   * and the text wrapped.
   */
  const handleMouseEnter = () => {
    if (tooltipRef.current && tooltipTriggerRef.current) {
      const tooltip = tooltipRef.current;
      const trigger = tooltipTriggerRef.current;
      const { innerWidth: viewportWidth } = window;
      const tooltipRect = tooltip.getBoundingClientRect();
      const triggerRect = trigger.getBoundingClientRect();

      let left = triggerRect.x + triggerRect.width + 4;

      if (
        left + tooltipRect.width > viewportWidth &&
        triggerRect.x - tooltipRect.width - 4 < 0
      ) {
        tooltip.style.left = "10%";
        tooltip.style.width = "80%";
        tooltip.style.textWrap = "wrap";
        return;
      }

      if (left + tooltipRect.width > viewportWidth) {
        left = triggerRect.x - tooltipRect.width - 4;
      }

      tooltip.style.left = `${left}px`;

      // Center the tooltip vertically
      const heightDifference = (tooltipRect.height - triggerRect.height) / 2;
      tooltip.style.top = `${triggerRect.y - heightDifference}px`;
    }
  };

  /**
   * Removes any style changes made by handleMouseEnter when the mouse leaves the tooltip.
   */
  const handleMouseLeave = () => {
    if (tooltipRef.current) {
      tooltipRef.current.style.width = "";
      tooltipRef.current.style.textWrap = "";
    }
  };

  useEffect(() => {
    if (tooltipTriggerRef.current) {
      tooltipTriggerRef.current.addEventListener(
        "mouseenter",
        handleMouseEnter,
      );
      tooltipTriggerRef.current.addEventListener(
        "mouseleave",
        handleMouseLeave,
      );
    }
  }, []);

  return (
    <div className="has-tooltip flex items-center">
      <div ref={tooltipTriggerRef}>
        {icon === "info" ? <InfoSvg /> : <QuestionSvg />}
      </div>
      <div
        ref={tooltipRef}
        // pointer-events-none otherwise the tooltip might block the mouse events
        className="tooltip pointer-events-none fixed flex flex-row gap-2 rounded bg-accent-1 p-1 font-normal shadow-lg"
      >
        {children}
      </div>
    </div>
  );
}

function InfoSvg() {
  return (
    <svg
      width="24px"
      height="24px"
      viewBox="0 0 24 24"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <circle
        cx="12"
        cy="12"
        r="10"
        className="stroke-warn"
        strokeWidth="1.5"
      />
      <path
        d="M12 17V11"
        strokeWidth="1.5"
        strokeLinecap="round"
        className="stroke-warn"
      />
      <circle
        cx="1"
        cy="1"
        r="0.5"
        transform="matrix(1 0 0 -1 11 9)"
        className="stroke-warn"
      />
    </svg>
  );
}

function QuestionSvg() {
  return (
    <svg
      width="24px"
      height="24px"
      viewBox="0 0 24 24"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <circle
        className="stroke-link"
        cx="12"
        cy="12"
        r="10"
        strokeWidth="1.5"
      />
      <path
        d="M10.125 8.875C10.125 7.83947 10.9645 7 12 7C13.0355 7 13.875 7.83947 13.875 8.875C13.875 9.56245 13.505 10.1635 12.9534 10.4899C12.478 10.7711 12 11.1977 12 11.75V13"
        stroke="#1C274C"
        strokeWidth="1.5"
        strokeLinecap="round"
        className="stroke-link"
      />
      <circle cx="12" cy="16" r="0.5" className="stroke-link" />
    </svg>
  );
}

export function QuestionTooltip({ children }: TooltipProps): JSX.Element {
  return (
    <div className="has-tooltip flex items-center">
      <div className="tooltip ml-7 flex flex-row gap-2 text-wrap rounded bg-accent-1 p-1 text-base font-normal shadow-lg">
        {children}
      </div>
      <svg
        width="24px"
        height="24px"
        viewBox="0 0 24 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <circle
          className="stroke-link"
          cx="12"
          cy="12"
          r="10"
          strokeWidth="1.5"
        />
        <path
          d="M10.125 8.875C10.125 7.83947 10.9645 7 12 7C13.0355 7 13.875 7.83947 13.875 8.875C13.875 9.56245 13.505 10.1635 12.9534 10.4899C12.478 10.7711 12 11.1977 12 11.75V13"
          stroke="#1C274C"
          strokeWidth="1.5"
          strokeLinecap="round"
          className="stroke-link"
        />
        <circle cx="12" cy="16" r="0.5" className="stroke-link" />
      </svg>
    </div>
  );
}
