import { Filter, X, ArrowUpDown } from 'lucide-react';
import { useLensStore } from '@/store/lensStore';

const BRANDS = ['Canon', 'Tamron', 'Sigma'];
const MOUNTS = ['EF', 'RF'];
const TYPES = [
  { value: 'zoom', label: '变焦' },
  { value: 'prime', label: '定焦' },
];
const FOCAL_RANGES = [
  { value: 'ultra-wide', label: '超广角(<24mm)', min: 0, max: 24 },
  { value: 'wide', label: '广角(24-35mm)', min: 24, max: 35 },
  { value: 'standard', label: '标准(35-85mm)', min: 35, max: 85 },
  { value: 'telephoto', label: '长焦(85-200mm)', min: 85, max: 200 },
  { value: 'super-tele', label: '超长焦(>200mm)', min: 200, max: 999 },
];
const ERAS = [
  { value: 'film', label: '胶片时代' },
  { value: 'digital', label: '数码时代' },
  { value: 'mirrorless', label: '无反时代' },
];
const SORT_OPTIONS = [
  { value: 'none', label: '默认排序' },
  { value: 'price-asc', label: '价格↑' },
  { value: 'price-desc', label: '价格↓' },
  { value: 'year-asc', label: '年份↑' },
  { value: 'year-desc', label: '年份↓' },
];

export default function FilterBar() {
  const filters = useLensStore((state) => state.filters);
  const sortBy = useLensStore((state) => state.sortBy);
  const setFilters = useLensStore((state) => state.setFilters);
  const setSortBy = useLensStore((state) => state.setSortBy);
  const resetFilters = useLensStore((state) => state.resetFilters);

  const toggleArrayFilter = (
    key: 'brands' | 'mounts' | 'types' | 'focalRanges' | 'eras',
    value: string
  ) => {
    const current = filters[key];
    const updated = current.includes(value)
      ? current.filter((v) => v !== value)
      : [...current, value];
    setFilters({ [key]: updated });
  };

  const hasActiveFilters =
    filters.brands.length > 0 ||
    filters.mounts.length > 0 ||
    filters.types.length > 0 ||
    filters.focalRanges.length > 0 ||
    filters.eras.length > 0 ||
    sortBy !== 'none';

  return (
    <div className="bg-zinc-900/50 rounded-2xl border border-zinc-800/50 p-5">
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <Filter className="w-4 h-4 text-amber-500" />
          <span className="text-sm font-medium text-white">筛选条件</span>
        </div>
        {hasActiveFilters && (
          <button
            onClick={resetFilters}
            className="text-xs text-zinc-500 hover:text-amber-500 transition-colors flex items-center gap-1"
          >
            <X className="w-3 h-3" />
            清除全部
          </button>
        )}
      </div>

      <div className="space-y-5">
        <div>
          <label className="text-xs text-zinc-500 uppercase tracking-wider mb-2 block flex items-center gap-1">
            <ArrowUpDown className="w-3 h-3" />
            排序
          </label>
          <select
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value as any)}
            className="w-full px-3 py-2 rounded-lg text-sm bg-zinc-800/80 text-zinc-300 border border-zinc-700 focus:outline-none focus:border-amber-500"
          >
            {SORT_OPTIONS.map((opt) => (
              <option key={opt.value} value={opt.value}>
                {opt.label}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label className="text-xs text-zinc-500 uppercase tracking-wider mb-2 block">
            品牌
          </label>
          <div className="flex flex-wrap gap-2">
            {BRANDS.map((brand) => (
              <button
                key={brand}
                onClick={() => toggleArrayFilter('brands', brand)}
                className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                  filters.brands.includes(brand)
                    ? 'bg-amber-500 text-black'
                    : 'bg-zinc-800/80 text-zinc-300 hover:bg-zinc-700'
                }`}
              >
                {brand}
              </button>
            ))}
          </div>
        </div>

        <div>
          <label className="text-xs text-zinc-500 uppercase tracking-wider mb-2 block">
            卡口
          </label>
          <div className="flex flex-wrap gap-2">
            {MOUNTS.map((mount) => (
              <button
                key={mount}
                onClick={() => toggleArrayFilter('mounts', mount)}
                className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                  filters.mounts.includes(mount)
                    ? 'bg-amber-500 text-black'
                    : 'bg-zinc-800/80 text-zinc-300 hover:bg-zinc-700'
                }`}
              >
                {mount}
              </button>
            ))}
          </div>
        </div>

        <div>
          <label className="text-xs text-zinc-500 uppercase tracking-wider mb-2 block">
            类型
          </label>
          <div className="flex flex-wrap gap-2">
            {TYPES.map((type) => (
              <button
                key={type.value}
                onClick={() => toggleArrayFilter('types', type.value)}
                className={`px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                  filters.types.includes(type.value)
                    ? 'bg-amber-500 text-black'
                    : 'bg-zinc-800/80 text-zinc-300 hover:bg-zinc-700'
                }`}
              >
                {type.label}
              </button>
            ))}
          </div>
        </div>

        <div>
          <label className="text-xs text-zinc-500 uppercase tracking-wider mb-2 block">
            时代
          </label>
          <div className="flex flex-wrap gap-2">
            {ERAS.map((era) => (
              <button
                key={era.value}
                onClick={() => toggleArrayFilter('eras', era.value)}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                  filters.eras.includes(era.value)
                    ? 'bg-amber-500 text-black'
                    : 'bg-zinc-800/80 text-zinc-300 hover:bg-zinc-700'
                }`}
              >
                {era.label}
              </button>
            ))}
          </div>
        </div>

        <div>
          <label className="text-xs text-zinc-500 uppercase tracking-wider mb-2 block">
            焦段
          </label>
          <div className="flex flex-wrap gap-2">
            {FOCAL_RANGES.map((range) => (
              <button
                key={range.value}
                onClick={() => toggleArrayFilter('focalRanges', range.value)}
                className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                  filters.focalRanges.includes(range.value)
                    ? 'bg-amber-500 text-black'
                    : 'bg-zinc-800/80 text-zinc-300 hover:bg-zinc-700'
                }`}
              >
                {range.label}
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
