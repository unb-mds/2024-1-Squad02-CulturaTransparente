import { Container } from "../participantes/participantes"
import participantes from "../../../assets/images/Equipe.png"

const Participantes = () => {
    return (
        <div id="Participantes">
            <Container className="inicio">
                <div className="titulo">
                    <h2 className="titulo__texto">Nossa Equipe</h2>
                </div>
                <div>
                    <img src={participantes} alt="logo" />
                </div>
            </Container>
        </div>
    )
}

export default Participantes;
