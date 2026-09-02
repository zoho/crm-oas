Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.cadences[0].execution_details.unenroll_properties[3].type"
        },
        "api_name": "specific",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[3].details.specific"
      },
      "message": "dependent field is missing",
      "status": "error"
    }
  ]
}
```
