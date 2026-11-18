INVALID_DATA error: invalid data in the api_name field (state)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].connections[*].from_state.api_name"
      },
      "status": "error"
    }
  ]
}
```
