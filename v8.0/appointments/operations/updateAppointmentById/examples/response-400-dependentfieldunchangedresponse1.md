DEPENDENT_FIELD_UNCHANGED error when reschedule time matches existing Appointment_Start_Time.

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_UNCHANGED",
      "details": {
        "dependee": {
          "api_name": "Appointment_Start_Time",
          "json_path": "$.data[0].Appointment_Start_Time"
        },
        "api_name": "Rescheduled_From",
        "json_path": "$.data[0].Rescheduled_From"
      },
      "message": "Reschedule_From and Appointment_Start_Time cannot be same",
      "status": "error"
    }
  ]
}
```
