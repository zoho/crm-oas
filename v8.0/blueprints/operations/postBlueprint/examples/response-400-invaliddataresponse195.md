Error response with code INVALID_DATA: Invalid data type (Field: actions)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "actions",
        "expected_data_type": "jsonarray",
        "json_path": "$.blueprints[*].transitions[*].actions"
      },
      "status": "error"
    }
  ]
}
```
