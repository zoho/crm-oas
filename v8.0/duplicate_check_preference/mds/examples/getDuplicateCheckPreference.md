# Examples: getDuplicateCheckPreference

**GET /settings/duplicate_check_preference**

## Response examples

### Status `200` — `application/json` — DuplicateCheckPreferenceForContacts

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

### Status `200` — `application/json` — DuplicateCheckPreferenceForConvertedLead

Duplicate check preference for converted Leads

```json
{
  "duplicate_check_preference": {
    "type": "converted_records",
    "type_configurations": []
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
  "details": {},
  "message": "You don't have permission to perform this operation",
  "status": "error"
}
```
