Error response with code DEPENDENT_MISMATCH: dependent mismatch (Field: actions_per_approval)

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "approver_stages",
          "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.level_up_to"
        },
        "maximum_length": 3,
        "api_name": "actions_per_approval",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].actions.actions_per_approval[3].approval_order"
      },
      "message": "dependent mismatch",
      "status": "error"
    }
  ]
}
```
