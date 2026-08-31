Error response with code AMBIGUITY_DURING_PROCESSING: Ambiguity during processing (Field: meeting_duration)

```json
{
  "workflow_rules": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "meeting_duration",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.meeting_duration"
          },
          {
            "api_name": "field_mappings",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.field_mappings"
          }
        ]
      },
      "message": "As All Day is passed true, meeting_duration cannot be configured",
      "status": "error"
    }
  ]
}
```
