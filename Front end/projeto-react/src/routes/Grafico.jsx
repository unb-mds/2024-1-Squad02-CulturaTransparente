import React from 'react';
import { Link } from 'react-router-dom';
import Button_search from '../components/main_button/button_main';
import Chart from '../components/apexchart/chart_main';
import imagem from "../../assets/images/unb_image.png"; // Importe sua imagem aqui

const Grafico = () => {
    return (
        <div>
            <Button_search />
            <Chart />
            <p style={{ textAlign: 'center', marginTop: '20px', fontSize: '18px', fontFamily: 'Poppins', color: '#fff' }}>
                Projeto criado por alunos da Universidade de Brasília na disciplina de Métodos de Desenvolvimento de Software ensinada pela docente Carla Rocha.
            </p>
            <p style={{ textAlign: 'center', marginTop: '20px', fontSize: '14px', fontFamily: 'Poppins', color: '#fff' }}>
                Desenvolvido por: André Maia, Isabelle Costa, José Vinicius, Pedro Faria, Pedro Goiz, Enrico Zoratto e Mateu Cavalcante.
            </p>
            <img src={imagem} alt="Descrição da imagem" style={{ maxWidth: '10%', height: 'auto', display: 'block', margin: 'auto', marginTop: '20px' }} />
        </div>
    );
};

export default Grafico;
