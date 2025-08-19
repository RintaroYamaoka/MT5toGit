from pathlib import Path
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox
)
from Service import ConverterService


class ConverterApp(QWidget):
    def __init__(self, service: ConverterService):
        super().__init__()
        self.service = service
        self.setWindowTitle("UTF-16 → UTF-8 変換ツール")

        self.source_edit = QLineEdit()
        self.dest_edit = QLineEdit()

        run_btn = QPushButton("実行")
        run_btn.clicked.connect(self.run_conversion)

        layout = QVBoxLayout(self)

        row1 = QHBoxLayout()
        row1.addWidget(QLabel("入力フォルダ:"))
        row1.addWidget(self.source_edit)

        row2 = QHBoxLayout()
        row2.addWidget(QLabel("出力フォルダ:"))
        row2.addWidget(self.dest_edit)

        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addWidget(run_btn)

    def run_conversion(self):
        # 空白・引用符
        src_text = self.source_edit.text().strip().strip('"').strip("'")
        dst_text = self.dest_edit.text().strip().strip('"').strip("'")

        # Path へそのまま渡す
        src = Path(src_text)
        dst = Path(dst_text)

        exts = [".mq5", ".mqh"]  # 固定拡張子

        try:
            count = self.service.convert(src, dst, exts)
            QMessageBox.information(self, "完了", f"変換が完了しました（{count} 件）。")
        except Exception as e:
            QMessageBox.critical(self, "エラー", f"処理に失敗しました:\n{e}")
