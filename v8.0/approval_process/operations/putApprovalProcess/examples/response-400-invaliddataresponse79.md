INVALID_DATA error response caused by invalid fields data

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "fields",
        "maximum_length": 2,
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.fields"
      },
      "status": "error"
    }
  ]
}
```
