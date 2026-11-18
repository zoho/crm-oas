Invalid data type error for the id field in the update request

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
