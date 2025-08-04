import os
import docker

class ContainerManager:
    def __init__(self):
        self.client = docker.from_env()

    def run_container(self, image, mount_path, editor):
        try:
            self.client.images.pull(image)
            container = self.client.containers.run(
                image,
                command=editor,
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

