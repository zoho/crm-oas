MANDATORY_NOT_FOUND error for a missing type field in escalate_to

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "type",
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions[*].details.escalate_to[*].type"
      },
      "status": "error"
    }
  ]
}
```
