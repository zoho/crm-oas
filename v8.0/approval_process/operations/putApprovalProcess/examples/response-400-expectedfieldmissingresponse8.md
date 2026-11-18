EXPECTED_FIELD_MISSING error for a missing field in during_approval_waiting

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
            "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.during_approval_waiting.fields[*].api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.during_approval_waiting.fields[*].approval_process.rules.approver_stages.record_modification.during_approval_waiting.fields.id"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
