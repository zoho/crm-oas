Example of ambiguity in request field data.

```json
{
  "map_dependency": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.map_dependency[0].parent.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.map_dependency[0].parent.api_name"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```
