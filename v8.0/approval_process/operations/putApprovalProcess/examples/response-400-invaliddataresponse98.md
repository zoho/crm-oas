INVALID_DATA error: invalid data type for the name field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].name"
      },
      "status": "error"
    }
  ]
}
```
