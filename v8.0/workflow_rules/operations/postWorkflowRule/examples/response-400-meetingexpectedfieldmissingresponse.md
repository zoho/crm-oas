Error response with code EXPECTED_FIELD_MISSING: Specify atleast one field

```json
{
  "workflow_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "assign_record_owner_as_host",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.host_unavailable.assign_record_owner_as_host"
          },
          {
            "api_name": "assign_task",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.host_unavailable.assign_task"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
