Error response with code LIMIT_EXCEEDED: conditions count exceeds edition limit

```json
{
  "workflow_rules": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "conditions",
        "limit": 3,
        "json_path": "$.workflow_rules[*].conditions"
      },
      "message": "conditions limit exceeded",
      "status": "error"
    }
  ]
}
```
