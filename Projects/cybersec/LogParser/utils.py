from pathlib import Path


def get_log_path(filename: str) -> Path:
    return Path(__file__).parent / "sample_logs" / filename


def read_log_file(path: Path):
    with path.open("r") as file:
        return file.readlines()