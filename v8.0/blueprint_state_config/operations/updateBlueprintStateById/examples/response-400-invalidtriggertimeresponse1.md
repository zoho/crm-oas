INVALID_DATA Error When Trigger Time Exceeds SLA Time for Before Execution

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "value",
        "json_path": "$.states[0].state_escalation.trigger_details[0].value"
      },
      "message": "Trigger time should be less than SLA time when execute_type is 'before'",
      "status": "error"
    }
  ]
}
```
