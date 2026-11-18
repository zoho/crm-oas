Error — missing required field: api_name in resource (MANDATORY_NOT_FOUND)

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "api_name",
        "json_path": "$.blueprints[*].connections[*].to_state.api_name"
      },
      "status": "error"
    }
  ]
}
```
