from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila


# fila_test = FilaNormal()
# fila_test.atualiza_fila()
# fila_test.atualiza_fila()
# fila_test.atualiza_fila()
# print(fila_test.chama_cliente(5))
# print(fila_test.chama_cliente(2))

# fila_test_2 = FilaPrioritaria()
# fila_test_2.atualiza_fila()
# fila_test_2.atualiza_fila()
# fila_test_2.atualiza_fila()
# print(fila_test_2.chama_cliente(10))
# print(fila_test_2.chama_cliente(1))
# print(fila_test_2.estatisca("21/08/2021", 196, "detail"))

teste_fabrica = FabricaFila.escolhe_fila("normal")
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
