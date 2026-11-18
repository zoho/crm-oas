INVALID_DATA error for a state api_name exceeding the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 7,
        "json_path": "$.blueprints[*].chart_data.connections[*].to.state.api_name"
      },
      "status": "error"
    }
  ]
}
```
