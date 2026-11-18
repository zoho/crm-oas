INVALID_DATA error for an invalid data type on the based_on_field ID

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.based_on_field.id"
      },
      "status": "error"
    }
  ]
}
```
