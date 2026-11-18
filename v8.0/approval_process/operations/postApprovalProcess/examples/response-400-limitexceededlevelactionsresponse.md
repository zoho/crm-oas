Error response with code LIMIT_EXCEEDED: limit exceeded (Field: actions)

```json
{
  "approval_process": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "actions",
        "limit": 1,
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].actions.actions_per_approval[0].actions"
      },
      "message": "limit exceeded",
      "status": "error"
    }
  ]
}
```
