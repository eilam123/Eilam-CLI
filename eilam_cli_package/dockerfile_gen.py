# Functions to generate Dockerfiles dynamically based on language/editor

def generate_dockerfile(language: str, version: str, editor: str) -> str:
    """
    Generate a Dockerfile string for the given language, version, and editor.
    """
    if language == "python":
        base_image = f"python:{version}"
        install_editor = f"RUN apt-get update && apt-get install -y {editor}"
        return f"""
FROM {base_image}
{install_editor}
WORKDIR /workspace
CMD [\"{editor}\"]
"""
    elif language == "node":
        base_image = f"node:{version}"
        install_editor = f"RUN apt-get update && apt-get install -y {editor}"
        return f"""
FROM {base_image}
{install_editor}
WORKDIR /workspace
CMD [\"{editor}\"]
"""
    elif language == "java":
        base_image = f"openjdk:{version}"
        install_editor = f"RUN apt-get update && apt-get install -y {editor}"
        return f"""
FROM {base_image}
{install_editor}
WORKDIR /workspace
CMD [\"{editor}\"]
"""
    # Add more languages as needed
    raise ValueError(f"Unsupported language: {language}")
