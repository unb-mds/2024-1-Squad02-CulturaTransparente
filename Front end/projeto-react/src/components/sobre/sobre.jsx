import styled from 'styled-components'

export const Container = styled.div`
    position: relative;
    display: flex;
    margin-left: 250px;
    @media (max-width: 768px) {
        margin-left: 0;
        flex-direction: column;
        align-items: center;
    }

    @media (max-width: 992px) {
        margin-left: 150px;
    }
    `

export const About = styled.div`

    .text_box{
        margin-top: 32px;
        position: absolute;
        left: 600px;
        top: -100px;
        border-radius: 40.82px;
        border: 0.91px;
    }
        .about_text_title{
        position: absolute;
        margin-top: 32px;
        top: -25px;
        left: 631.75px;
        font-family: Poppins;
        font-weight: 700;
        font-size: 72.56px;
        color: #B27100
        }

        .about_text{
        position: absolute;
        margin-top: 32px;
        width: 520.63px;
        height: 273.01px;
        top: 72.05px;
        left: 631.75px;
        font-family: Poppins;
        font-weight: 400;
        font-size: 18.14px;
        color: #B27100;
        text-align: justify;
        }
    
    `