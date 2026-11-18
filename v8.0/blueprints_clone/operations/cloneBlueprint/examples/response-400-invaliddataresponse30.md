INVALID_DATA error for an invalid existing_state value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "actual_value",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].map_states[*].existing_state.actual_value"
      },
      "status": "error"
    }
  ]
}
```
