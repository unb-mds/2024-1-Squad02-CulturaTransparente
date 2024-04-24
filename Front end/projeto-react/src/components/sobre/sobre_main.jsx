import { Container } from "../sobre/sobre"
import sobre from "../sobre/Sobre.png"

const Sobre = () => {
    return (
        <div>
            <Container className="inicio">
                <img src={sobre} alt="logo" />
            </Container>
        </div>
    )
}

export default Sobre;
