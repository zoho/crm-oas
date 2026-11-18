INVALID_DATA error for a state value that exceeds the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "state",
        "maximum_length": 1,
        "json_path": "$.blueprints[*].chart_data.nodes[*].state"
      },
      "status": "error"
    }
  ]
}
```
