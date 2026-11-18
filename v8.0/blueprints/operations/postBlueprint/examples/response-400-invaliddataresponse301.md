INVALID_DATA error for an invalid to_state name data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].connections[*].to_state.name"
      },
      "status": "error"
    }
  ]
}
```
