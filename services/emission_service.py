"""Emission-estimation helpers. Factors are explicitly supplied by the caller."""


def estimate_co2e(activity_value: float, emission_factor: float) -> float:
    if activity_value < 0 or emission_factor < 0:
        raise ValueError("Activity values and emission factors must be non-negative.")
    return activity_value * emission_factor
