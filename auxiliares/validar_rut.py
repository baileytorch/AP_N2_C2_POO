def validar_rut(rut):
    rut_limpio = rut.replace('.', '').replace('-', '')
    digito_verificador = rut_limpio[-1]
    numero_rut = rut_limpio[:-1]
    rut_inverso = rut_limpio[::-1]