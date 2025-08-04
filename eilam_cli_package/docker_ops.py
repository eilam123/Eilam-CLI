"""
Docker operations for Eilam-CLI.
Handles building images from Dockerfiles and running containers with the specified configuration.
"""
import os
import docker
import tempfile
from .dockerfile_gen import generate_dockerfile


class ContainerManager:
    """
    Manages Docker container lifecycle: builds images, runs containers, and attaches to shells.
    """
    def __init__(self):
        """
        Initialize the Docker client from the environment.
        """
        self.client = docker.from_env()

    def run_container(self, image, version, mount_path, editor):
        """
        Build a Docker image using the specified base image, version, and editor, then run a container.
        The container mounts the given path and opens an interactive shell with the editor installed.

        Args:
            image (str): The base Docker image (e.g., 'python', 'node', 'openjdk').
            version (str): The version tag for the image (e.g., '3.10', '18', '17').
            mount_path (str): The local path to mount into the container at /workspace.
            editor (str): The text editor to install and make available in the container.
        """
        try:
            dockerfile_content = generate_dockerfile(image, version, editor)
            with tempfile.TemporaryDirectory() as tmpdir:
                dockerfile_path = os.path.join(tmpdir, "Dockerfile")
                with open(dockerfile_path, "w") as f:
                    f.write(dockerfile_content)
                image_tag = f"{image}:{version}-{editor}"
                self.client.images.build(path=tmpdir, tag=image_tag)
                shell = "/bin/bash"
                try:
                    self.client.containers.run(
                        image_tag,
                        command="which bash",
                        remove=True,
                        detach=False,
                        tty=True
                    )
                except Exception:
                    shell = "/bin/sh"
                container = self.client.containers.run(
                    image_tag,
                    command=shell,
                    volumes={os.path.abspath(mount_path): {'bind': '/workspace', 'mode': 'rw'}},
                    working_dir='/workspace',
                    tty=True,
                    stdin_open=True,
                    remove=True,
                    detach=True
                )
                os.system(f"docker attach {container.id}")
        except Exception as e:
            raise RuntimeError(f"Container error: {e}")
