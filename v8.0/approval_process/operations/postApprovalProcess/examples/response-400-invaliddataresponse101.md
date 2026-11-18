INVALID_DATA error for invalid data on the resource field

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
