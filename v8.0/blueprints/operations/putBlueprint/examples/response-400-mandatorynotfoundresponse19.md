Error — missing required field: end_point in connection target (MANDATORY_NOT_FOUND)

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "end_point",
        "json_path": "$.blueprints[*].chart_data.connections[*].to.end_point"
      },
      "status": "error"
    }
  ]
}
```
