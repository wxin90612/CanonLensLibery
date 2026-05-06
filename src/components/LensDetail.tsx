import {
  ArrowLeft,
  Heart,
  AlertTriangle,
  CheckCircle,
  XCircle,
  ChevronDown,
  ChevronUp,
  Star,
  TrendingUp,
} from 'lucide-react';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { Lens } from '@/types/lens';
import { useLensStore } from '@/store/lensStore';

interface LensDetailProps {
  lens: Lens;
}

export default function LensDetail({ lens }: LensDetailProps) {
  const { toggleFavorite, isFavorite } = useLensStore();
  const favorite = isFavorite(lens.id);
  const [expandedFaq, setExpandedFaq] = useState<number | null>(null);

  const ownershipColors = {
    high: 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30',
    medium: 'bg-amber-500/20 text-amber-400 border-amber-500/30',
    low: 'bg-zinc-500/20 text-zinc-400 border-zinc-500/30',
  };

  const retentionColor =
    lens.retentionRate >= 75
      ? 'text-emerald-400'
      : lens.retentionRate >= 60
      ? 'text-amber-400'
      : 'text-zinc-400';

  return (
    <div className="min-h-screen bg-zinc-950">
      <div className="max-w-6xl mx-auto px-4 py-6">
        <Link
          to="/"
          className="inline-flex items-center gap-2 text-zinc-400 hover:text-white transition-colors mb-6"
        >
          <ArrowLeft className="w-4 h-4" />
          返回列表
        </Link>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="relative">
            <div className="aspect-square rounded-3xl overflow-hidden bg-gradient-to-br from-zinc-800 to-zinc-900 border border-zinc-800/50">
              <img
                src={lens.imageUrl}
                alt={lens.model}
                className="w-full h-full object-cover"
              />
            </div>
            <button
              onClick={() => toggleFavorite(lens.id)}
              className={`absolute top-4 right-4 p-3 rounded-full backdrop-blur-md transition-all ${
                favorite
                  ? 'bg-amber-500 text-black'
                  : 'bg-black/60 text-white hover:bg-black/80'
              }`}
            >
              <Heart className={`w-5 h-5 ${favorite ? 'fill-current' : ''}`} />
            </button>
          </div>

          <div className="space-y-6">
            <div>
              <div className="flex flex-wrap gap-2 mb-3">
                <span className="px-3 py-1 bg-zinc-800 rounded-lg text-sm font-bold text-white">
                  {lens.brand}
                </span>
                <span className="px-3 py-1 bg-amber-500/20 rounded-lg text-sm font-bold text-amber-400">
                  {lens.mount}
                </span>
                <span className={`px-3 py-1 rounded-lg text-sm font-medium border ${
                  lens.era === 'film' ? 'bg-amber-500/20 text-amber-400 border-amber-500/30' :
                  lens.era === 'digital' ? 'bg-blue-500/20 text-blue-400 border-blue-500/30' :
                  'bg-emerald-500/20 text-emerald-400 border-emerald-500/30'
                }`}>
                  {lens.era === 'film' ? '胶片时代' : lens.era === 'digital' ? '数码时代' : '无反时代'}
                </span>
                <span className={`px-3 py-1 rounded-lg text-sm font-medium border ${ownershipColors[lens.ownershipCount]}`}>
                  {lens.ownershipCount === 'high' ? '高保有量' : lens.ownershipCount === 'medium' ? '中等保有量' : '低保有量'}
                </span>
              </div>
              <h1 className="text-2xl lg:text-3xl font-bold text-white mb-2">
                {lens.model}
              </h1>
              {lens.modelCode && (
                <p className="text-lg text-cyan-400 font-mono mb-1">
                  {lens.modelCode}
                </p>
              )}
              {lens.nickname && (
                <p className="text-lg text-zinc-400">"{lens.nickname}"</p>
              )}
              <p className="text-sm text-zinc-500 mt-1">{lens.year}年发布</p>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
              <div className="bg-zinc-900/80 rounded-xl p-4 border border-zinc-800/50">
                <p className="text-xs text-zinc-500 mb-1">类型</p>
                <p className="text-sm font-medium text-white">
                  {lens.type === 'zoom' ? '变焦镜头' : '定焦镜头'}
                </p>
              </div>
              <div className="bg-zinc-900/80 rounded-xl p-4 border border-zinc-800/50">
                <p className="text-xs text-zinc-500 mb-1">焦段</p>
                <p className="text-sm font-medium text-white">{lens.focalLength}</p>
              </div>
              <div className="bg-zinc-900/80 rounded-xl p-4 border border-zinc-800/50">
                <p className="text-xs text-zinc-500 mb-1">光圈</p>
                <p className="text-sm font-medium text-white">{lens.aperture}</p>
              </div>
              <div className="bg-zinc-900/80 rounded-xl p-4 border border-zinc-800/50">
                <p className="text-xs text-zinc-500 mb-1">防抖</p>
                <p className="text-sm font-medium text-white flex items-center gap-1">
                  {lens.isStabilized ? (
                    <>
                      <Star className="w-3.5 h-3.5 text-emerald-400 fill-current" />
                      支持
                    </>
                  ) : (
                    <span className="text-zinc-500">不支持</span>
                  )}
                </p>
              </div>
              <div className="bg-zinc-900/80 rounded-xl p-4 border border-zinc-800/50">
                <p className="text-xs text-zinc-500 mb-1">重量</p>
                <p className="text-sm font-medium text-white">{lens.weight}g</p>
              </div>
              <div className="bg-zinc-900/80 rounded-xl p-4 border border-zinc-800/50">
                <p className="text-xs text-zinc-500 mb-1">滤镜口径</p>
                <p className="text-sm font-medium text-white">{lens.filterSize}</p>
              </div>
              <div className="bg-zinc-900/80 rounded-xl p-4 border border-zinc-800/50">
                <p className="text-xs text-zinc-500 mb-1">最近对焦</p>
                <p className="text-sm font-medium text-white">{lens.minFocusDistance}</p>
              </div>
              <div className="bg-zinc-900/80 rounded-xl p-4 border border-zinc-800/50">
                <p className="text-xs text-zinc-500 mb-1">保值率</p>
                <p className={`text-sm font-bold ${retentionColor}`}>
                  {lens.retentionRate}%
                </p>
              </div>
            </div>

            <div className="bg-gradient-to-r from-amber-500/10 to-orange-500/10 rounded-2xl p-6 border border-amber-500/20">
              <div className="flex items-center gap-2 mb-4">
                <TrendingUp className="w-5 h-5 text-amber-500" />
                <span className="text-sm font-medium text-white">价格参考</span>
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <p className="text-xs text-zinc-500 mb-1">新品价格</p>
                  <p className="text-xl font-bold text-white">
                    ¥{lens.priceNew.toLocaleString()}
                  </p>
                </div>
                <div>
                  <p className="text-xs text-zinc-500 mb-1">二手价格区间</p>
                  <p className="text-xl font-bold text-amber-400">
                    ¥{lens.priceUsedMin.toLocaleString()} - ¥{lens.priceUsedMax.toLocaleString()}
                  </p>
                </div>
              </div>
              <p className="text-xs text-zinc-400 mt-3 flex items-center gap-1">
                <span className="w-1.5 h-1.5 bg-amber-500 rounded-full"></span>
                数据来源：闲鱼、转转等二手平台平均价格
              </p>
            </div>

            <div className="bg-emerald-500/10 rounded-2xl p-5 border border-emerald-500/20">
              <div className="flex items-center gap-2 mb-3">
                <CheckCircle className="w-5 h-5 text-emerald-500" />
                <span className="text-sm font-medium text-white">购买建议</span>
              </div>
              <p className="text-sm text-zinc-300">{lens.purchaseAdvice}</p>
            </div>
          </div>
        </div>

        <div className="mt-10 grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="space-y-5">
            <h2 className="text-lg font-bold text-white flex items-center gap-2">
              <span className="w-1 h-6 bg-emerald-500 rounded-full"></span>
              优点
            </h2>
            <div className="space-y-2">
              {lens.pros.map((pro, index) => (
                <div
                  key={index}
                  className="flex items-start gap-3 p-3 bg-emerald-500/5 rounded-xl border border-emerald-500/10"
                >
                  <CheckCircle className="w-4 h-4 text-emerald-500 shrink-0 mt-0.5" />
                  <span className="text-sm text-zinc-300">{pro}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="space-y-5">
            <h2 className="text-lg font-bold text-white flex items-center gap-2">
              <span className="w-1 h-6 bg-red-500 rounded-full"></span>
              缺点
            </h2>
            <div className="space-y-2">
              {lens.cons.map((con, index) => (
                <div
                  key={index}
                  className="flex items-start gap-3 p-3 bg-red-500/5 rounded-xl border border-red-500/10"
                >
                  <XCircle className="w-4 h-4 text-red-500 shrink-0 mt-0.5" />
                  <span className="text-sm text-zinc-300">{con}</span>
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="mt-10">
          <h2 className="text-lg font-bold text-white flex items-center gap-2 mb-5">
            <span className="w-1 h-6 bg-amber-500 rounded-full"></span>
            常见问题
          </h2>
          <div className="space-y-3">
            {lens.commonIssues.map((issue, index) => (
              <div
                key={index}
                className="bg-zinc-900/80 rounded-xl border border-zinc-800/50 overflow-hidden"
              >
                <button
                  onClick={() => setExpandedFaq(expandedFaq === index ? null : index)}
                  className="w-full flex items-center justify-between p-4 text-left"
                >
                  <div className="flex items-center gap-3">
                    <AlertTriangle className="w-4 h-4 text-amber-500" />
                    <span className="text-sm font-medium text-white">{issue}</span>
                  </div>
                  {expandedFaq === index ? (
                    <ChevronUp className="w-4 h-4 text-zinc-500" />
                  ) : (
                    <ChevronDown className="w-4 h-4 text-zinc-500" />
                  )}
                </button>
                {expandedFaq === index && (
                  <div className="px-4 pb-4 pt-0">
                    <p className="text-sm text-zinc-400 pl-7">
                      购买时请仔细检查镜头对焦马达和镜筒机构，必要时可要求卖家提供实拍样张。
                    </p>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>

        <div className="mt-10">
          <h2 className="text-lg font-bold text-white flex items-center gap-2 mb-5">
            <span className="w-1 h-6 bg-zinc-500 rounded-full"></span>
            详细参数
          </h2>
          <div className="bg-zinc-900/80 rounded-2xl border border-zinc-800/50 p-6">
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-4">
              {Object.entries(lens.specs).map(([key, value]) => (
                <div key={key} className="p-3 bg-zinc-800/50 rounded-xl">
                  <p className="text-xs text-zinc-500 mb-1">{key}</p>
                  <p className="text-sm font-medium text-white">{value}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
