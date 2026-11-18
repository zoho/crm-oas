INVALID_DATA error: invalid data type for the precedence field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "precedence",
        "expected_data_type": "integer",
        "json_path": "$.blueprints[*].connections[*].transitions.precedence"
      },
      "status": "error"
    }
  ]
}
```
