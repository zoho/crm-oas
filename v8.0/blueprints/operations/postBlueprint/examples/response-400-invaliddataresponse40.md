INVALID_DATA error for an invalid data type in the state field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "state",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].chart_data.nodes[*].state"
      },
      "status": "error"
    }
  ]
}
```
