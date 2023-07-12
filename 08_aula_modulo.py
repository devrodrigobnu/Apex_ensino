# FUNCIONALIDADES DO math
    # ceil - Arredonda um número para cima
    # floor - Arredonda um número para baixo
    # trunc - Elimina virgula para frente
    # pow - Potência
    # sqrt - Raiz quadrada
    # factorial - Fatorial

# 'import math' -> importa todas as funcionalidades 'matematicas'
import math 
num = int(input('Digite um número: ')) 
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))

# 'from math import sqrt' -> importa apenas a raiz quadrada
from math import sqrt 
num = int(input('Digite um número: ')) 
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz)) # :.2f -> 2 casas decimais após a virgula






