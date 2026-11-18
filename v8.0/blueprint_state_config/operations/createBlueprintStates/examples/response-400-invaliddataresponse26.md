INVALID_DATA Error for Invalid Data Type on a State Escalation Trigger Value

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "integer",
        "json_path": "$.states[*].state_escalation.trigger_details[*].value"
      },
      "status": "error"
    }
  ]
}
```
