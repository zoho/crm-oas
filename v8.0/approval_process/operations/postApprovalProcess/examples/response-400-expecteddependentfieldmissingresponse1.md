Expected dependent field missing error

```json
{
  "approval_process": [
    {
      "code": "EXPECTED_DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.type"
        },
        "expected_fields": [
          {
            "api_name": "$.approval_process[0].rules[0].approver_stages[0].approver.level"
          },
          {
            "api_name": "$.approval_process[0].rules[0].approver_stages[0].approver.level_up_to"
          }
        ]
      },
      "message": "expected dependent field missing",
      "status": "error"
    }
  ]
}
```
