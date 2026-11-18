Missing field ID or API name in a final-approval field mapping

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
            "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.field_mappings[*].field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.field_mappings[*].field.approval_process.rules.actions_upon_final_approval.actions.details.field_mappings.field.api_name"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
