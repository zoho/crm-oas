INVALID_DATA error when the fields array exceeds one entry

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "fields",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.during_approval_waiting.fields"
      },
      "status": "error"
    }
  ]
}
```
