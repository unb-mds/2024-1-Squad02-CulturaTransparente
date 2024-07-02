import imagem from '../../../assets/images/Group 10.png';
import { Container } from './inicial';
import { StyledLink } from "../navbar/navbar";

const Inicial = () => {
    return(
    <div className='div'>
        <Container>
        <img src={imagem} alt="initial_banner" classname="image"/>
        <a className='principal_text'>Transparência cultural ao <br/>alcance de um clique.</a>
        
        <StyledLink to="/grafico" className='button'>clique aqui</StyledLink>
        </Container>
    </div>       
    )
}

export default Inicial;