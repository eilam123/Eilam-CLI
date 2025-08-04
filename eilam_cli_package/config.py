# Central location for config, constants, and validation logic



SUPPORTED_EDITORS = ["vim", "nano"]


# Central location for config, constants, and validation logic

def validate_editor(editor: str):
    if editor not in SUPPORTED_EDITORS:
        raise ValueError(f"Unsupported editor: {editor}")
