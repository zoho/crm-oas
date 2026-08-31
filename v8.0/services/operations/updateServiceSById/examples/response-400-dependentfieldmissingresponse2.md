DEPENDENT_FIELD_MISSING when Available_Days required when Availability_Type is Specific Day(s).

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Unavailable_Till",
        "json_path": "$.data[0].Unavailable_Till"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
