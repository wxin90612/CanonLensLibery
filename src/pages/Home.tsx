import { useState, useMemo } from 'react';
import { useSearchParams } from 'react-router-dom';
import { Heart } from 'lucide-react';
import Header from '@/components/Header';
import SearchBar from '@/components/SearchBar';
import FilterBar from '@/components/FilterBar';
import LensGrid from '@/components/LensGrid';
import Footer from '@/components/Footer';
import lensesData from '@/data/lenses.json';
import { Lens } from '@/types/lens';
import { useLensStore } from '@/store/lensStore';

const FOCAL_RANGE_MAP: Record<string, [number, number]> = {
  'ultra-wide': [0, 24],
  wide: [24, 35],
  standard: [35, 85],
  telephoto: [85, 200],
  'super-tele': [200, 999],
};

function parseFocalLength(focal: string): number {
  if (focal.includes('-')) {
    const parts = focal.replace(/[^0-9-]/g, '').split('-');
    return parseInt(parts[0]) || 0;
  }
  return parseInt(focal.replace(/[^0-9]/g, '')) || 0;
}

export default function Home() {
  const [searchParams] = useSearchParams();
  const tab = searchParams.get('tab');
  const [showFilters, setShowFilters] = useState(true);

  const filters = useLensStore((state) => state.filters);
  const favorites = useLensStore((state) => state.favorites);
  const lenses = lensesData as Lens[];

  const filteredLenses = useMemo(() => {
    let result = lenses;

    if (tab === 'favorites') {
      result = result.filter((lens) => favorites.includes(lens.id));
    }

    if (filters.brands.length > 0) {
      result = result.filter((lens) => filters.brands.includes(lens.brand));
    }

    if (filters.mounts.length > 0) {
      result = result.filter((lens) => filters.mounts.includes(lens.mount));
    }

    if (filters.types.length > 0) {
      result = result.filter((lens) => filters.types.includes(lens.type));
    }

    if (filters.focalRanges.length > 0) {
      result = result.filter((lens) => {
        const focal = parseFocalLength(lens.focalLength);
        return filters.focalRanges.some((range) => {
          const [min, max] = FOCAL_RANGE_MAP[range];
          return focal >= min && focal < max;
        });
      });
    }

    if (filters.search) {
      const search = filters.search.toLowerCase();
      result = result.filter(
        (lens) =>
          lens.model.toLowerCase().includes(search) ||
          lens.nickname.toLowerCase().includes(search) ||
          lens.brand.toLowerCase().includes(search)
      );
    }

    return result;
  }, [lenses, filters, tab, favorites]);

  const isFavoritesTab = tab === 'favorites';

  return (
    <div className="min-h-screen bg-zinc-950 text-white flex flex-col">
      <Header />

      <main className="flex-1 max-w-7xl mx-auto w-full px-4 sm:px-6 lg:px-8 py-6">
        <div className="mb-8">
          <h1 className="text-2xl sm:text-3xl font-bold text-white mb-2">
            {isFavoritesTab ? '我的收藏' : '镜头速查'}
          </h1>
          <p className="text-sm text-zinc-500">
            {isFavoritesTab
              ? `共 ${favorites.length} 款收藏镜头`
              : `共 ${lenses.length} 款镜头，筛选 ${filteredLenses.length} 款`}
          </p>
        </div>

        <div className="mb-6">
          <SearchBar />
        </div>

        <div className="flex gap-8">
          <div className="hidden lg:block w-72 shrink-0">
            <div className="sticky top-24">
              <FilterBar />
            </div>
          </div>

          <div className="flex-1 min-w-0">
            <div className="lg:hidden mb-6">
              <button
                onClick={() => setShowFilters(!showFilters)}
                className="w-full py-3 bg-zinc-900 border border-zinc-800 rounded-xl text-sm text-zinc-400 hover:text-white transition-colors"
              >
                {showFilters ? '隐藏筛选' : '显示筛选'}
              </button>
              {showFilters && (
                <div className="mt-4">
                  <FilterBar />
                </div>
              )}
            </div>

            {isFavoritesTab && favorites.length === 0 ? (
              <div className="flex flex-col items-center justify-center py-20">
                <div className="w-24 h-24 mb-6 rounded-full bg-zinc-800/50 flex items-center justify-center">
                  <Heart className="w-12 h-12 text-zinc-600" />
                </div>
                <h3 className="text-lg font-medium text-zinc-300 mb-2">暂无收藏</h3>
                <p className="text-sm text-zinc-500">点击镜头卡片上的心形图标添加收藏</p>
              </div>
            ) : (
              <LensGrid lenses={filteredLenses} />
            )}
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
}
