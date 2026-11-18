INVALID_DATA error: invalid data in the name field (state)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].connections[*].from_state.name"
      },
      "status": "error"
    }
  ]
}
```
