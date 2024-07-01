import React from 'react';
import ApexCharts from 'react-apexcharts';

export default function Chart() {
    const options = {
        chart: {
            type: 'bar',
            height: 500, // Reduzindo um pouco a altura do gráfico
            width: '95%', // Utilizando 95% da largura disponível
            toolbar: {
                show: false // Oculta a barra de ferramentas do gráfico
            }
        },
        plotOptions: {
            bar: {
                horizontal: false,
                distributed: true, // Distribui as barras uniformemente
                barHeight: '80%', // Diminui o tamanho das barras
            }
        },
        xaxis: {
            categories: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
            type: 'category',
            labels: {
                style: {
                    fontSize: '14px' // Define o tamanho da fonte dos rótulos X
                }
            }
        },
        yaxis: {
            title: {
                text: 'Gastos (M de reais)',
                style: {
                    fontSize: '16px' // Define o tamanho da fonte do título Y
                }
            }
        },
        tooltip: {
            enabled: true,
            formatter: function (val) {
                return val + ' M';
            }
        },
        dataLabels: {
            formatter: function (val) {
                return val.toFixed(2) + ' M';
            }
        },
        colors: ['#FFCA00', '#874FD4', '#64BA8B', '#FFCA00', '#874FD4', '#64BA8B', '#FFCA00', '#874FD4', '#64BA8B', '#FFCA00', '#874FD4', '#64BA8B'],
        grid: {
            padding: {
                left: 20, // Adiciona margem à esquerda do gráfico
                right: 20 // Adiciona margem à direita do gráfico
            }
        },
        title: {
            text: 'Quantidade de investimento na área de cultura no município do Rio de Janeiro',
            align: 'center',
            margin: 10,
            style: {
                fontSize: '24px', // Aumenta o tamanho da fonte do título
                fontWeight: 'bold', // Define o peso da fonte do título
                fontFamily: 'Poppins', // Define a fonte do título
                color: '#fff' // Define a cor do título (branco)
            },
        },
    };

    const series = [{
        name: 'Gastos',
        data: [2.3, 3.1, 4.0, 10.1, 4.0, 3.6, 3.2, 2.3, 1.4, 0.8, 0.5, 0.2]
    }];

    return (
        <ApexCharts
            options={options}
            series={series}
            type='bar'
            width='100%' // Utilizando toda a largura disponível
            height={500} // Reduzindo um pouco a altura do gráfico
        />
    );
}
