from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    render_json_logs: bool = False
    path: Path | None = None
    level: str = "DEBUG"
