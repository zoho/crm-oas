INVALID_DATA response for invalid data in the api_name field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.fields[*].api_name"
      },
      "status": "error"
    }
  ]
}
```
