import logo from "../navbar/Logo-cabecalho.png"
import { Container } from "../navbar/navbar"
import { Link } from "react-router-dom";


const Navbar = () => {
    const scrollToSobre = () => {
        const Sobre = document.getElementById('Sobre');
        if (Sobre) {
            window.scrollTo({
                top: 200,
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
                top: 1000,
                behavior: 'smooth'
            });
        }
    };

    const scrollToFooter = () => {
        const Participantes = document.getElementById('Participantes');
        if (Participantes) {
            window.scrollTo({
                top: 1800,
                behavior: 'smooth'
            });
            Participantes.scroll
        }
    };
    return (
        <div>
            <Container className="inicio">
                <button id="logo2" className="b" onClick={scrollToTop}> <img src={logo} alt="logo" className="logo" /> </button>
                <button className="b1" onClick={scrollToSobre}>Sobre</button>
                <button className="b2" onClick={scrollToLicitacoes}>Licitações</button>
                <button className="b3" onClick={scrollToFooter}>Participantes</button>
            </Container>
        </div>
    );
};

export default Navbar;