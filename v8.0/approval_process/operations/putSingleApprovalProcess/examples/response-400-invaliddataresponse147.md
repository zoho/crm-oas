INVALID_DATA error when after-record-rejection fields exceed the length limit

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
