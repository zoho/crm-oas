INVALID_DATA error for an on_approve value with a non-JSONArray data type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "on_approve",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approve"
      },
      "status": "error"
    }
  ]
}
```
