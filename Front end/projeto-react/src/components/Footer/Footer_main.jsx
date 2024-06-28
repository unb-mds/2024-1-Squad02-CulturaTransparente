import { Container } from "./Footer"
import logo from "../../../assets/unb_image.png"
import logo2 from "../../../assets/FGA_artigos3x(1).png"
import github from "../../../assets/github.png"



function Footer() {
  return (
    <Container>
    <footer className="rodape">
        <ul className="rodape__lista">
            <li className="lista__link">
                <img src= {logo} alt="Logo UnB" className="img__ung img"/>
            </li>
            <li className="lista__link ancora">
                <img src= {github} alt="Logo github" className="img__github img"/><a href="https://github.com/unb-mds/2024-1-Squad02-CulturaTransparente" className="links">Cultura Transparente</a>
            </li>
            <li className="lista__link ancora">
                <img src={github} alt="Logo github" className="img__github img"/><a href="https://github.com/unb-mds" className="links">Métodos de desenvolvimento de software</a>
            </li>
            <li className="lista__link">
                <img src={logo2} alt="Logo FGA" className="img__fga img"/>
            </li>
        </ul>
    </footer>
    </Container>
  );
}

export default Footer;