Invalid data error for **after_record_rejection** exceeding maximum length 1

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "after_record_rejection",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.after_record_rejection"
      },
      "status": "error"
    }
  ]
}
```
