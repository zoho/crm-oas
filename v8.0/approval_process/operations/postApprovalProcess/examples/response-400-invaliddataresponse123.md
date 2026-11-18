INVALID_DATA error for invalid data on the during_approval_waiting field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "during_approval_waiting",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.during_approval_waiting"
      },
      "status": "error"
    }
  ]
}
```
