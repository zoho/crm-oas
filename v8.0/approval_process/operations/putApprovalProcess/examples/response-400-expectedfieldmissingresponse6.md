EXPECTED_FIELD_MISSING for id/api_name in approver_stages[*].approver.field

```json
{
  "approval_process": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "message": "One of the required fields is missing",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.field.approval_process.rules.approver_stages.approver.field.api_name"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
