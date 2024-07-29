import React, { useState, useEffect } from 'react';
import ApexCharts from 'react-apexcharts';
import jsonData from '../public/Nova Iguacu_2023_somas.json'; // Lembrar de mudar o path depois para a pasta do back-end (se tiver uma )

export default function Chart() {
    const [series, setSeries] = useState([]);
    const [loading, setLoading] = useState(true); // Adicionando um estado de carregamento

    useEffect(() => {
        // Simulando o fetch de dados do JSON importado
        console.log('Dados carregados do JSON:', jsonData);
        const transformedData = Object.values(jsonData).map(value => {
            const floatValue = parseFloat(value.replace(',', '.'));
            return isNaN(floatValue) ? 0 : floatValue; // Verifica se o valor é um número válido
        });
        console.log('Dados transformados:', transformedData);
        setSeries([{ name: 'Gastos', data: transformedData }]);
        setLoading(false); // Dados carregados, desativa o carregamento
    }, []);

    const options = {
        chart: {
            type: 'bar',
            height: 500,
            width: '95%',
            toolbar: {
                show: false
            }
        },
        plotOptions: {
            bar: {
                horizontal: false,
                distributed: true,
                barHeight: '80%',
            }
        },
        xaxis: {
            categories: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
            type: 'category',
            labels: {
                style: {
                    fontSize: '14px'
                }
            }
        },
        yaxis: {
            title: {
                text: 'Gastos (M de reais)',
                style: {
                    fontSize: '16px'
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
                left: 20,
                right: 20
            }
        },
        title: {
            text: 'Quantidade de investimento na área de cultura no município do Rio de Janeiro',
            align: 'center',
            margin: 10,
            style: {
                fontSize: '24px',
                fontWeight: 'bold',
                fontFamily: 'Poppins',
                color: '#fff'
            },
        },
    };

    if (loading) {
        return <div>Carregando...</div>; // Exibe uma mensagem de carregamento enquanto os dados estão sendo carregados
    }

    return (
        <ApexCharts
            options={options}
            series={series}
            type='bar'
            width='100%'
            height={500}
        />
    );
}
