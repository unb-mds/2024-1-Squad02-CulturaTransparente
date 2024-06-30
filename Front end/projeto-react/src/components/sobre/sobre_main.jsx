import { Container, About } from "./sobre"
import image from "../../../assets/images/Group 11.png"
import text_box from "../../../assets/images/Group 12.png"


const Sobre = () => {
    return (
        <div id="Sobre">
            <Container className="inicio">
                <img src={image} alt="header" />
                <About>
                <img src = {text_box} alt = "text_box" className="text_box"/>
                <a className="about_text_title">Sobre</a>
                <a className="about_text">Cultura Transparente é uma inovadora ferramenta desenvolvida como parte do curso de Métodos de Desenvolvimento de Software, com o objetivo de simplificar e automatizar o processo de extração de dados de licitações publicadas no Diário Oficial do Estado do Rio de Janeiro. Este projeto surge como uma solução eficaz para profissionais, empresas e órgãos públicos que necessitam acompanhar licitações de maneira eficiente e oportuna.</a>
                </About>
            </Container>
        </div>
    )
}

export default Sobre;
