#!/usr/bin/env python3
"""
AI Desktop Assistant - Main Entry Point
"""

import sys
import argparse
from src.interfaces.cli_interface import CLIInterface

def main():
    parser = argparse.ArgumentParser(description='AI Desktop Assistant')
    parser.add_argument('--interface', choices=['cli', 'gui', 'web'], 
                       default='cli', help='Interface to use')
    
    args = parser.parse_args()
    
    if args.interface == 'cli':
        assistant = CLIInterface()
        assistant.run()
    elif args.interface == 'gui':
        from src.interfaces.gui_interface import GUIInterface
        assistant = GUIInterface()
        assistant.run()
    elif args.interface == 'web':
        from src.interfaces.web_interface import WebInterface
        assistant = WebInterface()
        assistant.run()

if __name__ == '__main__':
    main()