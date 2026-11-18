LIMIT_EXCEEDED error: active approval processes limit exceeded

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
