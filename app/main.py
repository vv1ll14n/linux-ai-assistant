import sys
from controllers.command_controller import CommandController

def main():
    if len(sys.argv) < 2:
        print("Jarvis iniciado. Como posso ajudar?")
        sys.exit(1)

    user_input = " ".join(sys.argv[1:])
    controller = CommandController()
    controller.handle(user_input)

if __name__ == "__main__":
    main()

