export interface Lens {
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

export interface Filters {
  brands: string[];
  mounts: string[];
  types: string[];
  focalRanges: string[];
  search: string;
}
