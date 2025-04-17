// Create a simple version of React's useState hook
function useState(initialValue) {
    let state = initialValue;
    const setState = (newValue) => {
        state = newValue;
        render();
    };
    return [state, setState];
}

// Matches component
function Matches(props) {
    const items = ["aaaaa", "abbbbbb", "acccccc", "bndddddd", "beeeeee", "cffffff", "gggggg", "hhhhhh", "iiiiii", "jjjjjj", "kkkkkk", "llllll", "mmmmmm", "nnnnnn", "oooooo", "pppppp", "qqqqqq", "rrrrrr", "ssssss", "tttttt", "uuuuuu", "vvvvvvv"];

    const name = props.name.toLowerCase().trim();
    if (name.length === 0) {
        return '';
    }

    let matches = items.filter(item => item.startsWith(name));
    if (matches.length === 0) {
        matches = items;
    }

    return matches.map(item => `<div>${item}</div>`).join('');
}

// Global state for the search input
let searchValue = '';

// Render function to update the UI
function render() {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
    <div style="border: solid">
      <div>
        <input type="text" id="search-input" value="${searchValue}" />
      </div>
      <div></div>
      <div id="matches-container">
        ${Matches({ name: searchValue })}
      </div>
      <div></div>
    </div>
  `;

    // Add event listener to the input
    const input = document.getElementById('search-input');
    if (input) {
        input.addEventListener('input', (e) => {
            searchValue = e.target.value;
            render();
        });
    }
}

// Store the container ID
let containerId = '';

// Create SearchBox function
function createSearchBox(id) {
    containerId = id;

    // Initialize the component
    document.addEventListener('DOMContentLoaded', () => {
        render();
    });

    // If the DOM is already loaded, render immediately
    if (document.readyState === 'complete' || document.readyState === 'interactive') {
        render();
    }
}

// Make the function available globally
window.createSearchBox = createSearchBox;
