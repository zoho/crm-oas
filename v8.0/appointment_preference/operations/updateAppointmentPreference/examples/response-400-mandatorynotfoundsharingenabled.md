Example of an error when sharing_details is present but sharing_enabled is missing.

```json
{
  "appointment_preferences": {
    "status": "error",
    "code": "MANDATORY_NOT_FOUND",
    "details": {
      "api_name": "sharing_enabled",
      "json_path": "$.appointment_preferences.sharing_enabled"
    },
    "message": "required field not found"
  }
}
```
