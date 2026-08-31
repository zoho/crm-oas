Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "id",
          "json_path": "$.cadences[0].execution_details.unenroll_properties[2].id"
        },
        "api_name": "criteria",
        "json_path": "$.cadences[0].execution_details.unenroll_properties[2].details.criteria"
      },
      "message": "dependent field is missing",
      "status": "error"
    }
  ]
}
```
