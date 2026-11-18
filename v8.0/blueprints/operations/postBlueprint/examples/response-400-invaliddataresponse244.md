Error response with code INVALID_DATA: Invalid data type (Field: execute_type)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "execute_type",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].execute_type"
      },
      "status": "error"
    }
  ]
}
```
