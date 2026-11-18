EXPECTED_FIELD_MISSING for api_name/id under rules[*].criteria.field

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
            "json_path": "$.approval_process[*].rules[*].criteria.field.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.approval_process[*].rules[*].criteria.field.approval_process.rules.criteria.field.id"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
