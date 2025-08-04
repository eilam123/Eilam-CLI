# Eilam-CLI

A CLI tool to launch a Docker container for a chosen programming language and version, mounting a local path for code editing and execution.

## Project Structure

```
Eilam-CLI
├── __main__.py         # Entry point
├── cli.py              # Argument parsing and command routing
├── container.py        # Logic for running containers
├── utils.py            # Helper functions/constants
├── requirements.txt    # Python dependencies
├── README.md           # This file
```

## Installation

1. Install Python 3.7+
2. Install Docker
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the CLI with:

```
python -m Eilam-CLI --language python --version 3.10 --path /your/code/path --editor vim
```

- `--language`: Programming language (python, node, java, ...)
- `--version`: Version of the language (e.g., 3.10, 18, 17)
- `--path`: Local path to mount into the container
- `--editor`: Editor to use inside the container (vim, nano)

## Example

```
python -m Eilam-CLI --language python --version 3.10 --path C:\Users\Eilam\mycode --editor vim
```

## Notes
- Make sure Docker is running.
- The mounted path must exist on your system.
- You can extend supported languages and editors in `utils.py`.
