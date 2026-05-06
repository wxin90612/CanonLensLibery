import LensCard from '@/components/LensCard';
import { Lens } from '@/types/lens';

interface LensGridProps {
  lenses: Lens[];
}

export default function LensGrid({ lenses }: LensGridProps) {
  if (lenses.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-20">
        <div className="w-24 h-24 mb-6 rounded-full bg-zinc-800/50 flex items-center justify-center">
          <svg
            className="w-12 h-12 text-zinc-600"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={1.5}
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
        </div>
        <h3 className="text-lg font-medium text-zinc-300 mb-2">未找到匹配镜头</h3>
        <p className="text-sm text-zinc-500">尝试调整筛选条件或关键词</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
      {lenses.map((lens, index) => (
        <div
          key={lens.id}
          className="animate-in fade-in slide-in-from-bottom-4"
          style={{ animationDelay: `${index * 50}ms` }}
        >
          <LensCard lens={lens} />
        </div>
      ))}
    </div>
  );
}
