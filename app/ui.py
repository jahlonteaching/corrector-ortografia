from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox
)
from PySide6.QtCore import Qt
from interfaces import ICorrector


class CorrectorDummy(ICorrector):
    """Implementación ficticia para pruebas"""
    def corregir_ortografia(self, texto: str) -> str:
        return texto.replace("ortogrfía", "ortografía").replace("exelente", "excelente")

    def obtener_cantidad_errores(self, texto: str) -> int:
        errores = ["ortogrfía", "exelente"]
        return sum(texto.count(palabra) for palabra in errores)


class CorrectorGUI(QWidget):
    def __init__(self, corrector: ICorrector):
        super().__init__()
        self.corrector = corrector
        self.setWindowTitle("Corrector de Ortografía")

        self.text_input = QTextEdit()
        self.result_label = QLabel("Texto corregido:")
        self.corrected_text = QTextEdit()
        self.corrected_text.setReadOnly(True)

        self.error_count_button = QPushButton("Contar errores")
        self.correct_button = QPushButton("Corregir texto")

        self.error_count_button.clicked.connect(self.mostrar_cantidad_errores)
        self.correct_button.clicked.connect(self.mostrar_texto_corregido)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Texto de entrada:"))
        layout.addWidget(self.text_input)
        layout.addWidget(self.error_count_button)
        layout.addWidget(self.correct_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.corrected_text)

        self.setLayout(layout)

    def mostrar_cantidad_errores(self):
        texto = self.text_input.toPlainText()
        cantidad = self.corrector.obtener_cantidad_errores(texto)
        QMessageBox.information(self, "Cantidad de errores", f"Errores encontrados: {cantidad}")

    def mostrar_texto_corregido(self):
        texto = self.text_input.toPlainText()
        texto_corregido = self.corrector.corregir_ortografia(texto)
        self.corrected_text.setText(texto_corregido)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    corrector = CorrectorDummy()  # Aquí puedes inyectar tu implementación real
    gui = CorrectorGUI(corrector)
    gui.resize(600, 500)
    gui.show()
    sys.exit(app.exec())
