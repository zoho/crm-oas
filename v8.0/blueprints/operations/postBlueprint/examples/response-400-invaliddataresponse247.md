Error response with code INVALID_DATA: Invalid data type (Field: value)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "integer",
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].value"
      },
      "status": "error"
    }
  ]
}
```
