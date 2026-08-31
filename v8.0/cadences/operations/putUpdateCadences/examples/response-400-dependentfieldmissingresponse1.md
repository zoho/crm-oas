Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].type"
        },
        "api_name": "custom_view",
        "json_path": "$.cadences[0].custom_view"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
