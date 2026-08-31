DEPENDENT_FIELD_MISSING when Unavailable_From required when Status is Temporarily Unavailable.

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
        "api_name": "Unavailable_From",
        "json_path": "$.data[0].Unavailable_From"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
