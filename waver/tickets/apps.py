"""
Configure the app here
"""

from django.apps import AppConfig


class TicketsConfig(AppConfig):
    """
    Tickets app config
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "tickets"
