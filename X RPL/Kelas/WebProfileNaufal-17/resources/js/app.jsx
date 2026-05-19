import React from 'react';
import { createRoot } from 'react-dom/client';
import ProfileApp from './components/ProfileApp';

const container = document.getElementById('app');
if (container) {
    const root = createRoot(container);
    root.render(<ProfileApp />);
}
