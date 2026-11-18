INVALID_DATA error listing supported values for the failing field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.approval_process[0].rules[0].actions_upon_final_approval.actions[0].details.type",
        "supported_values": [
          "user",
          "channel",
          "fields"
        ]
      },
      "message": "INVALID_DATA",
      "status": "error"
    }
  ]
}
```
