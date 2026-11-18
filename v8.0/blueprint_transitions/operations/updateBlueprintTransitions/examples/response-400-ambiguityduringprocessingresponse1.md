Error response with code AMBIGUITY_DURING_PROCESSING: Provide proper data

```json
{
  "transitions": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "type",
            "json_path": "$.transitions[0].actions[1].type"
          },
          {
            "api_name": "type",
            "json_path": "$.transitions[0].actions[0].type"
          }
        ]
      },
      "message": "Provide proper data",
      "status": "error"
    }
  ]
}
```
