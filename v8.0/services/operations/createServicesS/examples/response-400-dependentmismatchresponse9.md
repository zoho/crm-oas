Dependent mismatch where Available_Dates includes a holiday or non-business day.

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
        "api_name": "Available_Dates",
        "json_path": "$.data[0].Available_Dates"
      },
      "message": "Available Dates value in holiday or Not in BusinessDays",
      "status": "error"
    }
  ]
}
```
