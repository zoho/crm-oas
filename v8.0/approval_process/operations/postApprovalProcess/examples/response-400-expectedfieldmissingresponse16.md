Demonstrates the bad request response returned when a required field is omitted from the Approval Process create request. The error uses the EXPECTED_FIELD_MISSING code and reports that one of the required fields is missing.

```json
{
  "approval_process": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "message": "One of the required fields is missing",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.field_mappings[*].field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.field_mappings[*].field.approval_process.rules.actions_upon_rejection.actions.details.field_mappings.field.api_name"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
