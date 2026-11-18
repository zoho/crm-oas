Error response with code EXPECTED_FIELD_MISSING: One of the required fields is missing

```json
{
  "approval_process": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "message": "One of the required fields is missing",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.approval_process[*].module.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.approval_process[*].module.approval_process.module.id"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
