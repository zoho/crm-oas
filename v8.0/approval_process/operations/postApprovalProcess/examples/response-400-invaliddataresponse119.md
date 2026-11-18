INVALID_DATA error for an invalid data type on everyone_approval_required

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
