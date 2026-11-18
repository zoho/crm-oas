Error response with code INVALID_DATA: Invalid data (Field: name)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 50,
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions[*].name"
      },
      "status": "error"
    }
  ]
}
```
