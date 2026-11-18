Error response with code DEPENDENT_FIELD_MISSING: dependent field missing (Field: level_up_to)

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "actions_per_approval",
          "json_path": "$.approval_process[0].rules[0].approver_stages[0].actions.actions_per_approval"
        },
        "api_name": "level_up_to",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.level_up_to"
      },
      "message": "dependent field missing",
      "status": "error"
    }
  ]
}
```
