DEPENDENT_FIELD_MISSING error for a missing dependent field (name)

```json
{
  "blueprints": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "actual_value",
          "json_path": "$.blueprints[*].states[*].pick_list_value.actual_value"
        },
        "api_name": "name",
        "json_path": "$.blueprints[*].states[*].pick_list_value.blueprints.states.name"
      },
      "status": "error"
    }
  ]
}
```
