DEPENDENT_FIELD_MISSING for Status not set to Cancelled.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Cancellation_Reason",
          "json_path": "$.data[0].Cancellation_Reason"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "To Update the fields of Cancellation Information Section, value of Status should be Cancelled",
      "status": "error"
    }
  ]
}
```
