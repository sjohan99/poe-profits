import Image from "next/image";

function BlankImage(props: { width: number; height: number }) {
  const { width, height } = props;

  return <div style={{ width, height }}></div>;
}

export function ItemImage(props: { icon: string | null; alt: string }) {
  const { icon, alt } = props;

  if (!icon) {
    return <BlankImage width={32} height={32} />;
  }

  return (
    <Image
      src={icon ? icon : "/items/blank.png"}
      width={32}
      height={32}
      alt={alt}
      unoptimized
      className="h-8 w-8 object-contain"
    ></Image>
  );
}
