import { Container } from "../participantes/participantes";
import integrante1 from "../../../assets/images/Integrante 1.png";
import integrante2 from "../../../assets/images/Integrante 2.png";
import integrante3 from "../../../assets/images/Integrante 3.png";
import integrante4 from "../../../assets/images/Integrante 4.png";
import integrante5 from "../../../assets/images/Integrante 5.png";
import integrante6 from "../../../assets/images/Integrante 6.png";
import integrante7 from "../../../assets/images/Integrante 7.png";

const Participantes = () => {
    return (
        <div id="Participantes">
            <Container className="inicio">
                <div className="titulo">
                    <h2 className="titulo__texto">Nossa Equipe</h2>
                </div>
                <div style={{ display: 'flex', justifyContent: 'center', gap: '50px', marginBottom: '40px' }}>
                    <a href="https://github.com/andre-maia51" target="_blank" rel="noopener noreferrer">
                        <img src={integrante1} alt="Integrante 1" className="integrante-img" />
                    </a>
                    <a href="https://github.com/mateuscavati" target="_blank" rel="noopener noreferrer">
                        <img src={integrante2} alt="Integrante 2" className="integrante-img" />
                    </a>
                    <a href="https://github.com/Goizzz" target="_blank" rel="noopener noreferrer">
                        <img src={integrante3} alt="Integrante 3" className="integrante-img" />
                    </a>
                </div>
                <div style={{ display: 'flex', justifyContent: 'center', gap: '50px', marginBottom: '40px' }}>
                    <a href="https://github.com/isacostaf" target="_blank" rel="noopener noreferrer">
                        <img src={integrante4} alt="Integrante 4" className="integrante-img" />
                    </a>
                    <a href="https://github.com/JoseViniciusQueiroz" target="_blank" rel="noopener noreferrer">
                        <img src={integrante5} alt="Integrante 5" className="integrante-img" />
                    </a>
                    <a href="https://github.com/PhFariaa" target="_blank" rel="noopener noreferrer">
                        <img src={integrante6} alt="Integrante 6" className="integrante-img" />
                    </a>
                </div>
                <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '40px' }}>
                    <a href="https://github.com/sidts" target="_blank" rel="noopener noreferrer">
                        <img src={integrante7} alt="Integrante 7" className="integrante-img" />
                    </a>
                </div>
            </Container>
        </div>
    );
}

export default Participantes;
