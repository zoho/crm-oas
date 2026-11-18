Invalid data error for rejection_type exceeding 50 characters after rejection

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "rejection_type",
        "maximum_length": 50,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.rejection_type"
      },
      "status": "error"
    }
  ]
}
```
