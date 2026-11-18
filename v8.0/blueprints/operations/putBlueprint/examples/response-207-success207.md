Partial update — some blueprints updated, some failed — 207 Multi-Status

```json
{
  "blueprints": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000091059"
      },
      "message": "Blueprint updated successfully",
      "status": "success"
    },
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "api_name": "connections",
        "json_path": "$.blueprints[0].chart_data.connections[0].transition",
        "dependee": {
          "api_name": "Transition_1",
          "json_path": "$.blueprints[0].chart_data.connections[0].transition"
        }
      },
      "message": "The module or layout of this transition is different from the blueprint",
      "status": "error"
    }
  ]
}
```
