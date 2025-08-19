from pathlib import Path


class FileRepository:
    def read_file(self, path: Path) -> str:
        # UTF-16 固定で読み込み
        return path.read_text(encoding="utf-16")

    def write_file(self, path: Path, content: str) -> None:
        # UTF-8 固定で保存
        path.write_text(content, encoding="utf-8")
