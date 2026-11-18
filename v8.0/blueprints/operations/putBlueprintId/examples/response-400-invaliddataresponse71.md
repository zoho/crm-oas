INVALID_DATA error: Invalid data (Field: api_name)

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
