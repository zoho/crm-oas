INVALID_DATA error with invalid data in the api_name field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.during_approval_waiting.fields[*].api_name"
      },
      "status": "error"
    }
  ]
}
```
