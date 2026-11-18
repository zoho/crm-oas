Dependent field overall_stages_record_modification missing

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "overall_approval_type",
          "json_path": "$.approval_process[*].rules[*].overall_approval_type"
        },
        "api_name": "overall_stages_record_modification",
        "json_path": "$.approval_process[*].rules[*].approval_process.rules.overall_stages_record_modification"
      },
      "status": "error"
    }
  ]
}
```
