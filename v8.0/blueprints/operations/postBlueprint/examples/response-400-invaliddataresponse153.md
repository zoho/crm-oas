INVALID_DATA error for an invalid data type in the api_name field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "bigint",
        "json_path": "$.blueprints[*].transitions[*].include_states[*].state.api_name"
      },
      "status": "error"
    }
  ]
}
```
