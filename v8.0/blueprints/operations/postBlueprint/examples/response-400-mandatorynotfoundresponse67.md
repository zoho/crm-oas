MANDATORY_NOT_FOUND error for a missing ID field in action details

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions[*].details.id"
      },
      "status": "error"
    }
  ]
}
```
