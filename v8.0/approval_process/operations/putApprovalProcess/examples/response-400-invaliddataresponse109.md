INVALID_DATA when approver resource exceeds maximum length of 1

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "resource",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.resource"
      },
      "status": "error"
    }
  ]
}
```
