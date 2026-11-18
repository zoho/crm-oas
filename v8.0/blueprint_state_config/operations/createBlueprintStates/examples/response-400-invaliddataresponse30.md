INVALID_DATA Error for an Invalid Data Type on the Details Field

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "details",
        "expected_data_type": "jsonobject",
        "json_path": "$.states[*].state_escalation.trigger_details[*].actions[*].details"
      },
      "status": "error"
    }
  ]
}
```
