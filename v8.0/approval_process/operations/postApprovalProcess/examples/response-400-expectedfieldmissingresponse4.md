Illustrates the EXPECTED_FIELD_MISSING error response for an Approval Process create request that does not include every required field. The returned error code is EXPECTED_FIELD_MISSING and its message indicates that one of the required fields is missing.

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
            "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.during_approval_waiting.fields[*].api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.during_approval_waiting.fields[*].approval_process.rules.overall_stages_record_modification.during_approval_waiting.fields.id"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
