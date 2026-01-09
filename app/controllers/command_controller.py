from services.ai_service import AIService
from security.command_guard import CommandGuard

class CommandController:
    def __init__(self):
        self.ai_service = AIService()
        self.guard = CommandGuard()

    def handle(self, user_input: str):
        suggestion = self.ai_service.generate_command(user_input)

        if not self.guard.is_safe(suggestion.command):
            print("⚠️ Comando bloqueado por segurança.")
            return

        print("\n💡 Sugestão de comando:\n")
        print(f"$ {suggestion.command}")
        print(f"\n📖 Explicação:\n{suggestion.explanation}\n")
