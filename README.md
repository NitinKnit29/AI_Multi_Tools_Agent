# AI Agent Assistant

A production-ready Streamlit-based AI assistant with FastAPI backend, powered by Llama 3.2 and LangChain.

## Features

- **Web Search**: Search the internet for current events, facts, and up-to-date information using DuckDuckGo.
- **Calculator**: Perform mathematical calculations with support for expressions and percentage conversions.
- **Weather**: Get current weather information for any city using OpenWeatherMap API.
- **Chat Interface**: Interactive chat UI with conversation history.
- **Microservices Architecture**: Separated backend (FastAPI) and UI (Streamlit) for scalability.

## Prerequisites

- Docker and Docker Compose
- OpenWeatherMap API key
- Ollama (for LLM inference)

## Ollama Installation

1. Download and install Ollama from https://ollama.com/download

2. Pull the Llama 3.2 model:
   ```bash
   ollama pull llama3.2
   ```

3. Verify installation:
   ```bash
   ollama list
   curl http://localhost:11434/api/tags
   ```

4. Ollama should be running on `http://localhost:11434`. If you get a port error, Ollama is already running.

> **Note**: When running the app via Docker, Ollama must be running on the **host machine** (not in a container). The Docker containers connect to the host's Ollama via `host.docker.internal`.

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd AI_Agent_Assistant
   ```

2. Create a `.env` file in the root directory:
   ```
   OPENWEATHER_API_KEY=your_openweathermap_api_key_here
   ```
   Get your API key from [OpenWeatherMap](https://openweathermap.org/api).

3. Ensure Ollama is running with the llama3.2 model (for local development):
   ```bash
   ollama pull llama3.2
   ollama serve
   ```

## Usage

### Local Development with Docker Compose

Run the entire stack:
```bash
docker-compose up --build
```

- Backend API will be available at http://localhost:8000
- UI will be available at http://localhost:8501

### Manual Development

1. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Run the backend:
   ```bash
   uvicorn src.main:app --host 0.0.0.0 --port 8000
   ```

3. In another terminal, install UI dependencies:
   ```bash
   cd ui
   pip install -r requirements.txt
   ```

4. Run the UI:
   ```bash
   streamlit run app.py
   ```

## Project Structure

- `backend/`: FastAPI backend service
  - `src/`: Source code
    - `main.py`: FastAPI application
    - `agent.py`: LangChain agent configuration
    - `tools.py`: Tool definitions
  - `requirements.txt`: Backend dependencies
  - `Dockerfile`: Backend Docker image
- `ui/`: Streamlit UI service
  - `app.py`: Streamlit application
  - `requirements.txt`: UI dependencies
  - `Dockerfile`: UI Docker image
- `docker-compose.yaml`: Multi-service Docker setup
- `.gitignore`: Git ignore rules

## API Endpoints

- `GET /ask_agent?query=<question>`: Ask the AI agent a question

## Contributing

Feel free to submit issues and pull requests.

## License

MIT License
