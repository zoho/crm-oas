INVALID_DATA Error for Invalid Data Type on the Id Field

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.states[*].state_escalation.trigger_details[*].actions[*].details.id"
      },
      "status": "error"
    }
  ]
}
```
