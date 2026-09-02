Missing both `id` and `api_name` for an excluded field

```json
{
  "record_locking_configurations": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "json_path": "$.record_locking_configurations[0].excluded_fields[0].api_name",
            "api_name": "api_name"
          },
          {
            "json_path": "$.record_locking_configurations[0].excluded_fields[0].id",
            "api_name": "id"
          }
        ]
      },
      "message": "Field Id and apiname is missing.",
      "status": "error"
    }
  ]
}
```
