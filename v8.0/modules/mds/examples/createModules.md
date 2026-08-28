# Examples: createModules

**POST /settings/modules**

## Request examples

### `application/json` — MinimalModule

Create a custom module with required fields only

```json
{
  "modules": [
    {
      "plural_label": "CM123456",
      "singular_label": "CM123465",
      "api_name": "CustomModule1",
      "profiles": [
        {
          "id": "111111000000000497"
        }
      ]
    }
  ]
}
```

### `application/json` — ModuleWithTextDisplay

Create a module with a text display field

```json
{
  "modules": [
    {
      "plural_label": "CM1",
      "singular_label": "CM1",
      "api_name": "CustomModule2",
      "profiles": [
        {
          "id": "111111000000000497"
        }
      ],
      "display_field": {
        "field_label": "fieldLabel",
        "data_type": "text"
      }
    }
  ]
}
```

### `application/json` — ModuleWithAutonumber

Create a module with an auto-number display field including prefix and suffix

```json
{
  "modules": [
    {
      "plural_label": "CM21",
      "singular_label": "CM21",
      "api_name": "CustomModule3",
      "profiles": [
        {
          "id": "111111000000000497"
        }
      ],
      "display_field": {
        "field_label": "fieldLabel",
        "data_type": "autonumber",
        "auto_number": {
          "prefix": "M",
          "suffix": "H",
          "start_number": "21"
        }
      }
    }
  ]
}
```

### `application/json` — TeamBasedModule

Create a team-based custom module

```json
{
  "modules": [
    {
      "plural_label": "TeamModule1",
      "singular_label": "TeamModule1",
      "api_name": "TeamModule1",
      "access_type": "team_based"
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — SuccessfulCreation

Custom module created successfully

```json
{
  "modules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000123456"
      },
      "message": "module created successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateApiName

Duplicate api_name value in module creation request

```json
{
  "modules": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.modules[0].api_name"
      },
      "message": "A module with the provided api_name already exists. Please use a unique api_name.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MissingRequiredField

Returned when a mandatory field is missing from the request

```json
{
  "modules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "singular_label",
        "json_path": "$.modules[0].singular_label"
      },
      "message": "The required field 'singular_label' is missing from the request.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FieldLengthExceeded

Field value exceeds maximum allowed length

```json
{
  "modules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 50,
        "api_name": "field_label",
        "json_path": "$.modules[0].display_field.field_label"
      },
      "message": "The value for 'field_label' exceeds the maximum allowed length of 50 characters.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MissingAutoNumberStart

Missing start_number in auto-number display field configuration

```json
{
  "modules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "start_number",
        "json_path": "$.modules[0].display_field.auto_number.start_number"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissing

Missing auto_number configuration for autonumber display field

```json
{
  "modules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "api_name": "auto_number",
        "json_path": "$.modules[0].auto_number"
      },
      "message": "autonumber data is not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ApiVersionNotSupported

Unsupported API version used in request

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "supported_version": 6
  },
  "message": "api version is not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataType

Incorrect data type for a request field

```json
{
  "modules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
        "api_name": "plural_label",
        "json_path": "$.modules[0].plural_label"
      },
      "message": "The field 'plural_label' expects a text value.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MissingProfiles

Required profiles field not provided in request

```json
{
  "modules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "profiles",
        "json_path": "$.modules[0].profiles"
      },
      "message": "The required field 'profiles' is missing from the request.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidProfileId

Profile ID does not exist in the organization

```json
{
  "modules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.modules[0].profiles[0].id"
      },
      "message": "The provided profile ID is invalid or does not exist.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidProfileDatatype

Profile ID provided with incorrect data type

```json
{
  "modules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "bigint",
        "api_name": "id",
        "json_path": "$.modules[0].profile[0].id"
      },
      "message": "The field 'id' expects a bigint value for the profile ID.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MissingProfileId

Profile entry missing required ID field

```json
{
  "modules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.modules[0].profiles[0].id"
      },
      "message": "The required field 'id' is missing from the profile configuration.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateSingularLabel

Duplicate singular_label value in module creation request

```json
{
  "code": "DUPLICATE_DATA",
  "details": {
    "api_name": "singular_label",
    "json_path": "$.modules[0].singular_label"
  },
  "message": "A module with this singular label already exists. Please use a unique singular_label.",
  "status": "error"
}
```

### Status `400` — `application/json` — LimitExceeded

Module creation limit has been reached

```json
{
  "code": "LIMIT_EXCEEDED",
  "details": {
    "limit": 10
  },
  "message": "The maximum number of custom modules (10) for your current edition has been reached.",
  "status": "error"
}
```

### Status `400` — `application/json` — LiteProfileLimit

Lite profile limit exceeded for custom module

```json
{
  "modules": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.modules.profiles.id"
      },
      "message": "Only 10 modules can be enabled for Lite Profile.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NullApiName

api_name submitted as null or empty string

```json
{
  "modules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.modules[0].api_name"
      },
      "message": "The field 'api_name' cannot be null or empty. Please provide a valid api_name.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidApiName

Invalid api_name naming convention

```json
{
  "modules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.modules[0].api_name"
      },
      "message": "The api_name format is invalid. It must follow CRM naming conventions.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ReservedKeyword

Reserved system keyword used as api_name

```json
{
  "modules": [
    {
      "code": "RESERVED_KEYWORD_NOT_ALLOWED",
      "details": {
        "api_name": "api_name",
        "json_path": "$.modules[0].api_name"
      },
      "message": "The api_name contains a reserved system keyword. Please choose a different name.",
      "status": "error"
    }
  ]
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

OAuth token missing required ZohoCRM.settings.modules.CREATE scope

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "invalid oauth scope to access this URL",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermission

User lacks Crm_Implied_Customize_Zoho_CRM permission

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

### Status `403` — `application/json` — NoPermissionTeamBased

User lacks permission to create a team-based module

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Create_Team_Module"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
