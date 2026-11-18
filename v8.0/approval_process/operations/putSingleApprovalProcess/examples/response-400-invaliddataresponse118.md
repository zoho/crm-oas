INVALID_DATA error for invalid data in the approver field ID

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
