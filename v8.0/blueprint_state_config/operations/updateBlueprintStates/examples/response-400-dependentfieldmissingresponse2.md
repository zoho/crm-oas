DEPENDENT_FIELD_MISSING Error When a Dependent Field Value Is Absent

```json
{
  "states": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "period",
          "json_path": "$.states[0].state_escalation.period"
        },
        "api_name": "value",
        "json_path": "$.states[0].state_escalation.value"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
