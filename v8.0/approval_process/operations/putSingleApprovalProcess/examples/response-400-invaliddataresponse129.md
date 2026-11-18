INVALID_DATA error: record_modification value exceeds the maximum length

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "record_modification",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification"
      },
      "status": "error"
    }
  ]
}
```
