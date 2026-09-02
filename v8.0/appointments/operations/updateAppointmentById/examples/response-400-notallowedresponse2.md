**NOT_ALLOWED** error when **Appointment_Start_Time** falls outside configured business hours.

```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Appointment_Start_Time",
        "json_path": "$.data[0].Appointment_Start_Time"
      },
      "message": "Appointment time does not falls under business hours",
      "status": "error"
    }
  ]
}
```
