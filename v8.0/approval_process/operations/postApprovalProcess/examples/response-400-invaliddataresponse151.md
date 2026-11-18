Invalid data type error on the name property

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approval_trigger[*].name"
      },
      "status": "error"
    }
  ]
}
```
