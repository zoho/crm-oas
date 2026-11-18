INVALID_DATA error for an invalid existing_state object data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "existing_state",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].map_states[*].existing_state"
      },
      "status": "error"
    }
  ]
}
```
