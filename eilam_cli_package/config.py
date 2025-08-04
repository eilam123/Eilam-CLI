"""
Configuration and validation logic for Eilam-CLI.
Defines supported editors and provides validation functions.
"""

SUPPORTED_EDITORS = ["vim", "nano"]


def validate_editor(editor: str):
    """
    Validates that the provided editor is supported.

    Args:
        editor (str): The editor to validate.

    Raises:
        ValueError: If the editor is not supported.
    """
    if editor not in SUPPORTED_EDITORS:
        raise ValueError(f"Unsupported editor: {editor}")
