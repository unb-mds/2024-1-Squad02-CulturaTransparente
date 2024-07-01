import { Container } from "../participantes/participantes"
import participantes from "../../../assets/images/Equipe.png"

const Participantes = () => {
    return (
        <div id="Participantes">
            <div>
                <h2 className="titulo">Nossa Equipe</h2>
            </div>
            <Container className="inicio">
                <img src={participantes} alt="logo" />
            </Container>
        </div>
    )
}

export default Participantes;
