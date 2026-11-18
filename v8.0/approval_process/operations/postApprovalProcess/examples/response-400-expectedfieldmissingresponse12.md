Missing module ID and api_name in actions upon final approval

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
            "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.module.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.module.approval_process.rules.actions_upon_final_approval.actions.details.module.api_name"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
