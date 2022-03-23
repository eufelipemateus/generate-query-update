

def format_cpf(cpf):
    Cpf = cpf.replace('.', '')
    return Cpf[0:9]+'-'+Cpf[len(Cpf)-2:len(Cpf)]