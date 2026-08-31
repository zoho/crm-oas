Error response with code ALREADY_USED: The condition is already used in the mentioned workflow

```json
{
  "workflow_rules": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "criteria_details",
        "exists_in": {
          "api_name": "criteria_details",
          "json_path": "$.workflow_rules[0].conditions[0].criteria_details"
        },
        "json_path": "$.workflow_rules[0].conditions[1].criteria_details"
      },
      "message": "duplicate criteria details.",
      "status": "error"
    }
  ]
}
```
