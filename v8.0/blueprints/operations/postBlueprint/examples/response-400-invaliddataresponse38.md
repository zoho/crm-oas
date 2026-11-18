INVALID_DATA error for a position_x value that exceeds the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "position_x",
        "maximum_length": 4,
        "json_path": "$.blueprints[*].chart_data.nodes[*].position_x"
      },
      "status": "error"
    }
  ]
}
```
