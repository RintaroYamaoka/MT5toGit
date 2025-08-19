from pathlib import Path
from Repository import FileRepository


class ConverterService:
    def __init__(self, repository: FileRepository):
        self.repository = repository

    def collect_files(self, source: Path, extensions: list[str]) -> list[Path]:
        if not source.exists():
            raise FileNotFoundError(f"入力フォルダが存在しません: {source}")
        if not source.is_dir():
            raise NotADirectoryError(f"ディレクトリを指定してください: {source}")

        exts = {ext.strip().lower() for ext in extensions if ext.strip()}
        return [p for p in source.rglob("*") if p.is_file() and p.suffix.lower() in exts]

    def convert(self, source: Path, dest: Path, extensions: list[str]) -> int:
        files = self.collect_files(source, extensions)
        converted = 0
        for path in files:
            out = dest / path.relative_to(source)
            out.parent.mkdir(parents=True, exist_ok=True)
            content = self.repository.read_file(path)
            self.repository.write_file(out, content)
            converted += 1
        return converted
