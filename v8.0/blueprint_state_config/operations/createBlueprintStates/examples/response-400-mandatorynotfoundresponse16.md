MANDATORY_NOT_FOUND Error for Missing Details Field in State Escalation Actions

```json
{
  "states": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "details",
        "json_path": "$.states[*].state_escalation.trigger_details[*].actions[*].details"
      },
      "status": "error"
    }
  ]
}
```
