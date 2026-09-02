Error response with code EXPECTED_FIELD_MISSING: Specify atleast one field

```json
{
  "workflow_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "period",
            "json_path": "$.workflow_rules[0].conditions[0].scheduled_actions[0].execute_after.period"
          },
          {
            "api_name": "unit",
            "json_path": "$.workflow_rules[0].conditions[0].scheduled_actions[0].execute_after.unit"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
