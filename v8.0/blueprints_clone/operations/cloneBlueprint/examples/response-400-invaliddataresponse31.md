INVALID_DATA error for an invalid clone_state object data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "clone_state",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].map_states[*].clone_state"
      },
      "status": "error"
    }
  ]
}
```
