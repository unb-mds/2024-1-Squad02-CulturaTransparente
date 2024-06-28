import { Container } from "../licitacoes/licitacoes"
import licitacoes from "../../../assets/Licitações.png"

const Licitacoes = () => {
    return (
        <div id="Licitacoes">
            <Container className="inicio">
                <img src={licitacoes} alt="logo" />
            </Container>
        </div>
    )
}

export default Licitacoes;
