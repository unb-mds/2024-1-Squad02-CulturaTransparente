import logo from "../navbar/logo-mono2.png"
import { Container } from "../navbar/navbar"


const Navbar = () => {
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
export default Navbar;