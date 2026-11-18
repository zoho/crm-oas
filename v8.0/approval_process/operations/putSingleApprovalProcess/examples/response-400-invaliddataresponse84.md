Invalid data type error for the actions_per_approval field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "actions_per_approval",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].actions_per_approval"
      },
      "status": "error"
    }
  ]
}
```
