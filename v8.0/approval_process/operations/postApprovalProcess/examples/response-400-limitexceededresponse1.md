LIMIT_EXCEEDED error for the active approval processes limit

```json
{
  "approval_process": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 10,
        "limit_due_to": [
          {
            "api_name": "module",
            "json_path": "$.approval_process[0].module"
          }
        ]
      },
      "message": "active approval processes limit exceeded",
      "status": "error"
    }
  ]
}
```
