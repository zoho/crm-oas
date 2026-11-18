Invalid data type error for rejection_type expected as text after rejection

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
