MANDATORY_NOT_FOUND error for a missing chart_data node api_name field

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "api_name",
        "json_path": "$.blueprints[*].chart_data.nodes[*].state.api_name"
      },
      "status": "error"
    }
  ]
}
```
