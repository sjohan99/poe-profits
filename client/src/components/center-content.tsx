export type CenterContentProps = {
  children: React.ReactNode;
  background?: string;
  className?: string;
  childrenContainerClassName?: string;
  skipPadX?: boolean;
  skipPadY?: boolean;
};

export function CenterContent({
  children,
  background,
  className,
  childrenContainerClassName,
  skipPadX,
  skipPadY,
}: CenterContentProps) {
  return (
    <div className="flex justify-center">
      <div className={`w-full max-w-screen-2xl ${className}`}>
        <div className={`rounded-sm ${background ?? ""}`}>
          <div
            className={`${skipPadX ? "" : "px-3"} ${skipPadY ? "" : "py-3"} ${childrenContainerClassName}`}
          >
            {children}
          </div>
        </div>
      </div>
    </div>
  );
}
