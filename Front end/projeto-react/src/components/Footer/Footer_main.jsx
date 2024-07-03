import { Container } from "./Footer"
import imagem from "../../../assets/images/unb_image.png";



function Footer() {
  return (
    <Container>
        <footer>
            <p style={{ textAlign: 'center', marginTop: '20px', fontSize: '18px', fontFamily: 'Poppins', color: '#fff' }}>
            Projeto criado por alunos da Universidade de Brasília na disciplina de Métodos de Desenvolvimento de Software ensinada pela docente Carla Rocha.
            </p>
            <p style={{ textAlign: 'center', marginTop: '20px', fontSize: '14px', fontFamily: 'Poppins', color: '#fff' }}>
            Desenvolvido por: André Maia, Isabelle Costa, José Vinicius, Pedro Faria, Pedro Goiz, Enrico Zoratto e Mateus Cavalcante.
            </p>
            <img src={imagem} alt="Descrição da imagem" style={{ maxWidth: '10%', height: 'auto', display: 'block', margin: 'auto', marginTop: '20px' }} />
            <br/>
        </footer>
    </Container>
  );
}

export default Footer;