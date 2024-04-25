import { Container } from "../licitacoes/licitacoes"
import licitacoes from "../licitacoes/Licitacoes.png"

const Licitacoes = () => {
    return (
        <div>
            <Container className="inicio">
                <img src={licitacoes} alt="logo" />
            </Container>
        </div>
    )
}

export default Licitacoes;
