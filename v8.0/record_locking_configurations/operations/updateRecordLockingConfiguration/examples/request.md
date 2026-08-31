### `application/json` — RequestBody

Request body for updating a record locking configuration

```json
{
  "record_locking_configurations": [
    {
      "id": "2000000066499",
      "lock_type": "both",
      "locked_for": "all_profiles",
      "restricted_actions": [
        "update",
        "delete",
        "change_owner"
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
          "name": "High Value Deal Lock",
          "id": "2000000066513",
          "lock_existing_records": true,
          "criteria": {
            "amount": {
              "gte": 50000
            }
          }
        }
      ],
      "restricted_communications": [
        "send_mail"
      ],
      "lock_excluded_profiles": [
        {
          "id": "2000000000497"
        },
        {
          "id": "2000000000499"
        }
      ],
      "lock_for_portal_users": true
    }
  ]
}
```
