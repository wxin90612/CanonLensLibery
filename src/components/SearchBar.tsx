import { Search, X } from 'lucide-react';
import { useLensStore } from '@/store/lensStore';

export default function SearchBar() {
  const filters = useLensStore((state) => state.filters);
  const setFilters = useLensStore((state) => state.setFilters);

  return (
    <div className="relative">
      <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-zinc-500" />
      <input
        type="text"
        placeholder="搜索镜头型号、绰号..."
        value={filters.search}
        onChange={(e) => setFilters({ search: e.target.value })}
        className="w-full pl-12 pr-10 py-3.5 bg-zinc-900/80 border border-zinc-800 rounded-xl text-white placeholder-zinc-500 focus:outline-none focus:border-amber-500/50 focus:ring-2 focus:ring-amber-500/20 transition-all"
      />
      {filters.search && (
        <button
          onClick={() => setFilters({ search: '' })}
          className="absolute right-4 top-1/2 -translate-y-1/2 p-1 text-zinc-500 hover:text-white transition-colors"
        >
          <X className="w-4 h-4" />
        </button>
      )}
    </div>
  );
}
