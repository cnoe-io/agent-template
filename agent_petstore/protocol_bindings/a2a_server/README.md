# Pet Store A2A Server

This directory contains the code for the A2A (Agent-to-Agent) protocol server implementation for the Pet Store agent.

## Key Components

- **__main__.py**: Entry point for starting the A2A server
- **agent_executor.py**: Handles the execution of agent tasks through the A2A protocol
- **helpers.py**: Utility functions for handling agent responses

## Usage

The A2A server can be started directly:

```bash
python -m agent_petstore.protocol_bindings.a2a_server --host localhost --port 8000
```

Or through the main agent entry point:

```bash
python -m agent_petstore --host localhost --port 8000
```
