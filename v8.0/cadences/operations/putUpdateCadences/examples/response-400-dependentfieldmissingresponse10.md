Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].follow_ups[1].action.type"
        },
        "api_name": "details",
        "json_path": "$.cadences[0].follow_ups[1].action.details"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
