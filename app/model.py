import os
from app.interfaces import ICorrector
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class Corrector(ICorrector):

    def __init__(self):
        self.historial: list[tuple[str, str]] = []
        self.client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

    def obtener_cantidad_errores(self, texto: str) -> int:
        try:
            for original, corregido in self.historial:
                if original == texto:
                    errores = sum(1 for o, c in zip(original.split(), corregido.split()) if o != c)
                    errores += abs(len(original.split()) - len(corregido.split()))
                    return errores

            resp = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=f"Cuenta la cantidad de errores ortográficos y gramaticales en el siguiente texto en español:\n\n{texto}",
                max_tokens=10,
                temperature=0
            )

            errores = int(resp.choices[0].text.strip())

            return errores
        except Exception as e:
            raise RuntimeError(f"Error al obtener la cantidad de errores: {e}")


    def corregir_ortografia(self, texto: str) -> str:
        try:
            for original, corregido in self.historial:
                if original == texto:
                    return corregido

            resp = self.client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=f"Corrige la ortografía y gramática del siguiente texto en español:\n\n{texto}",
                max_tokens=500,
                temperature=0
            )

            texto_corregido = resp.choices[0].text.strip()

            self.historial.append((texto, texto_corregido))

            return texto_corregido
        except Exception as e:
            raise RuntimeError(f"Error al corregir la ortografía: {e}")