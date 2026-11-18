MANDATORY_NOT_FOUND error for a missing value field

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "value",
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].value"
      },
      "status": "error"
    }
  ]
}
```
