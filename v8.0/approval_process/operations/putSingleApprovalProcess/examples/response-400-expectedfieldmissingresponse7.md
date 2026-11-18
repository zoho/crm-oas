Error when the based_on_field approver reference lacks api_name or id

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
            "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.based_on_field.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.based_on_field.approval_process.rules.approver_stages.approver.based_on_field.id"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
