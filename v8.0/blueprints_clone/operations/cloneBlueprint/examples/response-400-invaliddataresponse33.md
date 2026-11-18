INVALID_DATA error for an invalid clone_state value data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "actual_value",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].map_states[*].clone_state.actual_value"
      },
      "status": "error"
    }
  ]
}
```
