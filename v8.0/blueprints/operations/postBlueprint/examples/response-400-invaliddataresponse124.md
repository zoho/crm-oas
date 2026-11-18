INVALID_DATA error for an invalid data type in the ID field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.blueprints[*].transitions[*].module.id"
      },
      "status": "error"
    }
  ]
}
```
