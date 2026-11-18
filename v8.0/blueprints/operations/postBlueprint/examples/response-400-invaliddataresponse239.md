Error response with code INVALID_DATA: Invalid data type (Field: trigger_details)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "trigger_details",
        "expected_data_type": "jsonarray",
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details"
      },
      "status": "error"
    }
  ]
}
```
