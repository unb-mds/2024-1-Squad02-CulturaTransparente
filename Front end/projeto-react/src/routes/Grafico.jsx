import React from 'react';
import { Link } from 'react-router-dom';
import logo from "../../assets/images/Logo-cabecalho.png";
import Button_search from '../components/main_button/button_main';
import Chart from '../components/apexchart/chart_main';
const Grafico = () => {
    return (
        <div>
            <Button_search />
            <Chart />
        </div>
    );
};

export default Grafico;
