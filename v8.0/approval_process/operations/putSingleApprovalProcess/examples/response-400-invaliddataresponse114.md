Invalid data type error for the approver level

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "level",
        "expected_data_type": "integer",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.level"
      },
      "status": "error"
    }
  ]
}
```
