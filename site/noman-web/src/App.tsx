import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'


function Matches({ name }: { name: string }) {
  const items = ["aaaaa", "abbbbbb", "acccccc", "bndddddd", "beeeeee", "cffffff", "gggggg", "hhhhhh", "iiiiii", "jjjjjj", "kkkkkk", "llllll", "mmmmmm", "nnnnnn", "oooooo", "pppppp", "qqqqqq", "rrrrrr", "ssssss", "tttttt", "uuuuuu", "vvvvvvv"];

  name = name.toLowerCase().trim()
  if (name.length === 0) {
    return <div></div>
  }

  let matches = items.filter(item => item.startsWith(name))
  if (matches.length === 0) {
    matches = items
  }
  return (
    <div>
      {matches.map((item, index) => (
        <div key={index}>{item}</div>
      ))}
    </div>
  )
}

function SearchBox() {
  const [search, setSearch] = useState("");
  return (
    < div style={{ border: "solid" }}>
      <div>
        <input type="text" onChange={
          (e) => {
            setSearch(e.target.value);
          }
        } />
      </div>
      <div></div>
      <Matches name={search} />
      <div></div>
    </div>
  )
}

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <SearchBox />
      <div>
        <div>
        </div>
      </div>
      <a href="https://vite.dev" target="_blank">
        <img src={viteLogo} className="logo" alt="Vite logo" />
      </a>
      <a href="https://react.dev" target="_blank">
        <img src={reactLogo} className="logo react" alt="React logo" />
      </a>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
