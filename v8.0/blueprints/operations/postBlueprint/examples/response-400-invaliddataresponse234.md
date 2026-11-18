INVALID_DATA error for an escalation period with an incorrect data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "period",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].states[*].state_escalation.period"
      },
      "status": "error"
    }
  ]
}
```
