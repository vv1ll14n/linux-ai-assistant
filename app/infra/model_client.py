class ModelClient:
    def ask(self, text: str):
        text = text.lower()

        if "arquivo" in text and "grande" in text:
            return {
                "command": "du -ah . | sort -rh | head -n 10",
                "explanation": "Lista os 10 maiores arquivos e diretórios no diretório atual."
            }

        if "espaço" in text or "disco" in text:
            return {
                "command": "df -h",
                "explanation": "Mostra o uso de espaço em disco de forma legível."
            }

        if "processo" in text:
            return {
                "command": "ps aux --sort=-%mem | head",
                "explanation": "Lista os processos que mais consomem memória."
            }

        return {
            "command": "echo 'Não consegui entender a solicitação'",
            "explanation": "A frase informada ainda não está mapeada no MVP."
        }
