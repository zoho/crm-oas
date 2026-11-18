INVALID_DATA error when the transition name value exceeds the maximum length

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
