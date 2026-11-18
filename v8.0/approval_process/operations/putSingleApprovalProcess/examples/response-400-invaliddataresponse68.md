Error response when the fields key exceeds its maximum length

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "fields",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.during_approval_waiting.fields"
      },
      "status": "error"
    }
  ]
}
```
