# 🤖 Jarvis — Assistente Inteligente de Terminal para Linux (Ubuntu)

Jarvis é um **assistente inteligente de linha de comando**, inspirado no conceito de IA conversacional, que interpreta **linguagem natural** e sugere **comandos Linux seguros**, explicando exatamente o que cada comando faz antes de qualquer execução.

O projeto foi desenvolvido com foco em **boas práticas de arquitetura**, **segurança**, **IA local (offline)** e **qualidade para portfólio profissional**.

---

## ✨ Principais Funcionalidades

* 🧠 Interpretação de comandos em linguagem natural
* 💡 Sugestão de comandos Linux (Ubuntu)
* 📖 Explicação clara de cada comando sugerido
* 🔒 Camada de segurança contra comandos destrutivos
* 🤖 Integração com LLM local via **Ollama** (offline)
* 🧱 Arquitetura limpa e extensível (Clean Architecture)

---

## 📸 Exemplo de Uso

```bash
jarvis "listar arquivos grandes"
```

Saída:

```text
💡 Sugestão de comando:

$ du -ah . | sort -rh | head -n 10

📖 Explicação:
Lista os 10 maiores arquivos e diretórios no diretório atual.
```

---

## 🏗️ Arquitetura do Projeto

```text
CLI (Jarvis)
   ↓
Controller
   ↓
Service (IA)
   ↓
ModelClient
   ↓
Ollama (LLM local)
```

Separação clara de responsabilidades:

* **controllers** → fluxo da aplicação
* **services** → regras de negócio
* **infra** → integração com IA
* **security** → validação e bloqueio de comandos
* **domain** → modelos de domínio

---

## 📁 Estrutura de Pastas

```text
linux-ai-assistant/
│
├── app/
│   ├── main.py
│   ├── controllers/
│   ├── services/
│   ├── infra/
│   ├── security/
│   └── domain/
│
├── jarvis          # CLI executável
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Requisitos

* Ubuntu 20.04+
* Python 3.10+
* Git
* Ollama (LLM local)

---

## 🤖 Instalação do Ollama

O Ollama é tratado como **dependência de sistema** e **não é versionado no repositório**.

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Baixe um modelo recomendado:

```bash
ollama pull mistral
```

Teste:

```bash
ollama run mistral
```

---

## 🐍 Configuração do Projeto

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/linux-ai-assistant.git
cd linux-ai-assistant
```

Crie e ative o ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

---

## ▶️ Executando o Jarvis

Torne o launcher executável:

```bash
chmod +x jarvis
```

Crie o link global:

```bash
sudo ln -s ~/Projetos/linux-ai-assistant/jarvis /usr/local/bin/jarvis
```

Agora execute de qualquer lugar:

```bash
jarvis "ver espaço em disco"
```

---

## 🔒 Segurança

O Jarvis **não executa comandos automaticamente**.

Além disso, possui uma camada de proteção que bloqueia padrões perigosos como:

* `rm -rf /`
* `mkfs`
* `dd if=`
* fork bombs

Isso garante segurança mesmo com uso de IA.

---

## 🧠 Tecnologias Utilizadas

* Python 3
* Bash
* Ollama (LLM local)
* Mistral
* Git & GitHub

---

## 🚀 Roadmap

* [ ] Melhorar análise de segurança com regex avançado
* [ ] Adicionar testes unitários (pytest)
* [ ] Interface TUI (Textual / Rich)
* [ ] Contexto automático do sistema (versão do Ubuntu, disco, usuário)
* [ ] Histórico inteligente de comandos
* [ ] Entrada por voz

---

## 🎓 Motivação do Projeto

Este projeto foi desenvolvido com foco em:

* Aprendizado prático de **IA aplicada a sistemas operacionais**
* Criação de um **produto real para portfólio**
* Boas práticas de arquitetura e segurança

---

## 📄 Licença

MIT License

---

> 🤖 *Jarvis — tornando o terminal Linux mais inteligente e acessível.*
