Error response with code INVALID_DATA: Invalid data type (Field: ID)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions[*].details.id"
      },
      "status": "error"
    }
  ]
}
```
