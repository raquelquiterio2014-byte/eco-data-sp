"""Simple deterministic alert rules for the MVP."""


def variation_alert(previous: float, current: float, threshold_percent: float = 15.0) -> str | None:
    if previous <= 0:
        return None
    change = ((current - previous) / previous) * 100
    if change >= threshold_percent:
        return f"Consumption increased by {change:.1f}%."
    return None
