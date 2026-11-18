INVALID_DATA error for invalid data in the on_approval_trigger field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "on_approval_trigger",
        "maximum_length": 5,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approval_trigger"
      },
      "status": "error"
    }
  ]
}
```
