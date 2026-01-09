import subprocess
import json
import re

class ModelClient:
    def ask(self, user_input: str) -> dict:
        prompt = self._build_prompt(user_input)

        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()
        return self._parse_response(output)

    def _build_prompt(self, user_input: str) -> str:
        return f"""
Você é um assistente especialista em Linux Ubuntu.

Regras obrigatórias:
- Responda APENAS em JSON válido
- Não explique fora do JSON
- O comando deve ser seguro
- Não execute comandos destrutivos

Formato da resposta:
{{
  "command": "comando linux",
  "explanation": "explicação curta"
}}

Solicitação do usuário:
{user_input}
"""

    def _parse_response(self, text: str) -> dict:
        try:
            json_text = re.search(r"\{.*\}", text, re.DOTALL).group()
            return json.loads(json_text)
        except Exception:
            return {
                "command": "echo 'Erro ao interpretar resposta da IA'",
                "explanation": "A IA retornou um formato inesperado."
            }

