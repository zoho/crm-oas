Dependent field missing error when Unavailable_From is absent for Status.

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
