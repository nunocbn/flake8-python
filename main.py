from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

# fila_test = FilaNormal()
# fila_test.atualizafila()
# fila_test.atualizafila()
# fila_test.atualizafila()
# print(fila_test.chamacliente(5))
# print(fila_test.chamacliente(2))

fila_test_2 = FilaPrioritaria()
fila_test_2.atualiza_fila()
fila_test_2.atualiza_fila()
fila_test_2.atualiza_fila()
print(fila_test_2.chama_cliente(10))
print(fila_test_2.chama_cliente(1))
print(fila_test_2.estatisca("21/08/2021", 198, "qualquer string"))