Error when Service_Name is unavailable at the appointment time.


```json
{
  "data": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Appointment_Start_Time",
        "json_path": "$.data[0].Appointment_Start_Time"
      },
      "message": "Service is not available on the given time",
      "status": "error"
    }
  ]
}
```
