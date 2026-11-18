INVALID_DATA error for approver based_on_field with wrong data type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "based_on_field",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.based_on_field"
      },
      "status": "error"
    }
  ]
}
```
