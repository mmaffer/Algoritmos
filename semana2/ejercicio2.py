#Inveritr la cadena
def invertir_cadena(cadena):
    if len(cadena) == 0:  
        return cadena
    return cadena[-1] + invertir_cadena(cadena[:-1])  


texto = "Maria Fernanda Moya Condori"
resultado = invertir_cadena(texto)
print(resultado)