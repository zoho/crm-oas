Error response with code AMBIGUITY_DURING_PROCESSING: Ambiguity while processing the request

```json
{
  "scoring_rules": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "status": "error",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.api_name"
          }
        ]
      },
      "message": "Ambiguity while processing the request"
    }
  ]
}
```
