from typing import Dict, List, Union


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos) -> dict:
        estatistica: Dict[str, Union[List[str], int, str]] = {}
        estatistica["dia"] = self.dia
        estatistica["agencia"] = self.agencia
        estatistica["clientes atendidos"] = clientes_atendidos
        estatistica["quantidade clientes atendidos"] = (
            len(clientes_atendidos)
        )
        return estatistica
