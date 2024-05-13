#!/bin/bash

pasta_convertidos="./convertidos"
pasta_final="./arquivos_renomeados"

# Função para obter o nome do município a partir do código
obter_nome_municipio(){
    local codigo="$1"
    case "$codigo" in
        "3304557") echo "Rio_de_Janeiro" ;;
        "3303302") echo "Niteroi" ;;
        "3300258") echo "Arraial_do_Cabo" ;;
        "3300000") echo "Associacao_municipios" ;;
        "3300456") echo "Belford_Roxo" ;; 
        "3301009") echo "Campos_Goytacazes" ;;
        "3303500") echo "Nova_Iguacu" ;;
        "3305109") echo "Sao_Joao_de_Meriti" ;;
        # Adicione mais mapeamentos conforme necessário
        *) echo "Municipio_desconhecido" ;;
    esac
}

if [ ! -d "$pasta_convertidos" ]; then 
    echo "A pasta de convertidos não existe."
    exit 1
fi

mkdir -p "$pasta_final"

renomear_arquivos(){
    local pasta="$1"
    if [ -d "$pasta" ]; then
        for municipio_pasta in "$pasta"/*; do 
            if [ -d "$municipio_pasta" ]; then
                codigo_municipio=$(basename "$municipio_pasta")
                nome_municipio=$(obter_nome_municipio "$codigo_municipio")
                for data_pasta in "$municipio_pasta"/*; do
                    if [ -d "$data_pasta" ]; then
                        data=$(basename "$data_pasta")
                        for arquivo_txt in "$data_pasta"/*.txt; do
                           if [ -f "$arquivo_txt" ]; then
                                novo_nome="${nome_municipio}_${data}"
                                mv "$arquivo_txt" "$pasta_final/$novo_nome"
                                echo "Arquivo renomeado: $novo_nome"
                            fi
                        done
                    fi
                done
            fi 
        done 
    fi 
}

renomear_arquivos "$pasta_convertidos"

echo "Renomeação concluída."

