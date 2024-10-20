export type CheckBoxProps = {
  checked: boolean;
  onChange: () => void;
  id: string;
  label?: string;
};

export function CheckBox({ checked, onChange, id, label }: CheckBoxProps) {
  return (
    <div className="flex items-center">
      <input
        id={id}
        type="checkbox"
        className="h-5 w-5 rounded border-orange-600 bg-secondary-1 text-background"
        checked={checked}
        onChange={onChange}
      />
      {label && (
        <label
          htmlFor={id}
          className="ms-2 cursor-pointer text-lg font-medium text-secondary-2"
        >
          {label}
        </label>
      )}
    </div>
  );
}
