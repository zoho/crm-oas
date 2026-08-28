# Examples: updateModules

**PUT /settings/modules**

## Request examples

### `application/json` — RemoveAndAddProfile

Remove admin profile and add standard profile for a custom module

```json
{
  "modules": [
    {
      "singular_label": "CMUpdated",
      "plural_label": "CMUpdated",
      "id": "111111000000263276",
      "profiles": [
        {
          "id": "111111000000000497",
          "_delete": null
        },
        {
          "id": "111111000000000499"
        }
      ]
    }
  ]
}
```

### `application/json` — BatchUpdateMixedOperations

Batch update with label changes and profile modifications

```json
{
  "modules": [
    {
      "singular_label": "CMUpdated",
      "plural_label": "CMUpdated",
      "id": "111111000000263276",
      "profiles": [
        {
          "id": "111111000000000497"
        },
        {
          "id": "111111000000000499",
          "_delete": null
        }
      ]
    },
    {
      "id": "111111000000258973",
      "plural_label": "CM2Updated",
      "singular_label": "CM2Updated"
    }
  ]
}
```

### `application/json` — UpdateLabelsOnly

Update module labels without changing profiles

```json
{
  "modules": [
    {
      "id": "111111000000002654",
      "plural_label": "DealsUpdated",
      "singular_label": "DealUpdated"
    }
  ]
}
```

### `application/json` — RemoveProfileOnly

Remove profile access without updating labels

```json
{
  "modules": [
    {
      "id": "111111000000002654",
      "profiles": [
        {
          "id": "111111000000000497",
          "_delete": null
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SingleModuleSuccess

Single module updated successfully

```json
{
  "modules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000263276"
      },
      "message": "the module name has been updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `200` — `application/json` — BatchSuccess

All modules in the batch updated successfully

```json
{
  "modules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000263276"
      },
      "message": "module updated successfully",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000002654"
      },
      "message": "module updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — PartialSuccessInvalidProfile

Partial batch - one success, one invalid profile error

```json
{
  "modules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000263276"
      },
      "message": "module updated successfully",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.modules[1].profiles[0].id"
      },
      "message": "Invalid profile id passed",
      "status": "error"
    }
  ]
}
```

### Status `207` — `application/json` — PartialSuccessMissingId

Partial success - first module succeeds, second fails with missing required ID

```json
{
  "modules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000002654"
      },
      "message": "module updated successfully",
      "status": "success"
    },
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.modules[1]"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `207` — `application/json` — PartialSuccessLabelLength

Partial success - label length exceeded error for one module

```json
{
  "modules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000263276"
      },
      "message": "module updated successfully",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 50,
        "api_name": "plural_label",
        "json_path": "$.modules[1].plural_label"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `207` — `application/json` — PartialSuccessTeamModuleProfileUpdate

Partial success - profile update not allowed for team module

```json
{
  "modules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000263276"
      },
      "message": "module updated successfully",
      "status": "success"
    },
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "profiles",
        "json_path": "$.modules[1].profiles"
      },
      "message": "profile update for team module is not allowed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModuleId

Module ID does not exist

```json
{
  "modules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.modules[0].id"
      },
      "message": "the module id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MissingRequiredId

Required module ID is missing

```json
{
  "modules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.modules[0].id"
      },
      "message": "required data not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LabelLengthExceeded

Module label exceeds maximum length

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

### Status `400` — `application/json` — InvalidProfileId

Profile ID does not exist

```json
{
  "modules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.modules[0].profiles[0].id"
      },
      "message": "Invalid profile id passed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleRenameNotAllowed

Module rename not allowed

```json
{
  "modules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.modules[0].id"
      },
      "message": "Module rename not allowed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AccessTypeUpdateNotAllowed

Attempt to update access_type rejected

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

Profile update not allowed for team-based module

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
