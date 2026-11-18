INVALID_DATA error for invalid data in the state field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "state",
        "maximum_length": 1,
        "json_path": "$.blueprints[*].transitions[*].include_states[*].state"
      },
      "status": "error"
    }
  ]
}
```
