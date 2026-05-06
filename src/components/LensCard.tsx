import { Heart, Star, TrendingUp } from 'lucide-react';
import { Link } from 'react-router-dom';
import { Lens } from '@/types/lens';
import { useLensStore } from '@/store/lensStore';

interface LensCardProps {
  lens: Lens;
}

export default function LensCard({ lens }: LensCardProps) {
  const { toggleFavorite, isFavorite } = useLensStore();
  const favorite = isFavorite(lens.id);

  const ownershipColors = {
    high: 'bg-emerald-500/20 text-emerald-400',
    medium: 'bg-amber-500/20 text-amber-400',
    low: 'bg-zinc-500/20 text-zinc-400',
  };

  const ownershipLabels = {
    high: '高保有量',
    medium: '中等保有量',
    low: '低保有量',
  };

  return (
    <Link
      to={`/lens/${lens.id}`}
      className="group relative bg-zinc-900/80 border border-zinc-800/50 rounded-2xl overflow-hidden hover:border-amber-500/30 transition-all duration-300 hover:shadow-xl hover:shadow-amber-500/5 hover:-translate-y-1"
    >
      <div className="relative aspect-square overflow-hidden bg-gradient-to-br from-zinc-800 to-zinc-900">
        <img
          src={lens.imageUrl}
          alt={lens.model}
          className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
          loading="lazy"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-zinc-900 via-transparent to-transparent opacity-60" />

        <button
          onClick={(e) => {
            e.preventDefault();
            toggleFavorite(lens.id);
          }}
          className={`absolute top-3 right-3 p-2 rounded-full backdrop-blur-md transition-all ${
            favorite
              ? 'bg-amber-500 text-black'
              : 'bg-black/50 text-white hover:bg-black/70'
          }`}
        >
          <Heart className={`w-4 h-4 ${favorite ? 'fill-current' : ''}`} />
        </button>

        <div className="absolute bottom-3 left-3 flex flex-wrap gap-1.5">
          <span className="px-2 py-1 bg-black/60 backdrop-blur-sm rounded-md text-[10px] font-bold text-white uppercase tracking-wider">
            {lens.brand}
          </span>
          <span className="px-2 py-1 bg-black/60 backdrop-blur-sm rounded-md text-[10px] font-bold text-amber-400 uppercase tracking-wider">
            {lens.mount}
          </span>
          <span className={`px-2 py-1 backdrop-blur-sm rounded-md text-[10px] font-medium uppercase tracking-wider ${ownershipColors[lens.ownershipCount]}`}>
            {ownershipLabels[lens.ownershipCount]}
          </span>
        </div>
      </div>

      <div className="p-4">
        <div className="flex items-start justify-between gap-2 mb-2">
          <div className="flex-1 min-w-0">
            <h3 className="text-sm font-bold text-white truncate group-hover:text-amber-400 transition-colors">
              {lens.model}
            </h3>
            {lens.modelCode && (
              <p className="text-xs text-cyan-400 mt-0.5 font-mono">
                {lens.modelCode}
              </p>
            )}
            {lens.nickname && (
              <p className="text-xs text-zinc-500 mt-0.5">"{lens.nickname}"</p>
            )}
          </div>
          <span className="text-xs text-zinc-600 shrink-0">{lens.year}年</span>
        </div>

        <div className="flex items-center gap-3 mb-3">
          <span className="text-xs text-zinc-400">
            {lens.type === 'zoom' ? '变焦' : '定焦'}
          </span>
          <span className="text-xs text-zinc-600">•</span>
          <span className="text-xs text-zinc-400">{lens.aperture}</span>
          {lens.isStabilized && (
            <>
              <span className="text-xs text-zinc-600">•</span>
              <span className="text-xs text-emerald-500 flex items-center gap-0.5">
                <Star className="w-3 h-3 fill-current" />
                IS
              </span>
            </>
          )}
        </div>

        <div className="flex items-center justify-between pt-3 border-t border-zinc-800/50">
          <div className="flex items-center gap-1.5">
            <TrendingUp className="w-3.5 h-3.5 text-amber-500" />
            <div className="flex flex-col">
              <span className="text-[10px] text-zinc-500">二手价</span>
              <span className="text-sm font-bold text-white">
                ¥{lens.priceUsedMin.toLocaleString()}
                <span className="text-zinc-500 font-normal">-</span>
                {lens.priceUsedMax.toLocaleString()}
              </span>
            </div>
          </div>
          <div className="text-right">
            <span className="text-[10px] text-zinc-500">保值率</span>
            <p className={`text-sm font-bold ${
              lens.retentionRate >= 75 ? 'text-emerald-400' :
              lens.retentionRate >= 60 ? 'text-amber-400' : 'text-zinc-400'
            }`}>
              {lens.retentionRate}%
            </p>
          </div>
        </div>
      </div>
    </Link>
  );
}
