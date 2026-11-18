INVALID_DATA error for an invalid value in the field property

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
