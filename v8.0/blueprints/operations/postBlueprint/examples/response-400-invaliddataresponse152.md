INVALID_DATA error for invalid data in the name field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 50,
        "json_path": "$.blueprints[*].transitions[*].include_states[*].state.name"
      },
      "status": "error"
    }
  ]
}
```
