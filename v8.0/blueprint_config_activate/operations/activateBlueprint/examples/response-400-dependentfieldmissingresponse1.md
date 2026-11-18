Error response with code DEPENDENT_FIELD_MISSING: Specify record actions to be done while publishing this blueprint. (Field: record_actions)

```json
{
  "blueprints": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.blueprints[0].type"
        },
        "api_name": "record_actions",
        "json_path": "$.blueprints[0].record_actions"
      },
      "message": "Specify record actions to be done while publishing this blueprint.",
      "status": "error"
    }
  ]
}
```
