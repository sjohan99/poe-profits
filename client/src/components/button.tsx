import React from "react";

export type ButtonProps = {
  children: React.ReactNode;
  onClick: () => void;
  disabled: boolean;
};

export default function Button(props: ButtonProps) {
  const { children, onClick, disabled } = props;

  return (
    <button
      className={
        disabled
          ? "w-full min-w-min text-nowrap rounded bg-gray-700 p-2 opacity-75"
          : "w-full min-w-min text-nowrap rounded bg-accent-1 p-2 hover:-m-px hover:border hover:border-secondary-2 hover:bg-accent-3 hover:p-2"
      }
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
}

export type ProgressButtonProps = ButtonProps & {
  progress: number;
};

export function ProgressButton(props: ProgressButtonProps) {
  const { children, onClick, disabled, progress } = props;

  return (
    <div>
      <button
        className={
          disabled
            ? "relative w-full min-w-min overflow-hidden text-nowrap rounded bg-gray-700 p-2"
            : "relative w-full min-w-min overflow-hidden text-nowrap rounded bg-accent-1 p-2 hover:-m-px hover:border hover:border-secondary-2 hover:bg-accent-3 hover:p-2"
        }
        onClick={onClick}
        disabled={disabled}
      >
        <div
          className="absolute left-0 top-0 h-full bg-green"
          style={{ width: `${progress * 100}%` }}
        ></div>
        <span className="relative z-10">{children}</span>
      </button>
    </div>
  );
}
