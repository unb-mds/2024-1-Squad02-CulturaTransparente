import logo from "../../../assets/images/Logo-cabecalho.png"
import { Container } from "../navbar/navbar"
import { NavBar } from "../navbar/navbar";



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
                top: 1500,
                behavior: 'smooth'
            });
        }
    };

    const scrollToFooter = () => {
        const Participantes = document.getElementById('Participantes');
        if (Participantes) {
            window.scrollTo({
                top: 2500,
                behavior: 'smooth'
            });
            Participantes.scroll
        }
    };
    return (
        <div>
            <Container className="inicio">
                <button id="logo2" className="b" onClick={scrollToTop}> <img src={logo} alt="logo" className="logo" /> </button>
                <NavBar>
                <button className="b1" onClick={scrollToSobre}>Sobre</button>
                <button className="b2" onClick={scrollToLicitacoes}>Informações</button>
                <button className="b3" onClick={scrollToFooter}>Equipe</button>
                <button className="b4">Licitações</button>
                </NavBar>
            </Container>
        </div>
    );
};

export default Navbar;