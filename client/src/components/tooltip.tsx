import { type ReactNode } from "react";

type TooltipProps = {
  children: ReactNode;
};

export function Tooltip({ children }: TooltipProps): JSX.Element {
  return (
    <div className="has-tooltip flex items-center">
      <div className="tooltip ml-7 flex flex-row gap-2 text-wrap rounded bg-accent-1 p-1 shadow-lg">
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
    </div>
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
