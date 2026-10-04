# factorial
Arbitrary Integer Precision Factorial server.

## Run the server

```bash
python /home/runner/work/factorial/factorial/factorial_server.py
```

Server endpoint:

- `GET /factorial?n=<non-negative-integer>`
- Example response:

```json
{"n":"20","factorial":"2432902008176640000"}
```

## Run tests

```bash
python -m unittest -v /home/runner/work/factorial/factorial/test_factorial_server.py
```
