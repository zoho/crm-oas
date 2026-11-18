Error response with code INVALID_DATA: Invalid data (Field: ID)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions[*].id"
      },
      "status": "error"
    }
  ]
}
```
