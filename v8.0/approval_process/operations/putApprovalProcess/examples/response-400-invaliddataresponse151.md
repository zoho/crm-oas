INVALID_DATA error for invalid data in the id field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.after_record_rejection.fields[*].id"
      },
      "status": "error"
    }
  ]
}
```
