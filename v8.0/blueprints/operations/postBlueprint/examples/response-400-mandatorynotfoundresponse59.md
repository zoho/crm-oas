MANDATORY_NOT_FOUND error for a missing escalation period field

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "period",
        "json_path": "$.blueprints[*].states[*].state_escalation.period"
      },
      "status": "error"
    }
  ]
}
```
