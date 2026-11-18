Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: api_name)

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "api_name",
        "json_path": "$.blueprints[*].chart_data.connections[*].to.state.api_name"
      },
      "status": "error"
    }
  ]
}
```
