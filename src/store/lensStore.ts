import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { Filters } from '@/types/lens';

interface LensStore {
  filters: Filters;
  favorites: string[];
  setFilters: (filters: Partial<Filters>) => void;
  resetFilters: () => void;
  toggleFavorite: (lensId: string) => void;
  isFavorite: (lensId: string) => boolean;
}

const initialFilters: Filters = {
  brands: [],
  mounts: [],
  types: [],
  focalRanges: [],
  search: '',
};

export const useLensStore = create<LensStore>()(
  persist(
    (set, get) => ({
      filters: initialFilters,
      favorites: [],
      setFilters: (newFilters) =>
        set((state) => ({
          filters: { ...state.filters, ...newFilters },
        })),
      resetFilters: () => set({ filters: initialFilters }),
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
