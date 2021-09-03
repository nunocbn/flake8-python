import abc
from typing import List

from constantes import QUANTIDADE_MAXIMA_SENHAS, QUANTIDADE_MINIMA_SENHAS


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    def reseta_fila(self) -> None:
        if self.codigo >= QUANTIDADE_MAXIMA_SENHAS:
            self.codigo = QUANTIDADE_MINIMA_SENHAS
        else:
            self.codigo += 1

    def insere_senha(self):
        self.fila.append(self.senha_atual)

    @abc.abstractmethod
    def gera_senha_atual(self):
        pass

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_senha()

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        pass
