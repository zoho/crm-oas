Error with code **AMBIGUITY_DURING_PROCESSING** for fields with widget or kiosk

```json
{
  "transitions": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "type",
            "json_path": "$.transitions[0].during_inputs[0].type"
          },
          {
            "api_name": "type",
            "json_path": "$.transitions[0].during_inputs[1].type"
          }
        ]
      },
      "message": "Fields are configured along with widget or kiosk",
      "status": "error"
    }
  ]
}
```
