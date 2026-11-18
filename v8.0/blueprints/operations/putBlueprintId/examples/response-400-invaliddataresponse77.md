INVALID_DATA error: Invalid data (Field: name)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 100,
        "json_path": "$.blueprints[*].chart_data.connections[*].transition.name"
      },
      "status": "error"
    }
  ]
}
```
