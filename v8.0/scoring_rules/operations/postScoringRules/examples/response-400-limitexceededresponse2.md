Error response with code LIMIT_EXCEEDED: More than 10 scoring rules cannot be created for a layout (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "id",
        "limit": 10,
        "json_path": "$.scoring_rules[0].layout.id"
      },
      "message": "More than 10 scoring rules cannot be created for a layout",
      "status": "error"
    }
  ]
}
```
