Invalid approver field API name exceeding the maximum length of 200

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.field.api_name"
      },
      "status": "error"
    }
  ]
}
```
