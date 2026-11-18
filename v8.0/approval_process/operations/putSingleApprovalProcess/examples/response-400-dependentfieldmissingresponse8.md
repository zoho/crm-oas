DEPENDENT_FIELD_MISSING error for fields under during_approval_waiting

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "update_allowed_for",
          "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.during_approval_waiting.update_allowed_for"
        },
        "api_name": "fields",
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.during_approval_waiting.approval_process.rules.overall_stages_record_modification.during_approval_waiting.fields"
      },
      "status": "error"
    }
  ]
}
```
