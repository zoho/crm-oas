INVALID_DATA error for an invalid data type in the type field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approve[*].type"
      },
      "status": "error"
    }
  ]
}
```
