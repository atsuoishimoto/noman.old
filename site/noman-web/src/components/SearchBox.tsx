import { useState } from 'react'

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
        <div style={{ border: "solid" }}>
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

export default SearchBox;
