INVALID_DATA error for a transition exceeding the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "transition",
        "maximum_length": 1,
        "json_path": "$.blueprints[*].chart_data.connections[*].transition"
      },
      "status": "error"
    }
  ]
}
```
