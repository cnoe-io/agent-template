# ⚠️ Repo moved under [ai-platform-engineering](https://github.com/cnoe-io/ai-platform-engineering/tree/main/ai_platform_engineering/agents/template) ⚠️

# 🚀 Petstore AI Agent

[![Python](https://img.shields.io/badge/python-3.13%2B-blue?logo=python)](https://www.python.org/)
[![Poetry](https://img.shields.io/badge/poetry-2.1.1%2B-blueviolet?logo=python)](https://python-poetry.org/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)

[![Conventional Commits](https://github.com/cnoe-io/openapi-mcp-codegen/actions/workflows/conventional_commits.yml/badge.svg)](https://github.com/cnoe-io/openapi-mcp-codegen/actions/workflows/conventional_commits.yml)
[![Ruff Linter](https://github.com/cnoe-io/openapi-mcp-codegen/actions/workflows/ruff.yml/badge.svg)](https://github.com/cnoe-io/openapi-mcp-codegen/actions/workflows/ruff.yml)
[![Unit Tests](https://github.com/cnoe-io/agent-petstore/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/cnoe-io/agent-petstore/actions/workflows/unit-tests.yml)

[![A2A Docker Build and Push](https://github.com/cnoe-io/agent-petstore/actions/workflows/a2a-docker-build.yml/badge.svg)](https://github.com/cnoe-io/agent-petstore/actions/workflows/a2a-docker-build.yml)
---

## 🧪 Evaluation Badges

| Claude | Gemini | OpenAI | Llama |
|--------|--------|--------|-------|
| [![Claude Evals](https://github.com/cnoe-io/agent-petstore/actions/workflows/claude-evals.yml/badge.svg)](https://github.com/cnoe-io/agent-petstore/actions/workflows/claude-evals.yml) | [![Gemini Evals](https://github.com/cnoe-io/agent-petstore/actions/workflows/gemini-evals.yml/badge.svg)](https://github.com/cnoe-io/agent-petstore/actions/workflows/gemini-evals.yml) | [![OpenAI Evals](https://github.com/cnoe-io/agent-petstore/actions/workflows/openai-evals.yml/badge.svg)](https://github.com/cnoe-io/agent-petstore/actions/workflows/openai-evals.yml) | [![Llama Evals](https://github.com/cnoe-io/agent-petstore/actions/workflows/openai-evals.yml/badge.svg)](https://github.com/cnoe-io/agent-petstore/actions/workflows/openai-evals.yml) |

---

- 🤖 **Petstore Agent** is an LLM-powered agent built using the [LangGraph ReAct Agent](https://langchain-ai.github.io/langgraph/agents/agents/) workflow and [MCP tools](https://modelcontextprotocol.io/introduction).
- 🌐 **Protocol Support:** Compatible with [A2A](https://github.com/google/A2A) protocol for integration with external user clients.
- 🛡️ **Secure by Design:** Enforces API token-based authentication and supports external authentication for strong access control.
- 🔌 **Integrated Communication:** Uses [langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters) to connect with the Petstore MCP server within the LangGraph ReAct Agent workflow.
- 🏭 **First-Party MCP Server:** The MCP server is generated by our first-party [openapi-mcp-codegen](https://github.com/cnoe-io/openapi-mcp-codegen/tree/main) utility, ensuring version/API compatibility and software supply chain integrity.

---
## 🚀 Getting Started

Running it via Docker:

### 1️⃣ Configure Environment

Ensure your `.env` file is set up as follows:

```env
############################
# Agent Configuration
############################
LLM_PROVIDER=azure-openai
AGENT_NAME=petstore

############################
# Azure OpenAI Configuration
############################
AZURE_OPENAI_API_KEY=""
OPENAI_API_VERSION=2025-04-01-preview
AZURE_OPENAI_API_VERSION=2025-04-01-preview
AZURE_OPENAI_DEPLOYMENT=gpt-4.1
AZURE_OPENAI_ENDPOINT=https://platform-interns-eus2.openai.azure.com/

############################
# MCP Server Configuration
############################
# These are set by default:
MCP_API_URL=https://petstore.swagger.io/v2
MCP_API_KEY=special-key
```

### 2️⃣ Start the Agent (A2A Mode)

1. Pull the A2A image:

```bash
docker pull ghcr.io/cnoe-io/agent-petstore:a2a-latest
```

2. Run the agent in a Docker container using your `.env` file:

```bash
docker pull ghcr.io/cnoe-io/agent-petstore:a2a-latest && \
docker run --rm -p 0.0.0.0:8000:8000 -it \
  -v $(pwd)/.env:/app/.env \
  ghcr.io/cnoe-io/agent-petstore:a2a-latest
```

### 3️⃣ Run the Client

Use the [agent-chat-cli](https://github.com/cnoe-io/agent-chat-cli) to interact with the agent:

```bash
uvx https://github.com/cnoe-io/agent-chat-cli.git a2a
```

---

## 🏗️ Architecture

```mermaid
flowchart TD
  subgraph Client Layer
    A[User Client A2A]
  end

  subgraph Agent Transport Layer
    B[Google A2A]
  end

  subgraph Agent Graph Layer
    C[LangGraph ReAct Agent]
  end

  subgraph Tools/MCP Layer
    D[Langchain MCP Adapter]
    E[Petstore MCP Server]
    F[Petstore API Server]
  end

  A --> B --> C
  C --> D
  D -.-> C
  D --> E --> F --> E
```

## ✨ Features

- 🤖 **LangGraph + LangChain MCP Adapter** for agent orchestration
- 🧠 **Azure OpenAI GPT-4** as the LLM backend
- 🔗 Connects to Petstore via a dedicated Petstore MCP agent
- 🔄 **A2A protocol support:** Compatible with **A2A** protocol for flexible integration and multi-agent orchestration
- 📊 **Comprehensive Petstore API Support:**
  - Pet Management (add, update, find, delete)
  - Store Management (inventory, order)
  - User Management (create, login, logout)

---

## Local Development

### Alternative: Running Locally
You can also run the agent locally without Docker:

First clone the repo

```bash
git clone https://github.com/cnoe-io/agent-template.git
cd agent-template
```

```bash
make run-a2a
```

In a new terminal, start the A2A client:
```bash
make run-a2a-client
```

## Quick Demos

### ▶️ Test with Petstore API

#### 🏃 Quick Start: Petstore Access

No authentication or account setup is required for the public Petstore API. The agent is preconfigured to use:
- `MCP_API_URL=https://petstore.swagger.io/v2`
- `MCP_API_KEY=special-key`

### Example Interactions

1. **Pet Management**
```
User: list all available pets
Agent: Here are the current available pets:

1. ID: 1 - Doggie
   Status: available
   Category: Dogs

2. ID: 2 - Kitty
   Status: available
   Category: Cats

Let me know if you need more details about any pet or would like to take action!
```

2. **Order Management**
```
User: place an order for pet ID 1
Agent: Order placed successfully for pet ID 1. Order ID: 1001
```

3. **User Management**
```
User: login as user1
Agent: Login successful for user1.
```

## 🔍 Troubleshooting

### Common Issues

1. **Docker Issues**
   - Ensure Docker daemon is running
   - Check if you have sufficient permissions
   - Verify the required images are available

2. **Port Conflicts**
   - If port 8000 is in use, modify `A2A_AGENT_PORT` in `.env`
   - Check for other services using required ports

3. **Environment Variables**
   - Verify all required variables in `.env`
   - No trailing spaces in values

4. **Client Connection Issues**
   - Server must be running before client
   - Port numbers should match

### Logs

- Docker: Use `docker logs <container-id>`
- Local: Check terminal output
- Debug mode: Set `DEBUG=true` in `.env`

## 📚 Documentation

For more detailed information about the project, please refer to:

- [API Documentation](docs/api.md) - Detailed API reference
- [Architecture Overview](docs/architecture.md) - System design and components
- [Development Guide](docs/development.md) - Setup and development workflow
- [Deployment Guide](docs/deployment.md) - Production deployment instructions
- [Contributing Guide](CONTRIBUTING.md) - How to contribute to the project
- [Security Policy](SECURITY.md) - Security practices and vulnerability reporting
- [License](LICENSE) - Project license details
- [Changelog](CHANGELOG.md) - Version history and changes
- [Code of Conduct](CODE_OF_CONDUCT.md) - Community guidelines

## 🔐 Security Notes

* Never commit your `.env` file to version control
* Keep your API keys and tokens secure
* Use environment variables or secret managers in production
* Regularly rotate your API keys and tokens

## 👥 Maintainers

See [MAINTAINERS.md](MAINTAINERS.md) for the list of maintainers.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on how to get started.

## 📄 License

Apache 2.0
