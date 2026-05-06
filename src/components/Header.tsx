import { Camera, Heart, Menu } from 'lucide-react';
import { Link, useNavigate } from 'react-router-dom';
import { useLensStore } from '@/store/lensStore';

export default function Header() {
  const navigate = useNavigate();
  const favorites = useLensStore((state) => state.favorites);

  return (
    <header className="sticky top-0 z-50 bg-zinc-950/95 backdrop-blur-md border-b border-zinc-800/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <Link to="/" className="flex items-center gap-3 group">
            <div className="relative">
              <Camera className="w-8 h-8 text-amber-500 transition-transform duration-300 group-hover:scale-110" />
              <div className="absolute -inset-2 bg-amber-500/20 rounded-full blur-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
            </div>
            <div className="flex flex-col">
              <span className="text-lg font-bold tracking-tight text-white">
                镜头速查
              </span>
              <span className="text-[10px] text-zinc-500 uppercase tracking-widest">
                Lens Finder
              </span>
            </div>
          </Link>

          <nav className="hidden md:flex items-center gap-6">
            <Link
              to="/"
              className="text-sm text-zinc-400 hover:text-white transition-colors"
            >
              全部镜头
            </Link>
            <Link
              to="/?tab=favorites"
              className="text-sm text-zinc-400 hover:text-white transition-colors flex items-center gap-1.5"
            >
              <Heart className="w-4 h-4" />
              收藏
              {favorites.length > 0 && (
                <span className="bg-amber-500 text-black text-xs font-bold px-1.5 py-0.5 rounded-full">
                  {favorites.length}
                </span>
              )}
            </Link>
          </nav>

          <div className="flex items-center gap-3">
            <button
              onClick={() => navigate('/?tab=favorites')}
              className="md:hidden p-2 text-zinc-400 hover:text-white transition-colors"
            >
              <Heart className="w-5 h-5" />
            </button>
            <button className="md:hidden p-2 text-zinc-400 hover:text-white transition-colors">
              <Menu className="w-5 h-5" />
            </button>
          </div>
        </div>
      </div>
    </header>
  );
}
