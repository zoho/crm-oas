Limit exceeded error for more than 50 active approval processes

```json
{
  "approval_process": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 50,
        "limit_due_to": [
          {
            "api_name": "active",
            "json_path": "$.approval_process[0].active"
          }
        ]
      },
      "message": "active approval processes limit exceeded",
      "status": "error"
    }
  ]
}
```
