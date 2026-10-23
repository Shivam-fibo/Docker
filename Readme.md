# Python FastAPI Backend with Docker

A small FastAPI project for learning how to run a Python backend locally and inside Docker.

## Project Files

- `main.py` - Defines the FastAPI application and its API endpoints.
- `requirements.txt` - Lists the Python packages required to run the backend.
- `Dockerfile` - Contains the instructions Docker uses to build the application image.

## 1. Run Locally

Install Python, clone the repository, and open a terminal in the project directory.

### macOS / Linux

Create a virtual environment to keep this project's Python packages separate from other projects.

```bash
python3 -m venv .venv
```

Activate the virtual environment.

```bash
source .venv/bin/activate
```

Install FastAPI and Uvicorn from `requirements.txt`.

```bash
python -m pip install -r requirements.txt
```

Start the development server.

```bash
python -m uvicorn main:app --reload
```

### Windows PowerShell

Create a virtual environment for the project.

```powershell
python -m venv .venv
```

Activate the virtual environment in PowerShell.

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required packages.

```powershell
python -m pip install -r requirements.txt
```

Start the development server.

```powershell
python -m uvicorn main:app --reload
```

### Windows Git Bash

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment in Git Bash.

```bash
source .venv/Scripts/activate
```

Install the required packages.

```bash
python -m pip install -r requirements.txt
```

Start the development server.

```bash
python -m uvicorn main:app --reload
```

Once the server starts, open [http://localhost:8000/docs](http://localhost:8000/docs) to test the API. Press `Ctrl+C` in the terminal to stop the server.

## 2. Run with Docker

Install and start [Docker Desktop](https://www.docker.com/products/docker-desktop/) before running these commands from the project directory.

Build a Docker image named `python-task-api` from the `Dockerfile` in the current directory.

```bash
docker build -t python-task-api .
```

Create and start a container, publishing container port `8000` on your computer's port `8000`.

```bash
docker run --name python-task-container -p 8000:8000 python-task-api
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) to test the API. Press `Ctrl+C` in the terminal to stop the container.

## 3. Manage the Container

Start the existing stopped container and display its logs in the terminal.

```bash
docker start -a python-task-container
```

If you want to run the `docker run` command again and the old container name is already in use, remove the stopped container first.

```bash
docker rm python-task-container
```

## API Endpoints

- `GET /` - Returns a message confirming that the backend is running.
- `GET /tasks` - Returns the current list of tasks.
- `POST /tasks?title=Learn%20Docker` - Creates a task with the supplied title.
- `/docs` - Opens the interactive FastAPI documentation.
