Error — transition module or layout mismatch (DEPENDENT_MISMATCH)

```json
{
  "blueprints": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "id",
          "json_path": "$.blueprints[0].id"
        },
        "api_name": "id",
        "json_path": "$.blueprints[0].chart_data.connections[0].transition.id"
      },
      "message": "The module or layout of this transition is different from the blueprint",
      "status": "error"
    }
  ]
}
```
