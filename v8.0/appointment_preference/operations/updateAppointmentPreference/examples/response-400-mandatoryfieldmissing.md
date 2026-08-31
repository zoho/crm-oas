Example of an error when a required field is absent from the request.

```json
{
  "appointment_preferences": {
    "status": "error",
    "code": "MANDATORY_NOT_FOUND",
    "message": "Mandatory fields are missing",
    "details": {
      "api_name": "allow_booking_outside_service_availability",
      "json_path": "appointment_preferences.allow_booking_outside_service_availability"
    }
  }
}
```
