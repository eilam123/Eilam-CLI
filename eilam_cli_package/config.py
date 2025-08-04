# Central location for config, constants, and validation logic

SUPPORTED_LANGUAGES = {
    "python": ["3.7", "3.8", "3.9", "3.10", "3.11"],
    "node": ["14", "16", "18", "20"],
    "java": ["8", "11", "17", "21"]
}

SUPPORTED_EDITORS = ["vim", "nano"]


def validate_language(language: str, version: str):
    if language not in SUPPORTED_LANGUAGES:
        raise ValueError(f"Unsupported language: {language}")
    if version not in SUPPORTED_LANGUAGES[language]:
        raise ValueError(f"Unsupported version {version} for language {language}")

def validate_editor(editor: str):
    if editor not in SUPPORTED_EDITORS:
        raise ValueError(f"Unsupported editor: {editor}")
