pasta_pdf="./data_collection/gazette/spiders/rj/data/3304557"

if [ ! -d "$pasta_pdf" ]; then 
    echo "A pasta nao existe."
    exit 1
fi

converter_pdf_para_txt(){
    local pasta="$1"
    if [ -d "$pasta" ]; then
        for item in "$pasta"/*; do 
            if [ -d "$item" ]; then
               converter_pdf_para_txt "$item" 
            elif [ "${item##*.}" ]; then 
                nome_arquivo_txt="./convertidos_txt/${item##*/}.txt"
                pdftotext "$item" "$nome_arquivo_txt"
                echo "Arquivo PDF convertido: $item"
                echo "Arquivo de texto gerado: $nome_arquivo_txt"
            fi
        done 
    fi 

}

if [ ! -d "$pasta_pdf" ]; then 
    echo "A pasta raiz nao existe."
    exit 1 
fi 

converter_pdf_para_txt "$pasta_pdf"

echo "Conversao concluida."