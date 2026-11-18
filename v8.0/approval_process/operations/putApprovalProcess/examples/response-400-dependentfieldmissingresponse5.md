DEPENDENT_FIELD_MISSING for missing fields property

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "overall_approval_type",
          "json_path": "$.approval_process[0].rules[0].approver_stages[0].record_modification.after_record_rejection.update_allowed_for"
        },
        "api_name": "fields",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].record_modification.after_record_rejection.fields"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
