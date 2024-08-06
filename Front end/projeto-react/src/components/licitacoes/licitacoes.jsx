import styled from 'styled-components'

export const Container = styled.div` 
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 80vh;

    .about_text_title{
        transform: translate(-70%, -520%);
        display: flex;
        justify-content: center;
        height: 110 px;
        font-family: Poppins;
        font-weight: 700;
        font-size: 73.61px;
        left: 430px;
        color: #1E503F;
    }

    .about_text{
        transform: translate(-55%, -220%);
        width: 520.63px;
        height: 273.01px;
        font-family: Poppins;
        font-weight: 400;
        font-size: 18.14px;
        left: 300px;
        color: #1E503F;
        text-align: justify;   
    }
    `