import { useRef, useState } from "react"
import { Container } from "./styles"
import logo from "./imagens/logo-mono2.png"
function App() {
  const [count, setCount] = useState(0)
  return (
    <div>
      <Container className="inicio">
        <img src={logo} alt="titulo" />
        <button>Sobre</button>
        <button>Licitações</button>
        <button>Equipe</button>
      </Container>
    </div>

  )
}

export default App
