import { useMemo } from 'react';
import { useParams, Navigate } from 'react-router-dom';
import LensDetail from '@/components/LensDetail';
import lensesData from '@/data/lenses.json';
import { Lens } from '@/types/lens';

export default function LensDetailPage() {
  const { id } = useParams<{ id: string }>();
  const lenses = lensesData as Lens[];

  const lens = useMemo(() => {
    return lenses.find((l) => l.id === id);
  }, [id, lenses]);

  if (!lens) {
    return <Navigate to="/" replace />;
  }

  return <LensDetail lens={lens} />;
}
