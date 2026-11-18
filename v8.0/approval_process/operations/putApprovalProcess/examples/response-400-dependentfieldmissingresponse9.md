DEPENDENT_FIELD_MISSING: dependent field is missing (field: fields)

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "update_allowed_for",
          "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.update_allowed_for"
        },
        "api_name": "fields",
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.approval_process.rules.overall_stages_record_modification.after_record_rejection.fields"
      },
      "status": "error"
    }
  ]
}
```
