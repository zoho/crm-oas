Dependent mismatch error when Available_Days conflict with business days.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Available_Days",
        "json_path": "$.data[0].Available_Days"
      },
      "message": "The given Available Days are not there in business days",
      "status": "error"
    }
  ]
}
```
