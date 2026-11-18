EXPECTED_FIELD_MISSING for api_name/id in after_record_rejection.fields[*]

```json
{
  "approval_process": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "message": "One of the required fields is missing",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.fields[*].api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.fields[*].approval_process.rules.overall_stages_record_modification.after_record_rejection.fields.id"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
