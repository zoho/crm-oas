INVALID_DATA error for a precedence field with an invalid data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "precedence",
        "expected_data_type": "integer",
        "json_path": "$.blueprints[*].module.precedence"
      },
      "status": "error"
    }
  ]
}
```
