# Enterprise FastAPI Template

A modular, enterprise-ready FastAPI project template with best practices for configuration, logging, error handling, and testing.

## Features
- Modular app structure
- Environment variable management
- Logging and error handling
- Dependency injection
- Example GET and POST endpoints
- Pytest-based testing

## Quickstart
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the app:
   ```sh
   uvicorn app.main:app --reload
   ```
3. Visit [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API docs.

## Testing
```sh
pytest
```
