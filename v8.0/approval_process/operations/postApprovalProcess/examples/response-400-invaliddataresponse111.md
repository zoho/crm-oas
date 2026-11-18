INVALID_DATA error for an invalid data type in the api_name property

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.field.api_name"
      },
      "status": "error"
    }
  ]
}
```
