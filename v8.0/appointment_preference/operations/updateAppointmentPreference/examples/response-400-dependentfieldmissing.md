Example of dependent field missing error when sharing_enabled is set but sharing_details is absent.

```json
{
  "appointment_preferences": {
    "status": "error",
    "code": "DEPENDENT_FIELD_MISSING",
    "details": {
      "dependee": {
        "api_name": "sharing_enabled",
        "json_path": "$.appointment_preferences.sharing_enabled"
      },
      "api_name": "sharing_details",
      "json_path": "$.appointment_preferences.sharing_details"
    },
    "message": "Dependent Field missing"
  }
}
```
