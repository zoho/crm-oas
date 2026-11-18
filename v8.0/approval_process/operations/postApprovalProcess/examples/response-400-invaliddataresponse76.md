INVALID_DATA error for invalid data in the ID field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.fields[*].id"
      },
      "status": "error"
    }
  ]
}
```
