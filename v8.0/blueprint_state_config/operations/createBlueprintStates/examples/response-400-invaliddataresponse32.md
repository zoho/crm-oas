INVALID_DATA Error for Unsupported Data Type on the Name Field

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.states[*].state_escalation.trigger_details[*].actions[*].details.name"
      },
      "status": "error"
    }
  ]
}
```
