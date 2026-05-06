import { Camera } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="bg-zinc-950 border-t border-zinc-800/50 py-8 mt-auto">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <Camera className="w-5 h-5 text-amber-500" />
            <span className="text-sm text-zinc-400">镜头速查</span>
          </div>
          <p className="text-xs text-zinc-500 text-center">
            数据来源：闲鱼、转转等二手平台 | 仅供参考，价格以实际为准
          </p>
          <p className="text-xs text-zinc-600">
            © 2024 Lens Finder
          </p>
        </div>
      </div>
    </footer>
  );
}
