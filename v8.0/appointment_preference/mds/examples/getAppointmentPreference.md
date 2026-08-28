# Examples: getAppointmentPreference

**GET /settings/appointment_preferences**

## Response examples

### Status `200` — `application/json` — SuccessResponse

Example of successful retrieval of appointment preferences with deal record configuration.

```json
{
  "appointment_preferences": {
    "allow_booking_outside_businesshours": true,
    "sharing_enabled": true,
    "sharing_details": {
      "sharing_computation_status": false,
      "permission": "read_only"
    },
    "deal_record_configuration": {
      "layout": {
        "name": "Standard",
        "id": "4838129000000095023"
      },
      "field_mappings": [
        {
          "field": {
            "api_name": "Owner",
            "id": "4838129000000000515"
          },
          "type": "merge_field",
          "value": "${!Appointments__s.Owner}"
        },
        {
          "field": {
            "api_name": "Amount",
            "id": "4838129000000000517"
          },
          "type": "merge_field",
          "value": "${!Appointments__s.Service_Name.Price}"
        },
        {
          "field": {
            "api_name": "Deal_Name",
            "id": "4838129000000000519"
          },
          "type": "merge_field",
          "value": "${!Appointments__s.Appointment_Name}"
        },
        {
          "field": {
            "api_name": "Closing_Date",
            "id": "4838129000000000521"
          },
          "type": "merge_field",
          "value": "${!Appointments__s.Appointment_Start_Time}"
        },
        {
          "field": {
            "api_name": "Account_Name",
            "id": "4838129000000000523"
          },
          "type": "static",
          "value": {
            "name": "Printing Dimensions (Sample)",
            "id": "4838129000000659698"
          }
        },
        {
          "field": {
            "api_name": "Stage",
            "id": "4838129000000000525"
          },
          "type": "static",
          "value": "Closed Won"
        }
      ],
      "id": "4838129000000718001"
    },
    "show_job_sheet": true,
    "when_duration_exceeds": "ask_appointment_provider_to_complete",
    "when_appointment_completed": "create_deal",
    "allow_booking_outside_service_availability": true
  }
}
```
