import { createRoot } from 'react-dom/client';
import { StrictMode } from 'react';
import SearchBox from '../components/SearchBox';

/**
 * Creates a SearchBox component and renders it inside the specified element ID
 * @param id - The ID of the element where the SearchBox should be rendered
 * @returns void
 */
export function createSearchBox(id: string): void {
    const container = document.getElementById(id);
    if (!container) {
        console.error(`Element with id "${id}" not found`);
        return;
    }

    const root = createRoot(container);
    root.render(
        <StrictMode>
            <SearchBox />
        </StrictMode>
    );
}

// Make the function available globally when the script is loaded in a browser
declare global {
    interface Window {
        createSearchBox: typeof createSearchBox;
    }
}

// Assign the function to the window object
if (typeof window !== 'undefined') {
    window.createSearchBox = createSearchBox;
}

export default createSearchBox;
