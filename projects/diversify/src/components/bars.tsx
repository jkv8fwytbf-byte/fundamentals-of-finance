import type { Slice } from "../lib/types";

export function StackedBar({ slices, height = 14 }: { slices: Slice[]; height?: number }) {
  if (!slices.length) {
    return <div className="h-3.5 rounded-full bg-sunken" />;
  }
  return (
    <div
      className="flex overflow-hidden rounded-full bg-sunken"
      style={{ height }}
    >
      {slices.map((slice) => (
        <div
          key={slice.id}
          title={`${slice.name} ${Math.round(slice.weight * 100)}%`}
          style={{
            width: `${Math.max(slice.weight * 100, 0.6)}%`,
            background: slice.color,
          }}
        />
      ))}
    </div>
  );
}

export function RowBar({
  label,
  value,
  color = "var(--brass)",
  hint,
}: {
  label: string;
  value: number;
  color?: string;
  hint?: string;
}) {
  const pct = Math.max(0, Math.min(100, value * 100));
  return (
    <div className="grid grid-cols-[1fr_auto] items-end gap-x-3 gap-y-1">
      <div className="text-sm text-ink">{label}</div>
      <div className="font-mono text-xs text-muted">{Math.round(pct)}%</div>
      <div className="col-span-2 h-1.5 overflow-hidden rounded-full bg-sunken">
        <div className="h-full rounded-full" style={{ width: `${pct}%`, background: color }} />
      </div>
      {hint ? <p className="col-span-2 text-xs text-faint">{hint}</p> : null}
    </div>
  );
}

export function SignedBar({
  label,
  value,
  plus,
  minus,
}: {
  label: string;
  value: number;
  plus: string;
  minus: string;
}) {
  const mag = Math.min(1, Math.abs(value));
  const right = value >= 0;
  return (
    <div className="space-y-1.5">
      <div className="flex items-baseline justify-between gap-3">
        <div className="text-sm text-ink">{label}</div>
        <div className="font-mono text-xs text-muted">
          {right ? "+" : "−"}
          {Math.round(mag * 100)}
        </div>
      </div>
      <div className="relative h-1.5 rounded-full bg-sunken">
        <div className="absolute top-0 left-1/2 h-full w-px bg-line-strong" />
        <div
          className="absolute top-0 h-full rounded-full"
          style={{
            width: `${mag * 50}%`,
            left: right ? "50%" : `${50 - mag * 50}%`,
            background: right ? "var(--brass)" : "var(--fox)",
          }}
        />
      </div>
      <div className="flex justify-between gap-4 text-[0.7rem] leading-snug text-faint">
        <span className="max-w-[48%]">{minus}</span>
        <span className="max-w-[48%] text-right">{plus}</span>
      </div>
    </div>
  );
}
