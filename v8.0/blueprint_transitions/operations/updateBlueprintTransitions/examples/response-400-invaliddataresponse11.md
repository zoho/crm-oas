Error response with code INVALID_DATA: You can provide upto 140 checklists option character limit (Field: name)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 140,
        "json_path": "$.transitions[0].during_inputs[0].items[0].name",
        "api_name": "name"
      },
      "message": "You can provide upto 140 checklists option character limit",
      "status": "error"
    }
  ]
}
```
