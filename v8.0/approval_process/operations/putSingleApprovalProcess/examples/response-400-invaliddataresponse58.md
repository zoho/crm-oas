Invalid overall_approval_type value exceeding the 50-character limit

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "overall_approval_type",
        "maximum_length": 50,
        "json_path": "$.approval_process[*].rules[*].overall_approval_type"
      },
      "status": "error"
    }
  ]
}
```
