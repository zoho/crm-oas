Error response with code ACTIVE_STATE_LIMIT_EXCEEDED: More than 5 active scoring rules cannot be created for a layout (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "ACTIVE_STATE_LIMIT_EXCEEDED",
      "details": {
        "api_name": "id",
        "limit": 5,
        "json_path": "$.scoring_rules[0].layout.id"
      },
      "message": "More than 5 active scoring rules cannot be created for a layout",
      "status": "error"
    }
  ]
}
```
