INVALID_DATA error: Invalid data type (Field: api_name)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].chart_data.connections[*].transition.api_name"
      },
      "status": "error"
    }
  ]
}
```
