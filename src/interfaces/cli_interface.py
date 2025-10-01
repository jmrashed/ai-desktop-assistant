from ..core.assistant_base import AssistantBase

class CLIInterface(AssistantBase):
    def __init__(self):
        super().__init__()
    
    def run(self):
        """Run CLI interface"""
        print("AI Desktop Assistant - CLI Mode")
        super().run()

def main():
    assistant = CLIInterface()
    assistant.run()

if __name__ == '__main__':
    main()