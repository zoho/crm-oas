INVALID_DATA Error for Invalid Data Type on Actions Field

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "actions",
        "expected_data_type": "jsonarray",
        "json_path": "$.states[*].state_escalation.trigger_details[*].actions"
      },
      "status": "error"
    }
  ]
}
```
