LIMIT_EXCEEDED error when rule actions exceed the allowed limit

```json
{
  "approval_process": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "cliq_notifications",
        "limit": 1,
        "json_path": "$.approval_process[0].rules[0].actions_upon_final_approval.actions"
      },
      "message": "actions limit exceeded",
      "status": "error"
    }
  ]
}
```
