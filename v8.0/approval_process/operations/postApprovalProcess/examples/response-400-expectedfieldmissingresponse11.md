Missing layout ID and name in actions upon final approval

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
            "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.layout.id"
          },
          {
            "api_name": "name",
            "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.layout.approval_process.rules.actions_upon_final_approval.actions.details.layout.name"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
