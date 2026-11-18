Invalid data in the **trigger_type** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "trigger_type",
        "supported_values": [
          "automatic",
          "manual"
        ],
        "json_path": "$.transitions[*].trigger_type"
      },
      "status": "error"
    }
  ]
}
```
