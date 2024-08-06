pasta_raiz="./data_collection/gazette/spiders/rj/data"

if [ ! -d "$pasta_raiz" ]; then 
    echo "A pasta raiz não existe."
    exit 1
fi

converter_pdf_para_txt(){
    local pasta="$1"
    if [ -d "$pasta" ]; then
        for subpasta in "$pasta"/*; do 
            if [ -d "$subpasta" ]; then
                for pdf_subpasta in "$subpasta"/*; do
                    if [ -d "$pdf_subpasta" ]; then
                        for pdf in "$pdf_subpasta"/*; do
                           if [ "${pdf##*.}" ]; then 
                                nome_arquivo_txt="../.gitignore/convertidos/$(basename "$subpasta")/$(basename "$pdf_subpasta")/${pdf##*/}.txt"
                                mkdir -p "$(dirname "$nome_arquivo_txt")"
                                pdftotext "$pdf" "$nome_arquivo_txt"
                                echo "Arquivo PDF convertido: $pdf"
                                echo "Arquivo de texto gerado: $nome_arquivo_txt" 
                                rm "$pdf"
                           fi
                            
                        done
                    fi
                done
            fi 
        done 
        rm -r "$pasta_raiz"
    fi 
}

converter_pdf_para_txt "$pasta_raiz"

echo "Conversão concluída."