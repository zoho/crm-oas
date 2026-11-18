INVALID_DATA error for a non-text state api_name value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].chart_data.connections[*].to.state.api_name"
      },
      "status": "error"
    }
  ]
}
```
