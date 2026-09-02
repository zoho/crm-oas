Example of missing expected field in a related_modules entry.

```json
{
  "code": "EXPECTED_FIELD_MISSING",
  "message": "Specify Atleast one field",
  "status": "error",
  "details": {
    "expected_fields": [
      {
        "api_name": "id",
        "json_path": "$.related_modules[0].id"
      },
      {
        "api_name": "api_name",
        "json_path": "$.related_modules[0].api_name"
      }
    ]
  }
}
```
