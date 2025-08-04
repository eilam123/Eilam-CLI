import os
import docker
import tempfile
from .dockerfile_gen import generate_dockerfile


def run_container_docstring():
    pass

class ContainerManager:
    def __init__(self):
        self.client = docker.from_env()

    def run_container(self, image, version, mount_path, editor):
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
