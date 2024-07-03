import { Container } from "./participantes.jsx"
import participantes from "../../../assets/images/Equipe.png"
import png_github from "../../../assets/images/github.png"

const Participantes = () => {
    return (
        <div id="Participantes">
            <Container className="inicio">
                <div className="titulo">
                    <h2 className="titulo__texto">Nossa Equipe</h2>
                </div>
                <div>
                    <img src={participantes}/>
                    <div className="equipe">
                        <div className='quadrado1'>
                            <p className="nome1">André <br/>Maia</p>
                            <a href="//github.com/andre-maia51" target="_blank">
                                <img className="imagem1" src="https://avatars.githubusercontent.com/u/76632983?v=4"/>
                            </a>
                            <br/>
                            <img className="github_png" src={png_github}/>
                            <p className='githubname1'>Andre-maia51</p>
                            <p className='function1'>Scrum Master</p>
                        </div>

                        <div className="quadrado2">
                            <p className="nome2">Mateus<br/>Cavalcante</p>
                            <a href="//github.com/mateuscavati" target="_blank">
                                <img className="imagem2" src="https://avatars.githubusercontent.com/u/117764744?v=4"/>
                            </a>
                            <br/>
                            <img className="github_png" src={png_github}/>
                            <p className='githubname2'>Mateuscavati</p>
                            <p className='function2'>Project Owner</p>
                        </div>

                    </div>
                </div>
            </Container>
        </div>
    )
}

export default Participantes;