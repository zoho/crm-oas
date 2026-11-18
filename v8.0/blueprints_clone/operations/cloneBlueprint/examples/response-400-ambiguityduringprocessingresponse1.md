AMBIGUITY_DURING_PROCESSING error when map_states is given for a draft clone

```json
{
  "blueprints": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "type",
            "json_path": "$.blueprints[0].type"
          },
          {
            "api_name": "map_states",
            "json_path": "$.blueprints[0].map_states"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```
