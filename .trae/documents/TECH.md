# 镜头速查 - 技术架构文档

## 1. 技术栈

- **框架**：React 18 + Vite
- **样式**：TailwindCSS
- **图标**：Lucide React
- **路由**：React Router DOM v6
- **动画**：CSS Transitions + Framer Motion
- **数据**：本地JSON文件 + LocalStorage

---

## 2. 项目结构

```
/workspace/
├── index.html
├── package.json
├── vite.config.js
├── tailwind.config.js
├── postcss.config.js
├── src/
│   ├── main.jsx
│   ├── App.jsx
│   ├── index.css
│   ├── components/
│   │   ├── Header/
│   │   │   └── Header.jsx
│   │   ├── FilterBar/
│   │   │   └── FilterBar.jsx
│   │   ├── LensCard/
│   │   │   └── LensCard.jsx
│   │   ├── LensGrid/
│   │   │   └── LensGrid.jsx
│   │   ├── LensDetail/
│   │   │   └── LensDetail.jsx
│   │   ├── SearchBar/
│   │   │   └── SearchBar.jsx
│   │   └── Footer/
│   │       └── Footer.jsx
│   ├── pages/
│   │   ├── HomePage.jsx
│   │   └── LensDetailPage.jsx
│   ├── data/
│   │   └── lenses.json
│   ├── hooks/
│   │   └── useFilters.js
│   └── utils/
│       └── constants.js
└── public/
    └── favicon.ico
```

---

## 3. 路由定义

| 路由 | 组件 | 说明 |
|------|------|------|
| `/` | HomePage | 首页-筛选+镜头列表 |
| `/lens/:id` | LensDetailPage | 镜头详情页 |

---

## 4. 数据模型

### 4.1 镜头数据结构

```typescript
interface Lens {
  id: string;
  brand: 'Canon' | 'Tamron' | 'Sigma';
  mount: 'EF' | 'RF';
  model: string;
  nickname: string;
  year: number;
  type: 'zoom' | 'prime';
  focalLength: string;
  aperture: string;
  isStabilized: boolean;
  weight: number;
  minFocusDistance: string;
  filterSize: string;
  priceNew: number;
  priceUsedMin: number;
  priceUsedMax: number;
  retentionRate: number;
  ownershipCount: 'high' | 'medium' | 'low';
  pros: string[];
  cons: string[];
  commonIssues: string[];
  imageUrl: string;
  purchaseAdvice: string;
  specs: Record<string, string>;
}
```

---

## 5. 组件层级

```
App
├── Header
├── Router
│   ├── HomePage
│   │   ├── SearchBar
│   │   ├── FilterBar
│   │   └── LensGrid
│   │       └── LensCard (×n)
│   └── LensDetailPage
│       └── LensDetail
└── Footer
```

---

## 6. 状态管理

### 6.1 全局状态（React Context）

- `FilterContext`：筛选条件状态
- `FavoritesContext`：收藏夹数据

### 6.2 本地存储

- `localStorage.lensFavorites`：收藏的镜头ID列表
- `localStorage.filterState`：上次筛选状态

---

## 7. 筛选逻辑

```javascript
// 筛选条件
const filters = {
  brands: [], // ['Canon', 'Tamron', 'Sigma']
  mounts: [], // ['EF', 'RF']
  types: [],  // ['zoom', 'prime']
  focalRange: null, // 'wide' | 'standard' | 'telephoto'
  search: ''
};

// 筛选函数
function filterLenses(lenses, filters) {
  return lenses.filter(lens => {
    const brandMatch = filters.brands.length === 0 || filters.brands.includes(lens.brand);
    const mountMatch = filters.mounts.length === 0 || filters.mounts.includes(lens.mount);
    const typeMatch = filters.types.length === 0 || filters.types.includes(lens.type);
    const searchMatch = lens.model.toLowerCase().includes(filters.search.toLowerCase()) ||
                        lens.nickname.toLowerCase().includes(filters.search.toLowerCase());
    return brandMatch && mountMatch && typeMatch && searchMatch;
  });
}
```

---

## 8. 性能优化

- 图片懒加载（Intersection Observer）
- 筛选结果缓存
- 虚拟列表（大数据量时）
- CSS 动画替代 JS 动画

---

## 9. 浏览器兼容

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
