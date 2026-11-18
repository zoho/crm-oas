Invalid data type for the id of the approver field in an approver stage

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
