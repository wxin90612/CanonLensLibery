import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "@/pages/Home";
import LensDetailPage from "@/pages/LensDetailPage";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/lens/:id" element={<LensDetailPage />} />
      </Routes>
    </Router>
  );
}
