NOT_ALLOWED error for a team user approver type outside a team module

```json
{
  "approval_process": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "type",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.type"
      },
      "message": "team user is applicable for only team module",
      "status": "error"
    }
  ]
}
```
