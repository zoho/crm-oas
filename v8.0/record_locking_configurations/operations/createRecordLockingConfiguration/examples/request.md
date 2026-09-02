### `application/json` — RequestBody

Request body for creating a record locking configuration

```json
{
  "record_locking_configurations": [
    {
      "lock_type": "automatic",
      "locked_for": "all_profiles",
      "restricted_actions": [
        "update",
        "delete"
      ],
      "excluded_fields": [
        {
          "id": "2000000004846"
        },
        {
          "id": "2000000004924"
        }
      ],
      "feature_type": "record_locking",
      "locking_rules": [
        {
          "name": "HighValueDealsRule",
          "lock_existing_records": true,
          "criteria": {
            "field": "Amount",
            "operator": "greater_than",
            "value": 50000
          }
        },
        {
          "name": "CriticalStatusRule",
          "criteria": {
            "field": "Status",
            "operator": "equals",
            "value": "Critical"
          }
        }
      ],
      "restricted_communications": [
        "send_mail"
      ],
      "restricted_custom_buttons": [
        {
          "id": "2000000034237"
        },
        {
          "id": "2000000034564"
        }
      ],
      "lock_excluded_profiles": [
        {
          "id": "2000000000497"
        },
        {
          "id": "2000000000495"
        }
      ],
      "lock_for_portal_users": true
    }
  ]
}
```
