#!/usr/bin/env python3
import os
from pathlib import Path

def load_config(config_path=None):
    """Load configuration from file"""
    if config_path is None:
        config_path = Path.home() / '.screen-ai.conf'
    else:
        config_path = Path(config_path)
    
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    # Load config file as Python module
    config_vars = {}
    with open(config_path, 'r') as f:
        exec(f.read(), config_vars)
    
    screenshot_cmd = config_vars.get('SCREENSHOT_COMMAND', 'spectacle -b -r -n -o /tmp/$FILENAME')
    return config_vars['OLLAMA_SERVER_URL'], config_vars['MODEL_NAME'], config_vars['INITIAL_PROMPT'], screenshot_cmd
