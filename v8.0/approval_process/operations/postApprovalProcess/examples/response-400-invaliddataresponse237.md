Invalid data type error for **actions** expected as an array after rejection

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "actions",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions"
      },
      "status": "error"
    }
  ]
}
```
