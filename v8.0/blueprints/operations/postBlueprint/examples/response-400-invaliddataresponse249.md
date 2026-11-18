INVALID_DATA error for an actions array exceeding the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "actions",
        "maximum_length": 2,
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions"
      },
      "status": "error"
    }
  ]
}
```
