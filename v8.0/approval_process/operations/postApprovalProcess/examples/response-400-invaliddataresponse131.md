INVALID_DATA error for an invalid data type in the ID field of the request

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.during_approval_waiting.fields[*].id"
      },
      "status": "error"
    }
  ]
}
```
