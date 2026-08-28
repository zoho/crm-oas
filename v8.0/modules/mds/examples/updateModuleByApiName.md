# Examples: updateModuleByApiName

**PUT /settings/modules/{moduleIdentifier}**

## Request examples

### `application/json` — UpdateModuleLabelsAndProfiles

Update Module Labels And Profile Access

```json
{
  "modules": [
    {
      "singular_label": "Custom Module",
      "plural_label": "Custom Modules",
      "id": "111111000000242167",
      "profiles": [
        {
          "id": "111111000000000497"
        },
        {
          "id": "111111000000000499"
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessfulUpdate

Module Update Succeeded

```json
{
  "modules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000242167"
      },
      "message": "module updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModuleApiName

Invalid Module Identifier

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "resource_path_index": 2
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — LabelTooLong

Label exceeds maximum length

```json
{
  "modules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 50,
        "api_name": "singular_label",
        "json_path": "$.modules[0].singular_label"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LabelSpecialCharacters

Label contains special characters

```json
{
  "modules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "singular_label",
        "json_path": "$.modules[0].singular_label"
      },
      "message": "Special characters in module singular name",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataType

Incorrect Field Data Type

```json
{
  "modules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "jsonobject",
        "api_name": "_delete",
        "json_path": "$.modules.profiles[0]._delete"
      },
      "message": "_delete is not an valid datatype",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ApiVersionNotSupported

API Version is not Supported

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "supported_version": 2
  },
  "message": "api version is not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — MissingProfiles

Profiles field is missing or not provided

```json
{
  "modules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "profiles",
        "json_path": "$.modules[0].profiles"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MissingPluralLabel

Plural Label Field Missing

```json
{
  "modules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "plural_label",
        "json_path": "$.modules[0].plural_label"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MissingSingularLabel

Singular Label Field Missing

```json
{
  "modules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "singular_label",
        "json_path": "$.modules[0].singular_label"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateSingularLabel

Duplicate Singular Label Conflict

```json
{
  "modules": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "singular_label",
        "json_path": "$.modules[0].singular_label"
      },
      "message": "Module singular name duplicate",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicatePluralLabel

Duplicate Plural Label Conflict

```json
{
  "modules": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "plural_label",
        "json_path": "$.modules[0].plural_label"
      },
      "message": "Module plural name duplicate",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ApiNameUpdateNotAllowed

Api Name Update is Blocked

```json
{
  "modules": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "api_name",
        "json_path": "$.modules[0].api_name"
      },
      "message": "Api name update not allowed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MinimumProfilesNotFound

Profiles minimum requirement is not met

```json
{
  "modules": [
    {
      "code": "MINIMUM_DATA_NOT_FOUND",
      "details": {
        "api_name": "profiles",
        "json_path": "$.modules[0].profiles"
      },
      "message": "At least one profile needed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AccessTypeUpdateNotAllowed

Access Type Update is Blocked

```json
{
  "modules": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "access_type",
        "json_path": "$.modules[0].access_type"
      },
      "message": "access type update not allowed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — TeamModuleProfileUpdateNotAllowed

Team Module Profile Update Blocked

```json
{
  "modules": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "profiles",
        "json_path": "$.modules[0].profiles"
      },
      "message": "profile update for team module is not allowed",
      "status": "error"
    }
  ]
}
```
