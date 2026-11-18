INVALID_DATA error for an invalid field API name data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```
