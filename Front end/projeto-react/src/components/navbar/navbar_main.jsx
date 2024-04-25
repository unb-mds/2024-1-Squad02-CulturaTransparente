import logo from "../navbar/logo-mono2.png"
import { Container } from "../navbar/navbar"
import React from 'react';
import Sobre from "../sobre/sobre_main";
import Licitacoes from "../licitacoes/licitacoes_main"
import Participantes from "../participantes/participantes_main"

const Navbar = () => {
    const scrollToSobre = () => {
        const Sobre = document.getElementById('Sobre');
        const NavbarHeight = 100;
        if (Sobre) {
            Sobre.scrollIntoView({ behavior: 'smooth' });
        }
    };

    const scrollToLicitacoes = () => {
        const Licitacoes = document.getElementById('Licitacoes');
        if (Licitacoes) {
            Licitacoes.scrollIntoView({ behavior: 'smooth' });
        }
    };

    const scrollToFooter = () => {
        const Participantes = document.getElementById('Participantes');
        if (Participantes) {
            Participantes.scrollIntoView({ behavior: 'smooth' });
        }
    };

    return (
        <div>
            <Container className="inicio">
                <img src={logo} alt="logo" />
                <button className="b1" onClick={scrollToSobre}>Sobre</button>
                <button className="b2" onClick={scrollToLicitacoes}>Licitações</button>
                <button className="b3" onClick={scrollToFooter}>Participantes</button>
            </Container>
        </div>
    );
};

export default Navbar;