Invalid data type error on the **rejection_type** field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "rejection_type",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.rejection_type"
      },
      "status": "error"
    }
  ]
}
```
