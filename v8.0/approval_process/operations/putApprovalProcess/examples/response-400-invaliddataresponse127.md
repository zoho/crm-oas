Invalid data type error for the everyone_approval_required field

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
