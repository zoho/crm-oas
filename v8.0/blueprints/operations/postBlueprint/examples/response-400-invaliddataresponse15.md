INVALID_DATA error for an invalid data type in the type field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].owners[*].type"
      },
      "status": "error"
    }
  ]
}
```
