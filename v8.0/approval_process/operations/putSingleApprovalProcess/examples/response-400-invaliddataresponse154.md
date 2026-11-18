INVALID_DATA error when the on_approval_trigger key is not a JSON array

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
