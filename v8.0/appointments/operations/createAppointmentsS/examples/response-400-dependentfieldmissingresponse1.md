DEPENDENT_FIELD_MISSING when Rescheduled_From is empty.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Reschedule_Reason",
          "json_path": "$.data[0].Reschedule_Reason"
        },
        "api_name": "Rescheduled_From",
        "json_path": "$.data[0].Rescheduled_From"
      },
      "message": "Rescheduled_From cannot be empty",
      "status": "error"
    }
  ]
}
```
