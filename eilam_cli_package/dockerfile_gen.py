# Functions to generate Dockerfiles dynamically based on language/editor

def generate_dockerfile(image: str, version: str, editor: str) -> str:
    """
    Generate a Dockerfile string for the given image, version, and editor.
    """
    base_image = f"{image}:{version}"
    install_editor = f"RUN apt-get update && apt-get install -y {editor}"
    return f"""
FROM {base_image}
{install_editor}
WORKDIR /workspace
CMD [\"{editor}\"]
"""
