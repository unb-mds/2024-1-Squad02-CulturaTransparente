def formatar(valor):
    partes = f"{valor:,.2f}".split(".")
    parte_inteira = partes[0].replace(",", ".")
    parte_decimal = partes[1]
    return f"{parte_inteira}.{parte_decimal}"
