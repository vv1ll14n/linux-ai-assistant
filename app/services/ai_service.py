from domain.command_suggestion import CommandSuggestion
from infra.model_client import ModelClient

class AIService:
    def __init__(self):
        self.client = ModelClient()

    def generate_command(self, user_input: str) -> CommandSuggestion:
        response = self.client.ask(user_input)

        return CommandSuggestion(
            command=response["command"],
            explanation=response["explanation"]
        )
