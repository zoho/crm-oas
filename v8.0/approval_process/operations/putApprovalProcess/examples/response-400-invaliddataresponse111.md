INVALID_DATA error: approver resource id exceeds maximum length of 25

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.resource.id"
      },
      "status": "error"
    }
  ]
}
```
