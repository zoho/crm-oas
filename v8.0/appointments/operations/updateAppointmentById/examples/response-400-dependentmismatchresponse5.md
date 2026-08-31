**DEPENDENT_MISMATCH** error when **Status** set to Scheduled with a past **Appointment_Start_Time**

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Status",
        "json_path": "$.data[0].Status"
      },
      "message": "Appointment cannot be scheduled for past dates",
      "status": "error"
    }
  ]
}
```
