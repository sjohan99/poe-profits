export type CenterContentProps = {
  children: React.ReactNode;
  background?: string;
  className?: string;
  childrenContainerClassName?: string;
};

export function CenterContent(props: CenterContentProps) {
  const extra_styling = props.className ?? "";
  const childrenContainerClassName = props.childrenContainerClassName ?? "";
  return (
    <div className="flex justify-center">
      <div className={`w-full max-w-screen-2xl ${extra_styling}`.trim()}>
        <div className={`rounded-sm ${props.background ?? ""}`.trim()}>
          <div className={`px-3 py-3  ${childrenContainerClassName}`}>
            {props.children}
          </div>
        </div>
      </div>
    </div>
  );
}
