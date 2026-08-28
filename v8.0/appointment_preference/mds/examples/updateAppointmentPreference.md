# Examples: updateAppointmentPreference

**PUT /settings/appointment_preferences**

## Request examples

### `application/json` — ExpectedRequest

Example of appointment preferences update with deal record configuration and sharing settings.

```json
{
  "appointment_preferences": {
    "when_duration_exceeds": "ask_appointment_provider_to_complete",
    "show_job_sheet": true,
    "allow_booking_outside_service_availability": true,
    "allow_booking_outside_businesshours": true,
    "when_appointment_completed": "create_deal",
    "sharing_enabled": true,
    "sharing_details": {
      "permission": "full_access"
    },
    "deal_record_configuration": {
      "layout": {
        "id": "4838717000000095023",
        "name": "Standard"
      },
      "field_mappings": [
        {
          "field": {
            "id": "4838717000000000515",
            "api_name": "Owner"
          },
          "type": "merge_field",
          "value": "${!Appointments__s.Created_By}"
        },
        {
          "field": {
            "id": "4838717000000000517",
            "api_name": "Amount"
          },
          "type": "merge_field",
          "value": "${!Appointments__s.Service_Name.Price}"
        },
        {
          "field": {
            "id": "4838717000000000519",
            "api_name": "Deal_Name"
          },
          "type": "merge_field",
          "value": "${!Appointments__s.Appointment_Name}"
        },
        {
          "field": {
            "id": "4838717000000000521",
            "api_name": "Closing_Date"
          },
          "type": "merge_field",
          "value": "${!Appointments__s.Appointment_Start_Time}"
        },
        {
          "field": {
            "id": "4838717000000000523",
            "api_name": "Account_Name"
          },
          "type": "static",
          "value": {
            "id": "4838717000000659093",
            "name": "Chapman (Sample)"
          }
        },
        {
          "field": {
            "id": "4838717000000000525",
            "api_name": "Stage"
          },
          "type": "static",
          "value": "Closed Won"
        }
      ]
    }
  }
}
```

## Response examples

### Status `200` — `application/json` — SuccessResponse

Example of a successful appointment preferences update response.

```json
{
  "appointment_preferences": {
    "code": "SUCCESS",
    "details": {},
    "message": "Appointments preferences updated successfully",
    "status": "success"
  }
}
```

### Status `400` — `application/json` — MandatoryFieldMissing

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

### Status `400` — `application/json` — InvalidData

Example of an error when a field receives a value of the wrong data type.

```json
{
  "appointment_preferences": {
    "status": "error",
    "code": "INVALID_DATA",
    "details": {
      "expected_data_type": "boolean",
      "api_name": "show_job_sheet",
      "json_path": "$.appointment_preferences.show_job_sheet"
    },
    "message": "invalid data"
  }
}
```

### Status `400` — `application/json` — DependentMismatch

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

### Status `400` — `application/json` — DependentFieldMissing

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

### Status `400` — `application/json` — MandatoryNotFoundSharingEnabled

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
