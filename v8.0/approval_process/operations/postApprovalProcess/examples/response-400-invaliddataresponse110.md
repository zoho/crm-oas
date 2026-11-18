INVALID_DATA error for an invalid value in the ID property

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
