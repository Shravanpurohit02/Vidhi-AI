import { Search } from "lucide-react";

type Props = {
  value: string;
  onChange(value: string): void;
};

export default function DocumentSearch({
  value,
  onChange,
}: Props) {
  return (
    <div className="relative">
      <Search className="absolute left-3 top-3 h-4 w-4 text-slate-500" />

      <input
        className="w-full rounded-lg border bg-white py-2 pl-10 pr-3"
        placeholder="Search documents..."
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
    </div>
  );
}
