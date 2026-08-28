# Examples: getRecordLockingConfigurationPassingIdInURL

**GET /settings/record_locking_configurations/{id}**

## Response examples

### Status `200` — `application/json` — SuccessCase

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

### Status `400` — `application/json` — InvalidModule

Invalid module name provided

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — RequiredParamMissing

Missing required `module` parameter

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "module"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidData

Invalid configuration ID provided

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — FeatureNotSupported

Record locking not supported in the user's edition

```json
{
  "code": "FEATURE_NOT_SUPPORTED",
  "details": {},
  "message": "Record Locking Configuration is not supported in your edition",
  "status": "error"
}
```

### Status `400` — `application/json` — NoPermission

User lacks customization permission

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Customize_Zoho_CRM"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
