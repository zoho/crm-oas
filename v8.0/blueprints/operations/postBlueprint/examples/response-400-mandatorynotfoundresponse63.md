MANDATORY_NOT_FOUND error for a missing execute_type field

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "execute_type",
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].execute_type"
      },
      "status": "error"
    }
  ]
}
```
