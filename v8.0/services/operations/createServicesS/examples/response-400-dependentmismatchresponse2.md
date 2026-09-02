Dependent mismatch where Available_Timings value does not satisfy business timing constraints.

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
        "api_name": "To",
        "json_path": "$.data[0].Available_Timings[0].To"
      },
      "message": "Service available time does not satisfy the business timing",
      "status": "error"
    }
  ]
}
```
