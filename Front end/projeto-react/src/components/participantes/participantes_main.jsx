import { Container } from "../participantes/participantes"
import participantes from "../../../assets/images/Equipe.png"

const Participantes = () => {
    return (
        <div id="Participantes">
            <Container className="inicio">
                <img src={participantes} alt="logo" />
            </Container>
        </div>
    )
}

export default Participantes;
