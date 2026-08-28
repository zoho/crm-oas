# Examples: updateDuplicateCheckPreference

**PUT /settings/duplicate_check_preference**

## Request examples

### `application/json` — DuplicateCheckPreferenceForContacts

Duplicate check preference for Contacts

```json
{
  "duplicate_check_preference": {
    "type": "mapped_module_records",
    "type_configurations": [
      {
        "field_mappings": [
          {
            "mapped_field": {
              "api_name": "Phone",
              "name": "Contacts",
              "id": "1124664000000000457"
            },
            "current_field": {
              "api_name": "Phone",
              "name": "Leads",
              "id": "1124664000000000565"
            }
          }
        ],
        "mapped_module": {
          "api_name": "Contacts",
          "name": "Contacts",
          "id": "1124664000000000129"
        }
      }
    ]
  }
}
```

### `application/json` — DuplicateCheckPreferenceForConvertedLead

Duplicate check preference for converted Leads

```json
{
  "duplicate_check_preference": {
    "type": "converted_records",
    "type_configurations": []
  }
}
```

## Response examples

### Status `200` — `application/json` — DuplicateCheckPreferenceForContacts

Duplicate check preference for Contacts

```json
{
  "duplicate_check_preference": {
    "code": "SUCCESS",
    "details": {},
    "message": "Updated fieldMapping for mapped_module_records successfully.",
    "status": "success"
  }
}
```

### Status `400` — `application/json` — MandatoryNotFound

Mandatory field missing error

```json
{
  "status": "error",
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field not found",
  "details": {
    "api_name": "duplicate_check_preference",
    "json_path": "$.data[0].duplicate_check_preference"
  }
}
```

### Status `400` — `application/json` — RequestLevelError

Required parameter missing error

```json
{
  "status": "error",
  "code": "REQUIRED_PARAM_MISSING",
  "message": "One of the expected parameter is missing",
  "details": {
    "param_name": "module"
  }
}
```

### Status `400` — `application/json` — FeatureNotSupportedForEdition

Feature not supported for this edition

```json
{
  "status": "error",
  "code": "FEATURE_NOT_SUPPORTED",
  "message": "Your License does not support this feature.",
  "details": {}
}
```

### Status `400` — `application/json` — FeatureNotSupportedForGivenModule

Feature not supported for this module

```json
{
  "status": "error",
  "code": "NOT_SUPPORTED",
  "message": "The feature not avilable in the given module.",
  "details": {
    "param_name": "module",
    "api_name": "field_api_name",
    "json_path": "$json_path"
  }
}
```

### Status `400` — `application/json` — InvalidModuleGiven

Invalid module error

```json
{
  "status": "error",
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid.",
  "details": {
    "param_name": "module"
  }
}
```

### Status `400` — `application/json` — Ambiguity

Ambiguity during field mapping

```json
{
  "code": "AMBIGUITY_DURING_PROCESSING",
  "details": {
    "ambiguity_due_to": [
      {
        "api_name": "id",
        "json_path": "$.duplicate_check_preference[0].type_configurations.field_mappings[0].mapped_field.id"
      },
      {
        "api_name": "api_name",
        "json_path": "$.duplicate_check_preference[0].type_configurations.field_mappings[0].mapped_field.api_name"
      }
    ]
  },
  "message": "two different crm fields are found",
  "status": "error"
}
```

### Status `400` — `application/json` — DependentFieldMissing

Dependent field missing error

```json
{
  "status": "error",
  "code": "DEPENDENT_FIELD_MISSING",
  "message": "Dependent Field missing",
  "details": {
    "dependee": {
      "api_name": "field_api_name",
      "json_path": "$json_path"
    },
    "api_name": "field_api_name",
    "json_path": "$json_path"
  }
}
```

### Status `400` — `application/json` — ExpectedFieldMissing

Expected field missing error

```json
{
  "status": "error",
  "code": "EXPECTED_FIELD_MISSING",
  "message": "Specify at least one field.",
  "details": {
    "expected_fields": [
      {
        "api_name": "id",
        "json_path": "$.duplicate_check_preference[0].type_configurations.field_mappings[0].mapped_field.id"
      },
      {
        "api_name": "api_name",
        "json_path": "$.duplicate_check_preference[0].type_configurations.field_mappings[0].mapped_field.api_name"
      }
    ]
  }
}
```

### Status `400` — `application/json` — NotAllowed

Not allowed unique field mapping

```json
{
  "status": "error",
  "code": "NOT_ALLOWED",
  "message": "the given current_field API name is not a unique field API name.",
  "details": {
    "api_name": "field_api_name",
    "json_path": "$json_path"
  }
}
```

### Status `403` — `application/json` — NoPermission

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": []
  },
  "message": "the user doesn't have permission for that module.",
  "status": "error"
}
```

### Status `403` — `application/json` — FeatureNotEnabled

```json
{
  "duplicate_check_preference": {
    "code": "FEATURE_NOT_ENABLED",
    "details": {},
    "message": "The DuplicateCheckPreference for mapped_module_records feature is not yet enabled. Please enable it before doing this action.",
    "status": "error"
  }
}
```
