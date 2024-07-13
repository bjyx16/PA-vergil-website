#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""

    is_prod = 'WEBSITE_HOSTNAME' in os.environ
    print("is_prod:", is_prod)
    settings_module = "vergil.production" if is_prod else 'vergil.settings'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
