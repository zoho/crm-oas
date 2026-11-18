INVALID_DATA error for invalid data in the include_states field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "include_states",
        "maximum_length": 1,
        "json_path": "$.blueprints[*].transitions[*].include_states"
      },
      "status": "error"
    }
  ]
}
```
