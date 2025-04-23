from app.interfaces import ICorrector


class Corrector(ICorrector):

    def __init__(self):
        self.historial: list[tuple[str, str]] = []

    def obtener_cantidad_errores(self, texto: str) -> int:
        pass

    def corregir_ortografia(self, texto: str) -> str:
        pass