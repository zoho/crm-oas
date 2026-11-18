INVALID_DATA error for a state escalation value with an incorrect data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "state_escalation",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].states[*].state_escalation"
      },
      "status": "error"
    }
  ]
}
```
