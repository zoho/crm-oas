Partial Success Response With Mandatory Field Validation Errors

```json
{
  "states": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "period",
        "json_path": "$.states[0].state_escalation.trigger_details[0].period"
      },
      "message": "The required data missing",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "1234567890"
      },
      "message": "State updated successfully",
      "status": "success"
    }
  ]
}
```
