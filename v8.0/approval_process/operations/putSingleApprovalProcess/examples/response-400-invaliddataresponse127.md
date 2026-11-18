INVALID_DATA error when everyone_approval_required is not a Boolean

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "everyone_approval_required",
        "expected_data_type": "boolean",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.everyone_approval_required"
      },
      "status": "error"
    }
  ]
}
```
