import sys
from PySide6.QtWidgets import QApplication
from Repository import FileRepository
from Service import ConverterService
from GUI import ConverterApp


if __name__ == "__main__":
    repo = FileRepository()
    service = ConverterService(repo)

    app = QApplication(sys.argv)
    w = ConverterApp(service)
    w.resize(600, 120)
    w.show()
    sys.exit(app.exec())
