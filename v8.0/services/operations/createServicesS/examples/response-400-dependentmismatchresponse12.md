Dependent mismatch when both unavailability fields are set for Available status.

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Unavailable_Till",
          "json_path": "$.data[0].Unavailable_Till"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "When the service status is available,  either both Unavailable From and Unavailable Till must be null, or only Unavailable From can have a value.",
      "status": "error"
    }
  ]
}
```
