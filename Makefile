# Makefile

.PHONY: build setup-venv activate-venv install run run-acp run-client langgraph-dev help

setup-venv:
	@echo "Setting up virtual environment using venv..."
	@if [ ! -d "venv" ]; then \
		python3 -m venv venv; \
	fi
	@echo "Activating virtual environment and installing requirements..."
	. venv/bin/activate && poetry install

activate-venv:
	@echo "Activating virtual environment..."
	@if [ -d "venv" ]; then \
		. venv/bin/activate; \
	else \
		echo "Virtual environment not found. Please run 'make setup-venv' first."; \
	fi

build:
	poetry build

install:
	@echo "Installing the package..."
	. venv/bin/activate && poetry install

run: build install
	@echo "Running the application..."
	. venv/bin/activate && . .env && python3 -m agent_template

# Makefile snippet to run ACP deploy & log to workspace

run-acp: build install
	@LOGFILE="./logs/wfsm_deploy.log"; \
	echo "▶ Starting wfsm deploy — logging to $$LOGFILE"; \
	wfsm deploy -m ./deploy/acp/agent.json -e ./deploy/acp/agent-env.yaml 2>&1 | tee "$$LOGFILE"


run-client: build install
	@echo "Running the client…"
	. venv/bin/activate && \
	set -a && . .env && set +a && \
	export API_PORT="$$(sed -nE 's/.*127\.0\.0\.1:([0-9]+).*/\1/p' logs/wfsm_deploy.log | tail -1)" \
	       API_KEY="$$(sed -nE 's/.*API Key: ([0-9A-Za-z-]+).*/\1/p' logs/wfsm_deploy.log | tail -1)" \
	       AGENT_ID="$$(sed -nE 's/.*Agent ID: ([0-9A-Za-z-]+).*/\1/p' logs/wfsm_deploy.log | tail -1)" && \
	python3 client/client_agent_template.py


langgraph-dev: build install
	@echo "Running the LangGraph agent..."
	. venv/bin/activate && . .env && langgraph dev

help:
	@echo "Available targets:"
	@echo "  setup-venv       Create virtual environment in venv and install dependencies"
	@echo "  activate-venv    Activate the virtual environment"
	@echo "  build            Build the project using poetry"
	@echo "  install          Install the package"
	@echo "  run              Build, install, and run the application"
	@echo "  run-acp          Deploy using wfsm with ACP configuration"
	@echo "  run-client       Run the client application"
	@echo "  langgraph-dev    Run the LangGraph agent"
	@echo "  help             Show this help message"
