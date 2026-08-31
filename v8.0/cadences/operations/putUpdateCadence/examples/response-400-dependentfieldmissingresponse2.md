Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].execution_details.unenroll_properties[0].type"
        },
        "api_name": "details",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[0].details"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
