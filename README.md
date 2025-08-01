# Enterprise FastAPI Template

This is a modular, enterprise-ready FastAPI project template that demonstrates best practices for scalable, maintainable, and extensible Python web APIs.

## Key Features
- **Layered Architecture**: Clear separation of concerns with routers, services, repositories (DAO), models, schemas, and integrations.
- **Abstract Factory Pattern for LLM**: Easily switch between different Large Language Model (LLM) providers (e.g., OLLAMA, Gemini) without changing business logic. All LLM logic is isolated in the `llm` package.
- **Environment-Specific Configuration**: Uses YAML config files for each environment (dev, prod, etc.), with a single `.env` to select the environment.
- **Database Integration**: Async SQLAlchemy setup for PostgreSQL, with repository pattern for all DB access. Example `Customer` entity and queries included.
- **Dependency Injection**: Clean, testable code using FastAPI's dependency injection system.
- **Error Handling & Logging**: Centralized, extensible error handling and logging setup.
- **Testing**: Pytest-based test structure for API and business logic.
- **Documentation**: All modules and methods are documented for clarity and maintainability.

## Project Structure
```
app/
  llm/           # LLM abstract factory, implementations, and factory logic
  models/        # ORM models (e.g., Customer)
  repositories/  # Data access layer (DAO)
  routers/       # FastAPI routers (API endpoints)
  schemas/       # Pydantic schemas for validation
  services/      # Business logic layer
  db.py          # Database session and engine setup
  main.py        # FastAPI app entry point
config/
  config-dev.yaml, config-prod.yaml  # Environment-specific configs
  settings.py     # Settings loader
tests/            # Pytest-based tests
.env              # Only contains ENV_NAME
.gitignore        # Ignores venv, .env, VS Code, etc.
```

## Quickstart
1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Set environment:**
   Create `.env` at parent location and set `ENV_NAME=dev` (or `prod`, etc.)
3. **Configure database:**
   Update the appropriate YAML config in `config/` with your DB connection string.
4. **Run the app:**
   ```sh
   uvicorn app.main:app --reload
   ```
5. **API docs:**
   Visit [http://localhost:8000/docs](http://localhost:8000/docs)

## Testing
```sh
pytest
```

## Extending the Template
- Add new LLM providers by implementing the `LLMBase` interface in `app/llm/` and updating the factory.
- Add new entities by creating models, schemas, repositories, and services.
- Add new endpoints by creating routers and connecting them to services.

## Git Integration
This project is git-ready with a `.gitignore` for Python, environments, and local config. Initialize your repo and push to GitHub as needed.
