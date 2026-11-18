INVALID_DATA error for invalid data type of the approver field ID

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.field.id"
      },
      "status": "error"
    }
  ]
}
```
