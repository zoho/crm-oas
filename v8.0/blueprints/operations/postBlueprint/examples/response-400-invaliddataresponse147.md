INVALID_DATA error for an invalid data type in the include_states field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "include_states",
        "expected_data_type": "jsonarray",
        "json_path": "$.blueprints[*].transitions[*].include_states"
      },
      "status": "error"
    }
  ]
}
```
