Invalid data error naming the **type** field on the create request

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 100,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.type"
      },
      "status": "error"
    }
  ]
}
```
