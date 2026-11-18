MANDATORY_NOT_FOUND error for a missing node state

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "state",
        "json_path": "$.blueprints[*].chart_data.nodes[*].state"
      },
      "status": "error"
    }
  ]
}
```
