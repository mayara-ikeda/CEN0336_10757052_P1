# Importação de biblioteca
import sys

# A função vai verificar se os números são inteiros e menores que 500. Esta função está apenas sendo criada aqui.Ela será utilizada na etapa de verificação.
def verificador_de_string(value):
    return value.isdigit() and 0 < int(value) < 500

# Aqui o sys.argv funcionará como uma lista de armazenamento.
# A mensagem de erro está programada para aparecer quando o número de elementos da lista for diferente de 3
# Isto porque a lista precisa seguir este formato: [nome_do_arquivo.py, numero_1, numero_2], ou seja, precisa ter 3 elementos
if len(sys.argv) != 3:
    print("Erro: Forneça dois números inteiros positivos menores que 500.")
    sys.exit(1)

# Aqui o objeto "a_str" está recebendo o segundo valor da lista e o objeto "b_str" está recebendo o terceiro valor da lista do sys.argv
a_str = sys.argv[1]
b_str = sys.argv[2]

# Aqui está acontecendo a etapa de verificação. Note que a função "verificador_de_string" criada lá no início está sendo chamada aqui.
if not (verificador_de_string(a_str) and verificador_de_string(b_str)):
    print("Erro: Os valores devem ser inteiros positivos menores que 500.")
    sys.exit(1)

# Aqui os inputs estão sendo convertidos para inteiros e sendo atribuídos a novos objetos ("a" e "b")
a = int(a_str)
b = int(b_str)

# Nesta etapa, o cálculo da nipotenuda está sendo realizado de acordo com base nos valores de "a" e "b"
hipotenusa = a**2 + b**2

# Por fim, o resultado é impresso no terminal desta forma:
print(f"O quadrado da hipotenusa do triângulo retângulo com lados a={a} e b={b}, é {hipotenusa}")
