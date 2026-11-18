DEPENDENT_FIELD_MISSING error for a missing details property in a final approval action

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].type"
        },
        "api_name": "details",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].approval_process.rules.actions_upon_final_approval.actions.details"
      },
      "status": "error"
    }
  ]
}
```
