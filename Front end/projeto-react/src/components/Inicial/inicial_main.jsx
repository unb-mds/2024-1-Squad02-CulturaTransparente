import imagem from '../../../assets/images/Group 10.png';
import { Container } from './inicial';

const Inicial = () => {
    return(
    <div className='div'>
        <Container>
        <img src={imagem} alt="initial_banner" classname="image"/>
        <a className='principal_text'>Transparência cultural ao <br/>alcance de um clique.</a>
        <button to="/grafico" className='button'>clique aqui</button>
        </Container>
    </div>       
    )
}

export default Inicial;