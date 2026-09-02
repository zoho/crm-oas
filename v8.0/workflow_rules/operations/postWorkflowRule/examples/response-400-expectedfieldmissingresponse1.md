Error response with code EXPECTED_FIELD_MISSING: Specify atleast one field

```json
{
  "workflow_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.module.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.module.id"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
