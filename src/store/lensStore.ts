import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { Filters } from '@/types/lens';

type SortBy = 'price-asc' | 'price-desc' | 'year-asc' | 'year-desc' | 'none';

interface LensStore {
  filters: Filters;
  favorites: string[];
  sortBy: SortBy;
  setFilters: (filters: Partial<Filters>) => void;
  resetFilters: () => void;
  setSortBy: (sortBy: SortBy) => void;
  toggleFavorite: (lensId: string) => void;
  isFavorite: (lensId: string) => boolean;
}

const initialFilters: Filters = {
  brands: [],
  mounts: [],
  types: [],
  focalRanges: [],
  eras: [],
  search: '',
};

export const useLensStore = create<LensStore>()(
  persist(
    (set, get) => ({
      filters: initialFilters,
      favorites: [],
      sortBy: 'none',
      setFilters: (newFilters) =>
        set((state) => ({
          filters: { ...state.filters, ...newFilters },
        })),
      resetFilters: () => set({ filters: initialFilters, sortBy: 'none' }),
      setSortBy: (sortBy) => set({ sortBy }),
      toggleFavorite: (lensId) =>
        set((state) => ({
          favorites: state.favorites.includes(lensId)
            ? state.favorites.filter((id) => id !== lensId)
            : [...state.favorites, lensId],
        })),
      isFavorite: (lensId) => get().favorites.includes(lensId),
    }),
    {
      name: 'lens-storage',
    }
  )
);
