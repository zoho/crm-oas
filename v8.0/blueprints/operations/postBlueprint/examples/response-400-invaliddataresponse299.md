INVALID_DATA error for an invalid to_state data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "to_state",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].connections[*].to_state"
      },
      "status": "error"
    }
  ]
}
```
