INVALID_DATA error for an invalid data type in the position_y field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "position_y",
        "expected_data_type": "integer",
        "json_path": "$.blueprints[*].chart_data.nodes[*].position_y"
      },
      "status": "error"
    }
  ]
}
```
