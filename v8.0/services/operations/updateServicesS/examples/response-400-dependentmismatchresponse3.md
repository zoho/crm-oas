Dependent mismatch when Duration does not satisfy service timing

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
        "api_name": "Duration",
        "json_path": "$.data[0].Duration"
      },
      "message": "Duration does not satisfy the service timing",
      "status": "error"
    }
  ]
}
```
