Error response with code INVALID_DATA: Invalid data (Field: execute_type)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "execute_type",
        "maximum_length": 9,
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].execute_type"
      },
      "status": "error"
    }
  ]
}
```
