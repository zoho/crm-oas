Error response with code LIMIT_EXCEEDED: More than 50 criteria cannot be configured with field_rules (Field: field_rules)

```json
{
  "scoring_rules": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "field_rules",
        "limit": 50,
        "json_path": "$.scoring_rules[0].field_rules"
      },
      "message": "More than 50 criteria cannot be configured with field_rules",
      "status": "error"
    }
  ]
}
```
