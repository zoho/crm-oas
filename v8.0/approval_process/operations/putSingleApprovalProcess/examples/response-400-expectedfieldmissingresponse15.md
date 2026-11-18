Missing module ID or API name in a rejection action

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
            "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.module.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.module.approval_process.rules.actions_upon_rejection.actions.details.module.api_name"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
