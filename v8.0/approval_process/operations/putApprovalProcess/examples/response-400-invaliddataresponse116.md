Approver field object in an approver stage exceeds the maximum length of 1

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.field"
      },
      "status": "error"
    }
  ]
}
```
