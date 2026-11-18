INVALID_DATA error: Invalid data type (Field: name)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].chart_data.connections[*].transition.name"
      },
      "status": "error"
    }
  ]
}
```
