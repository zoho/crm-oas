DEPENDENT_FIELD_MISSING error when the dependent field 'fields' is missing

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "update_allowed_for",
          "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.after_record_rejection.update_allowed_for"
        },
        "api_name": "fields",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.after_record_rejection.approval_process.rules.approver_stages.record_modification.after_record_rejection.fields"
      },
      "status": "error"
    }
  ]
}
```
