# Examples: massDeleteTags

**POST /settings/tags/actions/mass_delete**

## Request examples

### `application/json` — Sample

An example of the schedule deletion of a single tag from the Leads module.

```json
{
  "mass_delete": [
    {
      "module": {
        "api_name": "Leads",
        "id": "123"
      },
      "tags": [
        {
          "id": "456",
          "name": "Priority"
        }
      ]
    }
  ]
}
```

## Response examples

### Status `202` — `application/json` — Sample

An example of mass delete tag job scheduled successfully.

```json
{
  "status": "success",
  "code": "202",
  "details": {
    "job_id": "job_789"
  },
  "message": "Mass delete job scheduled successfully"
}
```

### Status `400` — `application/json` — RootKeyMissing

mass_delete root key is missing from the request body

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "status": "error",
  "message": "required field not found",
  "details": {
    "api_name": "mass_delete",
    "json_path": "$.mass_delete"
  }
}
```

### Status `400` — `application/json` — TagsMissing

tags key is missing inside a mass_delete item

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "status": "error",
  "message": "required field not found",
  "details": {
    "api_name": "tags",
    "json_path": "$.mass_delete[0].tags"
  }
}
```

### Status `400` — `application/json` — InvalidTagId

Tag ID does not exist in the CRM

```json
{
  "code": "INVALID_DATA",
  "status": "error",
  "message": "tags not found",
  "details": {
    "api_name": "id",
    "json_path": "$.mass_delete[0].tags[0].id"
  }
}
```

### Status `400` — `application/json` — TagsNotAvailable

Tag exists but is not available in the specified module

```json
{
  "code": "INVALID_DATA",
  "status": "error",
  "message": "one of the tags seems not found.",
  "details": {
    "api_name": "id",
    "json_path": "$.mass_delete[0].tags[0].id"
  }
}
```

### Status `400` — `application/json` — TagsArrayTooLong

tags array exceeds the allowed length

```json
{
  "code": "INVALID_DATA",
  "status": "error",
  "message": "invalid data",
  "details": {
    "api_name": "tags",
    "json_path": "$.mass_delete[0].tags",
    "maximum_length": 200
  }
}
```

### Status `400` — `application/json` — TagsNotArray

tags field is not a JSON array

```json
{
  "code": "INVALID_DATA",
  "status": "error",
  "message": "invalid data",
  "details": {
    "api_name": "tags",
    "json_path": "$.mass_delete[0].tags",
    "expected_data_type": "jsonarray"
  }
}
```

### Status `400` — `application/json` — TagsAssociatedWithFeatures

Tags are associated with features and cannot be deleted

```json
{
  "code": "NOT_ALLOWED",
  "status": "error",
  "message": "tags has been associated to features",
  "details": {
    "api_name": "id",
    "json_path": "$.mass_delete[0].tags[0].id"
  }
}
```

### Status `400` — `application/json` — EmptyMassDeleteArray

mass_delete array is empty

```json
{
  "code": "INVALID_DATA",
  "status": "error",
  "message": "invalid data",
  "details": {
    "api_name": "mass_delete",
    "json_path": "$.mass_delete"
  }
}
```

### Status `400` — `application/json` — MassDeleteArrayTooLong

mass_delete array exceeds the allowed length

```json
{
  "code": "INVALID_DATA",
  "status": "error",
  "message": "invalid data",
  "details": {
    "api_name": "mass_delete",
    "json_path": "$.mass_delete",
    "maximum_length": 1
  }
}
```

### Status `400` — `application/json` — ModuleMissing

module key is missing inside a mass_delete item

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "status": "error",
  "message": "required field not found",
  "details": {
    "api_name": "module",
    "json_path": "$.mass_delete[0].module"
  }
}
```

### Status `400` — `application/json` — ModuleNotObject

module field is not a JSON object

```json
{
  "code": "INVALID_DATA",
  "status": "error",
  "message": "invalid data",
  "details": {
    "api_name": "module",
    "json_path": "$.mass_delete[0].module",
    "expected_data_type": "jsonobject"
  }
}
```

### Status `400` — `application/json` — ModuleIdMissing

The module.id field is missing from the module object

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "status": "error",
  "message": "required field not found",
  "details": {
    "api_name": "id",
    "json_path": "$.mass_delete[0].module.id"
  }
}
```

### Status `400` — `application/json` — ModuleApiNameMissing

module.api_name is missing in the module object

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "status": "error",
  "message": "required field not found",
  "details": {
    "api_name": "api_name",
    "json_path": "$.mass_delete[0].module.api_name"
  }
}
```

### Status `400` — `application/json` — AmbiguousModule

Module ID and module API name refer to different modules

```json
{
  "code": "AMBIGUITY_DURING_PROCESSING",
  "status": "error",
  "message": "ambiguous module identifiers",
  "details": {
    "ambiguity_due_to": [
      {
        "api_name": "id",
        "json_path": "$.mass_delete[0].module.id"
      },
      {
        "api_name": "api_name",
        "json_path": "$.mass_delete[0].module.api_name"
      }
    ]
  }
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

An example of invalid OAuth scope for the tags delete permission.

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "status": "error",
  "message": "invalid oauth scope to access this URL",
  "details": {
    "method": "POST",
    "url": "/crm/v8/settings/tags/actions/mass_delete"
  }
}
```

### Status `403` — `application/json` — NoPermission

User profile lacks the tag management permission

```json
{
  "code": "NO_PERMISSION",
  "status": "error",
  "message": "permission denied",
  "details": {
    "permissions": [
      "Crm_Implied_Edit_Tags"
    ]
  }
}
```
