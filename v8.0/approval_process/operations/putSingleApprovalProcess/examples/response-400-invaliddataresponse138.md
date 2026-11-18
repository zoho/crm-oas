INVALID_DATA error when a during_approval_waiting field api_name exceeds 200 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.during_approval_waiting.fields[*].api_name"
      },
      "status": "error"
    }
  ]
}
```
