import os
import docker
import tempfile
from .dockerfile_gen import generate_dockerfile

class ContainerManager:
    def __init__(self):
        self.client = docker.from_env()

    def run_container(self, language, version, mount_path, editor):
        try:
            # Generate Dockerfile content
            dockerfile_content = generate_dockerfile(language, version, editor)
            # Create a temporary directory for the Dockerfile
            with tempfile.TemporaryDirectory() as tmpdir:
                dockerfile_path = os.path.join(tmpdir, "Dockerfile")
                with open(dockerfile_path, "w") as f:
                    f.write(dockerfile_content)
                image_tag = f"{language}:{version}-{editor}"
                # Build the image
                self.client.images.build(path=tmpdir, tag=image_tag)
                # Run the container with a shell (bash preferred, fallback to sh)
                shell = "/bin/bash"
                try:
                    # Test if bash exists in the image
                    test_container = self.client.containers.run(
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
