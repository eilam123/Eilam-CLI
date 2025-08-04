SUPPORTED_EDITORS = ["vim", "nano"]


def validate_editor(editor: str):
    if editor not in SUPPORTED_EDITORS:
        raise ValueError(f"Unsupported editor: {editor}")
