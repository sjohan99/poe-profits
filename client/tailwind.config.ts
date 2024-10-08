import { type Config } from "tailwindcss";
import { fontFamily } from "tailwindcss/defaultTheme";

export default {
  content: ["./src/**/*.tsx"],
  safelist: [
    {
      pattern: /^grid-cols-\d+$/, // for src/components/table.tsx since it uses dynamic classes
    },
    {
      pattern: /^col-span-\d+$/, // for src/components/table.tsx since it uses dynamic classes
    },
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["var(--font-geist-sans)", ...fontFamily.sans],
      },
      colors: {
        background: "#012533",
        primary: "#012E40",
        secondary: {
          1: "#F2E3D5",
          2: "#ADA399",
        },
        accent: {
          1: "#024959",
          2: "#026773",
          3: "#013245",
        },
        link: "#3b82f6",
        warn: "#EF6A00",
        green: "#5FA052",
        red: "#CB4C4E",
      },
      screens: {
        "-2xl": { max: "1535px" },
        "-xl": { max: "1279px" },
        "-lg": { max: "1023px" },
        "-md": { max: "767px" },
        "-sm": { max: "639px" },
      },
      minWidth: {
        sm: "640px",
        md: "768px",
        lg: "1024px",
        xl: "1280px",
        "2xl": "1536px",
      },
    },
  },
  plugins: [],
} satisfies Config;
