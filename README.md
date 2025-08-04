# Eilam-CLI

A CLI tool to launch a Docker container for a chosen programming language and version, mounting a local path for code editing and execution.

## Project Structure

```
eilam_cli_package/
├── main.py            # Entry point: runs the CLI when you do `python -m eilam_cli_package`
├── cli.py             # Argument parsing and user interaction (Click)
├── docker_ops.py      # All Docker-related functions: building, running, cleaning up containers/images
├── dockerfile_gen.py  # Functions to generate Dockerfiles dynamically based on language/editor
├── config.py          # Central location for config, constants, and validation logic
├── utils.py           # Helper utilities (logging, hashing for image tags, etc.)
├── requirements.txt   # Python dependencies (docker, click, etc.)
├── README.md          # Project overview, usage, and setup instructions
├── tests/
│   ├── __init__.py
│   └── test_dockerfile_gen.py   # Unit tests (Dockerfile generation logic)
```

## Installation

1. Install Python 3.7+
2. Install Docker
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the CLI with:

```sh
python -m eilam_cli_package --language python --version 3.10 --path /your/code/path --editor vim
```

- `--language`: Programming language (e.g., python)
- `--version`: Version of the language (e.g., 3.10)
- `--path`: Local path to mount into the container
- `--editor`: Editor to use inside the container (vim, nano)

## Testing

To run unit tests:

```sh
python -m unittest discover -s eilam_cli_package/tests
```
