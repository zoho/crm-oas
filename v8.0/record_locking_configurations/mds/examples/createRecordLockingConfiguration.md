# Examples: createRecordLockingConfiguration

**POST /settings/record_locking_configurations**

## Request examples

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

## Response examples

### Status `201` — `application/json` — SuccessCase

Successful response for creating a record locking configuration

```json
{
  "record_locking_configurations": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "431525000001114019"
      },
      "message": "record locking configuration created successfully",
      "status": "success"
    }
  ]
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

### Status `400` — `application/json` — InvalidModuleData

Invalid module name provided

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — NotSupportedModule

Module does not support record locking

```json
{
  "code": "NOT_SUPPORTED",
  "details": {
    "param_name": "module"
  },
  "message": "the module name given is not supported for the  feature",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidFieldData

The provided field API name is incorrect or does not exist

```json
{
  "record_locking_configurations": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.record_locking_configurations[0].locking_rules[0].criteria.fields.api_name"
      },
      "message": "field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotSupportedField

Unsupported field used in criteria

```json
{
  "record_locking_configurations": [
    {
      "code": "NOT_SUPPORTED",
      "details": {
        "api_name": "api_name",
        "json_path": "$.record_locking_configurations[0].locking_rules[0].criteria.group[0].field.api_name"
      },
      "message": "field not supported",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededLockrules

Exceeded maximum number of locking rules

```json
{
  "record_locking_configurations": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 5,
        "available_limit": 2,
        "api_name": "locking_rules",
        "json_path": "$.record_locking_configurations[0].locking_rules"
      },
      "message": "Maximum limit for locking rules exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidFeaturetypeData

Invalid feature type (must be `record_locking`)

```json
{
  "record_locking_configurations": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "feature_type",
        "json_path": "$.record_locking_configurations[0].feature_type"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidRestrictedActionData

Invalid restricted action value

```json
{
  "record_locking_configurations": [
    {
      "code": "INVALID_DATA",
      "details": {
        "supported_values": [
          "convert",
          "update",
          "delete",
          "change_owner",
          "tags"
        ],
        "api_name": "restricted_actions",
        "json_path": "$.record_locking_configurations[0].restricted_actions[1]"
      },
      "message": "action not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidRestrictedCustomButtonData

Invalid custom button ID

```json
{
  "record_locking_configurations": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.record_locking_configurations[0].restricted_custom_buttons[0].id"
      },
      "message": "custom button not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidRestrictedCommunicationData

Invalid restricted communication value

```json
{
  "record_locking_configurations": [
    {
      "code": "INVALID_DATA",
      "details": {
        "supported_values": [
          "send_mail",
          "send_survey",
          "send_portal_invitation"
        ],
        "api_name": "restricted_communications",
        "json_path": "$.record_locking_configurations[0].restricted_communications[1]"
      },
      "message": "communications not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotSupportedCommunication

Restricted communication not supported

```json
{
  "record_locking_configurations": [
    {
      "code": "NOT_SUPPORTED",
      "details": {
        "api_name": "restricted_communications",
        "json_path": "$.record_locking_configurations[0].restricted_communications"
      },
      "message": "communications not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidLocktypeData

Invalid lock type value

```json
{
  "record_locking_configurations": [
    {
      "code": "INVALID_DATA",
      "details": {
        "supported_values": [
          "manual",
          "automatic",
          "both"
        ],
        "api_name": "lock_type",
        "json_path": "$.record_locking_configurations[0].lock_type"
      },
      "message": "lock_type not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidLockedforData

Invalid `locked_for` value

```json
{
  "record_locking_configurations": [
    {
      "code": "INVALID_DATA",
      "details": {
        "supported_values": [
          "all_profiles",
          "all_profiles_except_excluded_profiles"
        ],
        "api_name": "locked_for",
        "json_path": "$.record_locking_configurations[0].locked_for"
      },
      "message": "locked_for not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidExcludedProfileData

Invalid profile ID in `lock_excluded_profiles`

```json
{
  "record_locking_configurations": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.record_locking_configurations[0].lock_excluded_profiles[0].id"
      },
      "message": "lock_excluded_profiles not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingExcludedProfiles

Missing `lock_excluded_profiles` when `locked_for` is `all_profiles_except_excluded_profiles`

```json
{
  "record_locking_configurations": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "locked_for",
          "json_path": "$.record_locking_configurations[0].locked_for"
        },
        "api_name": "lock_excluded_profiles",
        "json_path": "$.record_locking_configurations[0].lock_excluded_profiles"
      },
      "message": "lock_excluded_profiles should have been given when locked_for is given as all_profiles_except_excluded_profiles ",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingLocktype

Missing `locking_rules` when `lock_type` is `automatic` or `both`

```json
{
  "record_locking_configurations": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "lock_type",
          "json_path": "$.record_locking_configurations[0].lock_type"
        },
        "api_name": "locking_rules",
        "json_path": "$.record_locking_configurations[0].locking_rules"
      },
      "message": "locking_rules should have been given when lock_type is given as automatic or both",
      "status": "error"
    }
  ]
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

### Status `400` — `application/json` — MandatoryNotFoundLocktype

Missing required `lock_type` field

```json
{
  "record_locking_configurations": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "lock_type",
        "json_path": "$.record_locking_configurations[0].lock_type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissingExcludedFields

Missing both `id` and `api_name` for an excluded field

```json
{
  "record_locking_configurations": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "json_path": "$.record_locking_configurations[0].excluded_fields[0].api_name",
            "api_name": "api_name"
          },
          {
            "json_path": "$.record_locking_configurations[0].excluded_fields[0].id",
            "api_name": "id"
          }
        ]
      },
      "message": "Field Id and apiname is missing.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AmbiguityDuringProcessing

Ambiguity when `id` and `api_name` refer to different fields

```json
{
  "record_locking_configurations": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "json_path": "$.record_locking_configurations[0].excluded_fields[0].api_name",
            "api_name": "api_name"
          },
          {
            "json_path": "$.record_locking_configurations[0].excluded_fields[0].id",
            "api_name": "id"
          }
        ]
      },
      "message": "Field Id and apiname are ambiguous",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotSupportedApiname

Unsupported field (e.g., Tag, Owner, read-only) used in excluded fields

```json
{
  "record_locking_configurations": [
    {
      "code": "NOT_SUPPORTED",
      "details": {
        "api_name": "api_name",
        "json_path": "$.record_locking_configurations[0].excluded_fields[4].api_name"
      },
      "message": "Field not supported",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataFieldsId

Invalid or missing field ID

```json
{
  "record_locking_configurations": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.record_locking_configurations[0].excluded_fields[4].id"
      },
      "message": "field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededCustomButtons

Exceeded maximum number of restricted custom buttons

```json
{
  "record_locking_configurations": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 30,
        "available_limit": 2,
        "api_name": "restricted_custom_buttons",
        "json_path": "$.record_locking_configurations[0].restricted_custom_buttons"
      },
      "message": "Maximum limit for restricted custom buttons exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededExcludedFields

Exceeded maximum number of excluded fields

```json
{
  "record_locking_configurations": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 15,
        "available_limit": 2,
        "api_name": "excluded_fields",
        "json_path": "$.record_locking_configurations[0].excluded_fields"
      },
      "message": "Maximum limit for excluded fields exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceededExcludedProfiles

Exceeded maximum number of excluded profiles

```json
{
  "record_locking_configurations": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 15,
        "available_limit": 2,
        "api_name": "lock_excluded_profiles",
        "json_path": "$.record_locking_configurations[0].lock_excluded_profiles"
      },
      "message": "Maximum limit for excluded profiles exceeded",
      "status": "error"
    }
  ]
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

### Status `400` — `application/json` — LimitExceededConfiguration

A configuration already exists for the module

```json
{
  "code": "LIMIT_EXCEEDED",
  "details": {
    "param_name": "module",
    "limit": 1
  },
  "message": "Configuration already created for this module",
  "status": "error"
}
```

### Status `400` — `application/json` — DuplicateDataCriteria

Duplicate criteria found among locking rules

```json
{
  "record_locking_configurations": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "criteria",
        "json_path": "$.record_locking_configurations[0].locking_rules[1].criteria"
      },
      "message": "Duplicate criteria found, Enter unique criteria.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataRulename

Duplicate rule name found

```json
{
  "record_locking_configurations": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.record_locking_configurations[0].locking_rules[1].name"
      },
      "message": "Duplicate rule name found, Enter unique rulename.",
      "status": "error"
    }
  ]
}
```
