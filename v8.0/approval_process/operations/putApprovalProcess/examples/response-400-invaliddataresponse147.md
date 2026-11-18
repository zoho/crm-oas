INVALID_DATA: fields array exceeds maximum length 1 (Field: fields)

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "fields",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.after_record_rejection.fields"
      },
      "status": "error"
    }
  ]
}
```
