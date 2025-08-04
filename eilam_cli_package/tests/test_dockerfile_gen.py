# Unit tests for Dockerfile generation logic
import unittest
from eilam_cli_package.dockerfile_gen import generate_dockerfile

class TestDockerfileGen(unittest.TestCase):
    def test_python_vim(self):
        dockerfile = generate_dockerfile("python", "3.10", "vim")
        self.assertIn("FROM python:3.10", dockerfile)
        self.assertIn("apt-get install -y vim", dockerfile)
        self.assertIn("CMD [\"vim\"]", dockerfile)

    def test_node_nano(self):
        dockerfile = generate_dockerfile("node", "18", "nano")
        self.assertIn("FROM node:18", dockerfile)
        self.assertIn("apt-get install -y nano", dockerfile)
        self.assertIn("CMD [\"nano\"]", dockerfile)

    def test_java_vim(self):
        dockerfile = generate_dockerfile("java", "17", "vim")
        self.assertIn("FROM openjdk:17", dockerfile)
        self.assertIn("apt-get install -y vim", dockerfile)
        self.assertIn("CMD [\"vim\"]", dockerfile)

    def test_unsupported_language(self):
        with self.assertRaises(ValueError):
            generate_dockerfile("ruby", "3.0", "vim")

if __name__ == "__main__":
    unittest.main()
