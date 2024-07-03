import styled from 'styled-components'

export const Container = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    

    .imagem{
        width: auto;
        height: 130vh;
    }

    .titulo{
        font-weight: 700;
        font-size: 4rem;
        color: white;
        font-family: Poppins;
        padding-bottom: 5%;
    }

    .equipe {
        display: grid;
        grid-template-columns: 300px 300px 300px;
        gap: 20px;

        .quadrado1 {
            background-color: purple;
            width: 281px;
            height: 387px;
            border-radius: 10%;
        }

        .nome1 {
            font-family: Poppins;
            text-align: center;
            margin-top: 30px;
            font-weight: 700;
            font-size: 26px;
        }

        .imagem1 {
            border-radius: 50%;
            width: 150px;
            height: 150px;
            align-items: center;
            margin: auto;
            margin-left: 70px;
            margin-top: 20px;
        }

        .github_png {
            width: 23px;
            height: 23px;
            margin-left: 70px;
            margin-top: 20px;
        }

        .githubname1 {
            font-family: Poppins;
            font-weight: 600;
            height: 25px;
            transform: translate(35%, -105%);
        }

        .function1 {
            font-family: Poppins;
            font-weight: 400;
            font-style: italic;
            font-size: 18px;
            transform: translate(30%, -105%);
        }

        .quadrado2 {
            background-color: yellow;
            width: 281px;
            height: 387px;
            border-radius: 10%;

        }
        .nome2{
            font-family: Poppins;
            text-align: center;
            margin-top: 30px;
            font-weight: 700;
            font-size: 26px;
        }

        .imagem2{
            border-radius: 50%;
            width: 150px;
            height: 150px;
            align-items: center;
            margin: auto;
            margin-left: 70px;
            margin-top: 20px;
        }

        .github_png{
            width: 23px;
            height: 23px;
            margin-left: 70px;
            margin-top: 20px;
        }

        .githubname2{
            font-family: Poppins;
            font-weight: 600;
            height: 25px;
            transform: translate(35%, -105%);
        }

        .function2{
            font-family: Poppins;
            font-weight: 400;
            font-style: italic;
            font-size: 18px;
            transform: translate(30%, -105%);
        }
    }
`





