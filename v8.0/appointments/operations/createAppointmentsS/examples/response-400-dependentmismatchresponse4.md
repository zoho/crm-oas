DEPENDENT_MISMATCH for Status Overdue before end time.

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
      "message": "Appointment cannot be marked as overdue before the appointment ends",
      "status": "error"
    }
  ]
}
```
