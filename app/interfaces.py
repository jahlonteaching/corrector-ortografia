from abc import ABC, abstractmethod


class ICorrector(ABC):

    @abstractmethod
    def corregir_ortografia(self, texto: str) -> str:
        """
        Este método recibe una cadena de texto y retorna la cadena con cualquier error de ortografía corregido
        :param texto: La cadena a corregir
        :return: El texto corregido
        """
        ...

    @abstractmethod
    def obtener_cantidad_errores(self, texto: str) -> int:
        """
        Este método recibe una cadena de texto y retorna un entero con la cantidad de errores ortográficos
        :param texto: La cadena a corregir
        :return: La cantidad de errores
        """
        ...
