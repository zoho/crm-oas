INVALID_DATA Error for Invalid Id Field Value

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "regex": "[0-9]+",
        "json_path": "$.states[*].state_escalation.trigger_details[*].actions[*].details.id"
      },
      "status": "error"
    }
  ]
}
```
