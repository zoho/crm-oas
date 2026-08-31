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
