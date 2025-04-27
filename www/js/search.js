/*
const pages = {
    "cd": {
        "summary": "Changes the current directory",
    },
    "cp": {
        "summary": "Copies files and directories",
    },
    "less": {
        "summary": "Displays the contents of a file",
    },
    "ls": {
        "summary": "Lists files in a directory",
    },
    "pwd": {
        "summary": "Prints the current working directory",
    },
    // Add more commands here
};
*/
document.addEventListener('DOMContentLoaded', function () {
    // Event handlers to prevent scrolling and other interactions
    function preventWheel(e) {
        // Allow scrolling within the search results panel
        if (e.target.closest('.search-results-panel')) {
            return;
        }
        e.preventDefault();
        e.stopPropagation();
    }

    function preventTouch(e) {
        // Allow touch interactions within the search results panel
        if (e.target.closest('.search-results-panel')) {
            return;
        }
        e.preventDefault();
        e.stopPropagation();
    }

    function preventKeyScroll(e) {
        // Keys that typically cause scrolling or navigation
        const scrollKeys = [
            'Space', 'PageUp', 'PageDown', 'End', 'Home',
            'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'
        ];

        // Allow keyboard navigation within the search results panel
        if (e.target.closest('.search-results-panel') ||
            e.target.id === 'nav-searchbox' ||
            e.target.id === 'searchbox-2') {
            return;
        }

        if (scrollKeys.includes(e.key)) {
            e.preventDefault();
            e.stopPropagation();
        }
    }

    // Function to disable scrolling and other interactions
    function disableInteractions() {
        document.addEventListener('wheel', preventWheel, { passive: false });
        document.addEventListener('touchmove', preventTouch, { passive: false });
        document.addEventListener('keydown', preventKeyScroll);
    }

    // Function to re-enable scrolling and other interactions
    function enableInteractions() {
        document.removeEventListener('wheel', preventWheel);
        document.removeEventListener('touchmove', preventTouch);
        document.removeEventListener('keydown', preventKeyScroll);
    }

    // Function to create and setup search functionality for a search box
    function setupSearch(searchBoxId) {
        const searchBox = document.getElementById(searchBoxId);
        if (!searchBox) return;

        let searchResultsPanel = document.createElement('div');
        searchResultsPanel.className = 'search-results-panel';
        document.body.appendChild(searchResultsPanel);

        // Position the search results panel relative to the search box
        function positionSearchPanel() {
            const searchBoxRect = searchBox.getBoundingClientRect();
            searchResultsPanel.style.top = (searchBoxRect.bottom + window.scrollY) + 'px';

            // For the nav searchbox, position to the right
            if (searchBoxId === 'nav-searchbox') {
                searchResultsPanel.style.right = (window.innerWidth - searchBoxRect.right) + 'px';
                searchResultsPanel.style.left = '';
            } else {
                // For other searchboxes, position to match the left edge
                searchResultsPanel.style.left = searchBoxRect.left + 'px';
                searchResultsPanel.style.right = '';
            }
        }

        // Show/hide search results panel based on input
        searchBox.addEventListener('input', function () {
            const searchTerm = this.value.toLowerCase().trim();

            if (searchTerm === '') {
                searchResultsPanel.style.display = 'none';
                return;
            }

            // Position and show the panel
            positionSearchPanel();
            searchResultsPanel.style.display = 'block';

            // Disable scrolling and other interactions when panel is shown
            disableInteractions();

            // Filter pages based on search term
            const matchingPages = Object.entries(pages).filter(([command, data]) => {
                //return command.toLowerCase().includes(searchTerm);
                return command.toLowerCase().includes(searchTerm) || data.summary.toLowerCase().includes(searchTerm);
            });

            // Update search results panel
            if (matchingPages.length > 0) {
                searchResultsPanel.innerHTML = matchingPages.map(([command, data]) => {
                    return `
            <div class="search-result-item" data-command="${command}">
              <div class="search-result-command">${command}</div>
              <div class="search-result-summary">${data.summary}</div>
            </div>
          `;
                }).join('');

                // Add click event to search result items
                document.querySelectorAll('.search-result-item').forEach(item => {
                    item.addEventListener('click', function () {
                        const command = this.getAttribute('data-command');
                        window.location.href = `#${command}`;
                        searchResultsPanel.style.display = 'none';
                        searchBox.value = command;
                    });
                });
            } else {
                searchResultsPanel.innerHTML = '<div class="no-results">No matching commands found</div>';
            }
        });

        // Hide search results panel when clicking outside
        document.addEventListener('click', function (event) {
            if (event.target !== searchBox && !searchResultsPanel.contains(event.target)) {
                searchResultsPanel.style.display = 'none';
                // Re-enable scrolling and other interactions when panel is hidden
                enableInteractions();
            }
        });

        // Reposition search panel on window resize
        window.addEventListener('resize', function () {
            if (searchResultsPanel.style.display === 'block') {
                positionSearchPanel();
            }
        });

        // Handle keyboard navigation in search results
        searchBox.addEventListener('keydown', function (event) {
            // If the search term is empty, don't handle arrow keys
            if (this.value.trim() === '') return;

            // Check if we need to show the search results panel
            if ((event.key === 'ArrowDown' || event.key === 'ArrowUp') && searchResultsPanel.style.display !== 'block') {
                // Trigger the input event to show search results
                this.dispatchEvent(new Event('input'));
            }

            const items = document.querySelectorAll('.search-result-item');
            if (items.length === 0) return;

            const currentIndex = Array.from(items).findIndex(item => item.classList.contains('selected'));

            if (event.key === 'ArrowDown') {
                event.preventDefault();
                const nextIndex = currentIndex < 0 ? 0 : (currentIndex + 1) % items.length;
                items.forEach(item => item.classList.remove('selected'));
                items[nextIndex].classList.add('selected');
                items[nextIndex].scrollIntoView({ block: 'nearest' });
            } else if (event.key === 'ArrowUp') {
                event.preventDefault();
                const prevIndex = currentIndex < 0 ? items.length - 1 : (currentIndex - 1 + items.length) % items.length;
                items.forEach(item => item.classList.remove('selected'));
                items[prevIndex].classList.add('selected');
                items[prevIndex].scrollIntoView({ block: 'nearest' });
            } else if (event.key === 'Enter' && currentIndex >= 0) {
                event.preventDefault();
                items[currentIndex].click();
            } else if (event.key === 'Escape') {
                searchResultsPanel.style.display = 'none';
                // Re-enable scrolling and other interactions when panel is hidden
                enableInteractions();
            }
        });
    }

    // Setup search for both search boxes
    setupSearch('nav-searchbox');
    setupSearch('searchbox-2');
});
