Successful response for retrieving a specific record locking configuration

```json
{
  "record_locking_configurations": [
    {
      "created_time": "2025-11-24T10:43:45+05:30",
      "locked_for": "all_profiles_except_excluded_profiles",
      "excluded_fields": [
        {
          "api_name": "Annual_Revenue",
          "id": "2000000004846"
        },
        {
          "api_name": "City",
          "id": "2000000004924"
        }
      ],
      "created_by": {
        "name": "sivasankar.g",
        "id": "2000000058001"
      },
      "feature_type": "record_locking",
      "locking_rules": [
        {
          "name": "Tesing",
          "id": "2000000066513",
          "lock_existing_records": false,
          "criteria": {
            "comparator": "equal",
            "field": {
              "api_name": "Annual_Revenue",
              "id": "2000000004846"
            },
            "type": "value",
            "value": "10"
          }
        }
      ],
      "restricted_actions": [
        "update",
        "delete",
        "tags",
        "convert",
        "change_owner"
      ],
      "lock_for_portal_users": true,
      "modified_time": "2025-11-24T10:43:45+05:30",
      "restricted_communications": [
        "send_mail"
      ],
      "system_defined": false,
      "modified_by": {
        "name": "sivasankar.g",
        "id": "2000000058001"
      },
      "id": "2000000066499",
      "lock_type": "both",
      "restricted_custom_buttons": null,
      "lock_excluded_profiles": [
        {
          "name": "Administrator",
          "id": "2000000000497"
        },
        {
          "name": "Standard",
          "id": "2000000000499"
        }
      ]
    }
  ]
}
```
