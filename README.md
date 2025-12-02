# Screen AI

Screen AI is a tool that analyzes images using Ollama's vision models to extract text (OCR) e.g. to identify potential errors or anomalies.

## Features

- **OCR Analysis**: Extracts text from images while preserving formatting
- **Error Detection**: Reviews extracted text for mistakes and anomalies  
- **Interactive Chat**: Ask follow-up questions about the analyzed image
- **Dual Interface**: Both command-line and GUI versions available
- **Configurable**: Customizable server settings and prompts

## Applications

### `screen-ai-console`
Command-line interface for terminal-based image analysis with interactive chat.

### `screen-ai-gui` 
Graphical interface with split-pane view showing the image and chat side-by-side.

## Installation

1. Install dependencies (or go with your distribution packages):
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure Ollama server is running on your LLM host with a `vision` model that can work with images:
   ```bash
   ollama pull llama3.2-vision
   ollama pull granite3.2-vision
   ollama serve
   ```

## Configuration

Create `~/.screen-ai.conf` with your settings:

```python
OLLAMA_SERVER_URL = 'http://your_ollama_host:11434'
MODEL_NAME = 'granite3.2-vision'
INITIAL_PROMPT = """You are a QA and debug assistant. Your task is to analyze the provided image.

**Step 1: OCR**
First, extract all text from the image, preserving the original formatting as much as possible.

**Step 2: Analysis**
Review the extracted text for any mistakes, errors, or anomalies.

**Step 3: Reporting**
- If you find any errors, describe them clearly.
- If you find no errors, simply respond with exactly one sentence summary.

Do not include any other commentary or introductory phrases."""
```

## Usage

### Console Version
```bash
# Basic usage
./screen-ai-console --image screenshot.png

# With custom config
./screen-ai-console -i image.jpg -c /path/to/config

# With debug output
./screen-ai-console -i image.png --debug
```

### GUI Version
```bash
# Basic usage
./screen-ai-gui --image screenshot.png

# With custom config and debug
./screen-ai-gui -i image.jpg -c /path/to/config --debug
```

## Command Line Options

Both applications support:

- `--image, -i`: Path to image file (required)
- `--config, -c`: Path to config file (default: `~/.screen-ai.conf`)
- `--debug, -d`: Enable debug output (GUI only)
- `--help, -h`: Show help message

## Interactive Features

- **Console**: Type follow-up questions or 'exit'/'quit' to end
- **GUI**: Use the chat input field, arrow keys for command history
- **Image Context**: Follow-up questions maintain visual context of the original image

## Requirements

- Python 3.7+
- PySide6 (for GUI)
- ollama
- Running Ollama server with vision model

## File Structure

```
screen-ai/
├── screen-ai-console     # CLI application
├── screen-ai-gui         # GUI application  
├── config_loader.py      # Configuration loader
├── requirements.txt      # Python dependencies
└── README.md            # This file
```
