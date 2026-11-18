Error response with code DEPENDENT_FIELD_MISSING: Provide states to move the current records to current version of blueprint (Field: map_states)

```json
{
  "blueprints": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "action",
          "json_path": "$.blueprints[0].record_actions.action",
          "dependee_value": "move_current_records"
        },
        "api_name": "map_states",
        "json_path": "$.blueprints[0].map_states"
      },
      "message": "Provide states to move the current records to current version of blueprint",
      "status": "error"
    }
  ]
}
```
