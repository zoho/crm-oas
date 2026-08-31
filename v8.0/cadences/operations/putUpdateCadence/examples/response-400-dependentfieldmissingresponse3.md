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
        "api_name": "unenroll_date",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[0].details.unenroll_date"
      },
      "message": "dependent field is missing",
      "status": "error"
    }
  ]
}
```
