INVALID_DATA error for an invalid data type in the on_approval_trigger field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "on_approval_trigger",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approval_trigger"
      },
      "status": "error"
    }
  ]
}
```
