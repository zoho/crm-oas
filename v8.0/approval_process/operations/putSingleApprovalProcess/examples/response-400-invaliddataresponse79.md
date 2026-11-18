INVALID_DATA error when the fields array exceeds the maximum length of 25

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "fields",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.fields"
      },
      "status": "error"
    }
  ]
}
```
