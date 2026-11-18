Missing field ID and api_name after rejection in approver stages

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
            "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.after_record_rejection.fields[*].api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.after_record_rejection.fields[*].approval_process.rules.approver_stages.record_modification.after_record_rejection.fields.id"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
