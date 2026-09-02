Ambiguity error when both module.id and module.api_name are provided

```json
{
  "run_rules": {
    "code": "AMBIGUITY_DURING_PROCESSING",
    "details": {
      "ambiguity_due_to": [
        {
          "api_name": "api_name",
          "json_path": "$.run_rules.module.api_name"
        },
        {
          "api_name": "id",
          "json_path": "$.run_rules.module.id"
        }
      ]
    },
    "message": "Ambiguity while processing the request",
    "status": "error"
  }
}
```
