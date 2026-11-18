MANDATORY_NOT_FOUND error for missing escalation trigger details

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "trigger_details",
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details"
      },
      "status": "error"
    }
  ]
}
```
