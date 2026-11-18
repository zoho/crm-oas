Multi-Status Response With Partial Errors for Blueprint State Creation

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.state[0].state_escalation.trigger_details.actions.id"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "1234567890"
      },
      "message": "State created successfully",
      "status": "success"
    }
  ]
}
```
