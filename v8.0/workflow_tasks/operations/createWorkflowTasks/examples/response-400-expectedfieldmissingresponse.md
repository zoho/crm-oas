Error response with code EXPECTED_FIELD_MISSING: Specify Atleast one field

```json
{
  "tasks": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.tasks[0].field_mapping[0].field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.tasks[0].field_mapping[0].field.api_name"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
