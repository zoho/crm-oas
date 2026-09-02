Conflicting values ambiguity error

```json
{
  "cadences": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "triggers",
            "json_path": "$.cadences[0].follow_ups[1].triggers[0]"
          },
          {
            "api_name": "triggers",
            "json_path": "$.cadences[0].follow_ups[1].triggers[1]"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```
