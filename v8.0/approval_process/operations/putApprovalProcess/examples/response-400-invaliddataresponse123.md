INVALID_DATA error for based_on_field api_name with wrong data type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.based_on_field.api_name"
      },
      "status": "error"
    }
  ]
}
```
