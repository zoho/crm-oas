INVALID_DATA error: wrong data type for the actions field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "actions",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].actions_per_approval[*].actions"
      },
      "status": "error"
    }
  ]
}
```
