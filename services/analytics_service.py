"""Basic analytics functions for the Eco Data SP MVP."""
from typing import Iterable


def percentage_change(previous: float, current: float) -> float | None:
    if previous == 0:
        return None
    return ((current - previous) / previous) * 100


def average(values: Iterable[float]) -> float:
    items = list(values)
    return sum(items) / len(items) if items else 0.0
