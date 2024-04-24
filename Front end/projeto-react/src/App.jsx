import { useRef, useState } from "react"
import Navbar from "./components/navbar/navbar_main"
import Title from "./components/title/title_main"

function App() {
  const [count, setCount] = useState(0)
  return (
    <div>
      <Navbar />
      <Title />
    </div>
  )
}

export default App
