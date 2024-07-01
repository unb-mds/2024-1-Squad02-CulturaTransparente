import styled from "styled-components";

export const Container = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    @media (max-width: 768px) {
        margin: 32px;
    }

    @media (max-width: 480px) {
        .principal_text {
            font-size: 24px;
        }

        .button {
            margin: auto;
            font-size: 20px;
            line-height: 30px;
            
        }
    }

    .image {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        position: relative;
        width: 100%;
        height: 100%;
        padding-top: 20px;
    }

    .principal_text {
        font-size: 40px;
        weight: 400;
        text-align: center;
        height: 125px;
        font-family: Newake;
        transform: translate(-50%, -330%);
        color: #FFFFFF;
    }

    .button {
        transform: translate(-110%, -680%);
        cursor: pointer;
        margin: auto;
        height: 62px;
        border: none;
        color: #7A41C9;
        background-color: #FFCA00;
        font-family: Poppins;
        font-size: 27.07px;
        text-align: center;
        line-height: 40.61px;
        font-weight: 700;
        border-radius: 10px;
        width: 218px;
    }
`;