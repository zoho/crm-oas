Id of the approver field in an approver stage exceeds the maximum length of 25

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.field.id"
      },
      "status": "error"
    }
  ]
}
```
