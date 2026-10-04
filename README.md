# factorial

Arbitrary integer precision factorial API server running in Docker.

## API

- `GET /health` → health check
- `GET /factorial?n=<integer>` → factorial for non-negative integers

Example response:

```json
{
  "n": 20,
  "factorial": "2432902008176640000"
}
```

The `factorial` value is returned as a string to preserve precision for very large results.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

## Run tests

```bash
python -m unittest -v
```

## Run with Docker

```bash
docker build -t factorial-api .
docker run --rm -p 8000:8000 factorial-api
```
