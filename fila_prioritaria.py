from typing import Union

from constantes import CODIGO_PRIORITARIO
from fila_base import FilaBase
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada


Classes = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f"{CODIGO_PRIORITARIO}{self.codigo}"

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Cliente {cliente_atual} dirija-se ao Caixa {caixa}"

    def estatisca(self, retorna_estatistica: Classes) -> dict:
        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)
