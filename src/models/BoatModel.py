from dataclasses import dataclass
from typing import Optional


@dataclass
class BoatModel:
    plate: str
    foot: int = None
    price: float = None
