Returns the EXPECTED_FIELD_MISSING error response when a create Approval Process request omits one of the required fields. The response carries the EXPECTED_FIELD_MISSING code with the message that one of the required fields is missing.

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
