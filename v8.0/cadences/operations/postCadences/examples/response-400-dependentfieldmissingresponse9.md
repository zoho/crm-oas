Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].follow_ups[0].action.type"
        },
        "api_name": "id",
        "json_path": "$.cadences[0].follow_ups[0].action.id"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
