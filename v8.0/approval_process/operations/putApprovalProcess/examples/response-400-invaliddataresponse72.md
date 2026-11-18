INVALID_DATA error with invalid data in the id field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.during_approval_waiting.fields[*].id"
      },
      "status": "error"
    }
  ]
}
```
