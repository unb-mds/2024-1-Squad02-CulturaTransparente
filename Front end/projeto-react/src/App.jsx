import { useRef, useState } from "react"
import { Container } from "./styles"
import logo from "./imagens/logo-mono2.png"
import redbox from "./imagens/redbox.png"

function App() {
  const [count, setCount] = useState(0)
  return (
    <div>
      <Container className="inicio">
        <img src={logo} alt="logo" />
        <button className="b1">Sobre</button>
        <button className="b2">Licitações</button>
        <button className="b3">Equipe</button>
      </Container>
    </div>

  )
}

export default App
