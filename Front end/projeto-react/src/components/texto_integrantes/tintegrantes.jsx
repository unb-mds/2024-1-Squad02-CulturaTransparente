import styled from 'styled-components'

export const Container = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .about_text_title{
        padding-top: 13%; 
        font-weight: 700;
        font-size: 2.5rem;
        color: white;
        font-family: Poppins;
        padding-bottom: 0;
    }

    .about_text{
        padding-top: 0; 
        font-weight: 300;
        font-size: 1rem;
        color: white;
        font-family: Poppins;
        text-align: center;
        max-width: 40%;
        padding-bottom: 16%;
    }

    
`