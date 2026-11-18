INVALID_DATA error for an invalid data type in the ID field of the create request

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approve[*].id"
      },
      "status": "error"
    }
  ]
}
```
