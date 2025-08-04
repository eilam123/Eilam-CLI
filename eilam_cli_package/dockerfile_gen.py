"""
Dockerfile generation logic for Eilam-CLI.
Provides a function to dynamically create Dockerfiles for any base image, version, and editor.
"""

def generate_dockerfile(image: str, version: str, editor: str) -> str:
    """
    Generate a Dockerfile string for the given image, version, and editor.

    Args:
        image (str): The base Docker image (e.g., 'python', 'node', 'openjdk').
        version (str): The version tag for the image (e.g., '3.10', '18', '17').
        editor (str): The text editor to install in the image (e.g., 'vim', 'nano').
    Returns:
        str: The generated Dockerfile as a string.
    """
    base_image = f"{image}:{version}"
    install_editor = f"RUN apt-get update && apt-get install -y {editor}"
    return f"""
FROM {base_image}
{install_editor}
WORKDIR /workspace
CMD [\"{editor}\"]
"""
