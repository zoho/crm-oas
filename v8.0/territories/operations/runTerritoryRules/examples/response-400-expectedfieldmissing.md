Expected field missing — module identifier not provided

```json
{
  "run_rules": {
    "code": "EXPECTED_FIELD_MISSING",
    "details": {
      "expected_fields": [
        {
          "api_name": "api_name",
          "json_path": "$.run_rules.module.api_name"
        },
        {
          "api_name": "id",
          "json_path": "$.run_rules.module.id"
        }
      ]
    },
    "message": "one of the expected field is missing",
    "status": "error"
  }
}
```
