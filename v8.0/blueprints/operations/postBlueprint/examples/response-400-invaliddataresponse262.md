Error response with code INVALID_DATA: Invalid data (Field: ID)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "regex": "[0-9]+",
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions[*].details.id"
      },
      "status": "error"
    }
  ]
}
```
