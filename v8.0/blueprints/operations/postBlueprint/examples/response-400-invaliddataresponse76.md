INVALID_DATA error for a non-object transition value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "transition",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].chart_data.connections[*].transition"
      },
      "status": "error"
    }
  ]
}
```
