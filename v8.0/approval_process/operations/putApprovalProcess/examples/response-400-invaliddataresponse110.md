INVALID_DATA error: approver resource id must be a bigint

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.resource.id"
      },
      "status": "error"
    }
  ]
}
```
