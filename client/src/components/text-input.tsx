import React from "react";
import { useDebounce } from "react-use";

type TextInputProps = {
  inputCallback: (search: string) => void;
  placeholderText?: string;
  debounceMs?: number;
  restriction?: "number" | "text";
  textPosition?: "left" | "center";
};

export default function TextInput(params: TextInputProps) {
  const {
    placeholderText = "",
    inputCallback,
    debounceMs = 500,
    restriction,
    textPosition = "left",
  } = params;
  const [value, setValue] = React.useState("");

  useDebounce(
    () => {
      inputCallback(value);
    },
    debounceMs,
    [value],
  );

  return (
    <input
      type={restriction ? restriction : "text"}
      className={`h-10 w-full rounded border border-accent-2 bg-transparent placeholder-shown:border-opacity-50 ${textPosition === "center" ? "text-center" : "pl-2"}`}
      placeholder={placeholderText}
      onChange={({ currentTarget }) => {
        setValue(currentTarget.value);
      }}
    />
  );
}
