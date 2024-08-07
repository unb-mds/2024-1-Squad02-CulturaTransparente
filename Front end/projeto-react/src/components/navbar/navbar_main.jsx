import logo from "../../../assets/images/Logo-cabecalho.png";
import { Container } from "../navbar/navbar";
import Button_search from '../main_button/button_main';
import { NavBar, StyledLink } from "../navbar/navbar";

const Navbar = () => {
    const scrollToSobre = () => {
        const Sobre = document.getElementById('Sobre');
        if (Sobre) {
            window.scrollTo({
                top: 800,
                behavior: 'smooth'
            });
        }
    };
    const scrollToTop = () => {
        const logo2 = document.getElementById('logo2');

        logo2.addEventListener('click', function () {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        })
    };

    const scrollToLicitacoes = () => {
        const Licitacoes = document.getElementById('Licitacoes');
        if (Licitacoes) {
            window.scrollTo({
                top: 1750,
                behavior: 'smooth'
            });
        }
    };

    const scrollToFooter = () => {
        const Participantes = document.getElementById('Participantes');
        if (Participantes) {
            window.scrollTo({
                top: 2750,
                behavior: 'smooth'
            });
        }
    };

    return (
        <div>
            <Container className="inicio">
                <Button_search />
                <NavBar>
                    <button className="b1" onClick={scrollToSobre}>Sobre</button>
                    <button className="b2" onClick={scrollToLicitacoes}>Informações</button>
                    <StyledLink to="/integrantes" className="b3">Equipe</StyledLink>
                    <StyledLink to="/grafico" className="b4">Licitações</StyledLink>
                </NavBar>
            </Container>
        </div>
    );
};

export default Navbar;
