INVALID_DATA error: invalid data reported for the **type** field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "field_updates"
        ],
        "json_path": "$.approval_process[*].rules[*].actions_per_approval[*].actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
