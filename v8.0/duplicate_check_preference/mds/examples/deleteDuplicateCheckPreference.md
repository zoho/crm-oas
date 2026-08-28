# Examples: deleteDuplicateCheckPreference

**DELETE /settings/duplicate_check_preference**

## Response examples

### Status `200` — `application/json` — DuplicateCheckPreferenceForContacts

Duplicate check preference for Contacts

```json
{
  "duplicate_check_preference": {
    "code": "SUCCESS",
    "details": {},
    "message": "Duplicate check disabled for mapped_module_records successfully.",
    "status": "success"
  }
}
```

### Status `200` — `application/json` — DuplicateCheckPreferenceForConvertedLead

Duplicate check preference for converted Leads

```json
{
  "duplicate_check_preference": {
    "code": "SUCCESS",
    "details": {},
    "message": "Duplicate check disabled for converted_records successfully.",
    "status": "success"
  }
}
```

### Status `400` — `application/json` — RequiredParamMissing

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

### Status `400` — `application/json` — InvalidModule

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "param_name": "module"
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — NotSupported

```json
{
  "code": "NOT_SUPPORTED",
  "details": {
    "param_name": "module"
  },
  "message": "the given module is not supported for this api",
  "status": "error"
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
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "The DuplicateCheckPreference for mapped_module_records feature is not yet enabled. Please enable it before doing this action.",
  "status": "error"
}
```
