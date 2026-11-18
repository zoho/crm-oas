Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "user",
          "role",
          "group",
          "team_user",
          "profile"
        ],
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions[*].details.escalate_to[*].type"
      },
      "status": "error"
    }
  ]
}
```
