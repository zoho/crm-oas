Example of an error due to dependent mismatch - a conflicting booking preference setting.

```json
{
  "appointment_preferences": {
    "status": "error",
    "code": "DEPENDENT_MISMATCH",
    "details": {
      "dependee": {
        "api_name": "allow_booking_outside_service_availability",
        "json_path": "$.appointment_preferences.allow_booking_outside_service_availability"
      },
      "api_name": "allow_booking_outside_businesshours",
      "json_path": "$.appointment_preferences.allow_booking_outside_businesshours"
    },
    "message": "allow_booking_outside_service_availability must be enabled to set allow_booking_outside_businesshours to true"
  }
}
```
