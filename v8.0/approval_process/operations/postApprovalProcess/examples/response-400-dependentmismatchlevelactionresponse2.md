Error response with code DEPENDENT_MISMATCH: actions_per_approval is applicable for level approver type (Field: actions_per_approval)

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.type"
        },
        "api_name": "actions_per_approval",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].actions.actions_per_approval"
      },
      "message": "dependent mismatch",
      "status": "error"
    }
  ]
}
```
