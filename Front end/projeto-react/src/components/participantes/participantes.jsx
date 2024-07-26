import styled from 'styled-components'

export const Container = styled.div` 
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: auto;
    margin-top: 1%;
    margin-bottom: 5vh;
    width: 60vw; 
    height: auto;
    padding-bottom: 10%;

    .titulo{
        font-weight: 700;
        font-size: 4rem;
        color: white;
        font-family: Poppins;
        padding-bottom: 5%;
    }

    .integrante-img {
        width: 300px;
        height: 400px;
        display: block;
    }
`
