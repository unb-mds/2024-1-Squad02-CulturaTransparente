import { Container } from "./sobre"
import sobre from "../../../assets/Sobre.png"


const Sobre = () => {
    return (
        <div id="Sobre">
            <Container className="inicio">
                <img src={sobre} alt="logo" />
            </Container>
        </div>
    )
}

export default Sobre;
