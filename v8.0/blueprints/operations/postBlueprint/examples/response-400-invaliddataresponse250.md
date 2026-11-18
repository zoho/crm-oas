INVALID_DATA error for a details value with an invalid data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "details",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions[*].details"
      },
      "status": "error"
    }
  ]
}
```
