import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import HomePage from './Homepage';
import BlogDetail from './BlogDetail';
import TagSearchPage from './TagSearchPage';

function App() {
  return (
    <BrowserRouter>
      <div>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/blog/:id" element={<BlogDetail />} />
          <Route path="/tags/:tagName" element={<TagSearchPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;