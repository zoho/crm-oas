Invalid data type error for the on_approve action name

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approve[*].name"
      },
      "status": "error"
    }
  ]
}
```
