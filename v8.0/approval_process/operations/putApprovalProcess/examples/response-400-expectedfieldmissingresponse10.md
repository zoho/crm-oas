Error response: required approval action field missing

```json
{
  "approval_process": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "message": "One of the required fields is missing",
      "details": {
        "expected_fields": [
          {
            "api_name": "on_approval_trigger",
            "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approval_trigger"
          },
          {
            "api_name": "on_approve",
            "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.approval_process.rules.approver_stages.actions.on_approve"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
