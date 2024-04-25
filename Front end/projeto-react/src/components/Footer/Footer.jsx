import styled from 'styled-components'

export const Container = styled.div` 

    .rodape{
        background-color: #aaa399;
        height: 5em;
        margin: 5em 0 0 0;
    }

    .ancora{
        display: flex;
        align-items: center;
        gap: 0.7em;
    }
    .rodape__lista{
        display: flex;
        flex-direction: row;
        list-style-type: none;
        justify-content: space-between;
        align-items: center;
        
    }

    .links{
        color: black;
        text-decoration: none;
        font-family: sans-serif,NEWAKE;
        font-size: 1.2em;
        
    }

    .img{
        max-height: 4em;
        margin: 0.5em 0 0 0;
    }

    `