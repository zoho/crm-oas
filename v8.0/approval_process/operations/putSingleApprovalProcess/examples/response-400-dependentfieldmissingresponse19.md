DEPENDENT_FIELD_MISSING error for a missing id property in a rejection action

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].type"
        },
        "api_name": "id",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].approval_process.rules.actions_upon_rejection.actions.id"
      },
      "status": "error"
    }
  ]
}
```
