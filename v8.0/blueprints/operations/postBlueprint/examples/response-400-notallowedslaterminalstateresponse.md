Error response with code NOT_ALLOWED: SLA cannot be configured for a terminal (leaf) state that has no outgoing transitions

```json
{
  "blueprints": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.blueprints[0].connections[0].to_state.id"
      },
      "message": "SLA cannot be configured for a terminal (leaf) state that has no outgoing transitions",
      "status": "error"
    }
  ]
}
```
