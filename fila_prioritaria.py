from constantes import CODIGO_PRIORITARIO
from fila_base import FilaBase


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f"{CODIGO_PRIORITARIO}{self.codigo}"

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Cliente {cliente_atual} dirija-se ao Caixa {caixa}"

    def estatisca(self, dia: str, agencia: int, flag: str) -> dict:
        if flag != "detail":
            estatistica = {f"{agencia}-{dia}": len(self.clientes_atendidos)}
        else:
            estatistica = {}
            estatistica["dia"] = dia
            estatistica["agencia"] = agencia
            estatistica["clientes atendidos"] = self.clientes_atendidos
            estatistica["quantidade clientes atendidos"] = (
                len(self.clientes_atendidos)
            )

        return estatistica
