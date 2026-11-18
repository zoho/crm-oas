Error response with code INVALID_DATA: Invalid data (Field: api_name)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 99,
        "json_path": "$.blueprints[*].chart_data.nodes[*].state.api_name"
      },
      "status": "error"
    }
  ]
}
```
