DEPENDENT_FIELD_MISSING error when Available_From is omitted despite Availability_Type being set.

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
