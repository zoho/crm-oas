Missing required dependent field error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "period",
          "json_path": "$.cadences[0].execution_details.execute_every.period"
        },
        "api_name": "unit",
        "json_path": "$.cadences[0].execution_details.execute_every.unit"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
