from dataclasses import dataclass
from enum import StrEnum
from datetime import datetime

from django.db import models
from django.core.validators import RegexValidator

"""
class Customer(models.Model):
    class StressLevel(models.TextChoices):
        LOW = "LOW", "Низький"
        MEDIUM = "MEDIUM", "Середній"
        HIGH = "HIGH", "Високий"

    full_name = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r".*\s+.*",
                message="Значення імені має містити хочаб один пробіл.",
            )
        ],
    )
    stress_level = models.CharField(
        max_length=12, choices=StressLevel.choices, default=StressLevel.LOW
    )
    total_clicks = models.PositiveIntegerField(default=0)
    average_clicking_speed = models.FloatField(default=0.0)
    last_activity = models.DateTimeField(auto_now=True)
"""


class StressLevel(StrEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass
class Customer:
    full_name: str
    stress_level: StressLevel = StressLevel.LOW
    total_clicks: int = 0
    average_clicking_speed: float = 0.0
    last_activity: datetime | None = None
