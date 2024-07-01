import styled from 'styled-components';

export const Container = styled.div`
    display: flex;
    justify-content: flex-start; /* Alinha o botão à esquerda */
    align-items: center;
    background-color: #252424;
    height: 100px; /* Aumentar a altura */
    padding: 20px; /* Adicionar padding ao container */
    margin-top: 20px; /* Adicionar margem superior */

    button {
        margin-left: 10px; /* Adiciona uma pequena margem à esquerda */
        background: none; /* Remove o background padrão do botão */
        border: none; /* Remove a borda */
        padding: 0; /* Remove o padding interno */
        cursor: pointer; /* Adiciona um cursor pointer */

        .logo {
            height: 100%; /* Ajusta a altura da imagem para ocupar toda a altura do botão */
        }
    }
`;
