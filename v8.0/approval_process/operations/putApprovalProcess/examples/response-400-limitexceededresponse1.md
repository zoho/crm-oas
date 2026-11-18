LIMIT_EXCEEDED error: approver stage limit exceeded

```json
{
  "approval_process": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 10,
        "limit_due_to": [
          {
            "api_name": "approver_stages",
            "json_path": "$.approval_process[0].rules[0].approver_stages"
          }
        ]
      },
      "message": "approver stage limit exceeded",
      "status": "error"
    }
  ]
}
```
