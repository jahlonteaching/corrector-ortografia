from abc import ABC, abstractmethod


class ICorrector(ABC):

    @abstractmethod
    def corregir_ortografia(self, texto: str) -> str:
        ...

    @abstractmethod
    def obtener_cantidad_errores(self, texto: str) -> int:
        ...
