# Examples: getPickListValuesByPickListValueid

**GET /settings/fields/{fieldId}/pick_list_values/{pickListValueId}**

## Parameter examples

### `module` (query) — Leads

Leads module

```json
"Leads"
```

### `module` (query) — Contacts

Contacts module

```json
"Contacts"
```

### `module` (query) — Accounts

Accounts module

```json
"Accounts"
```

### `module` (query) — Deals

Deals module

```json
"Deals"
```

### `fieldId` (path) — StandardField

Example field ID

```json
"1629307000006596211"
```

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "pick_list_values": [
    {
      "sequence_number": 1,
      "display_value": "Referral",
      "reference_value": "Referral",
      "colour_code": null,
      "actual_value": "Referral",
      "id": "2423488000000002313",
      "type": "used",
      "layout_associations": [
        {
          "api_name": "Standard__s",
          "name": "Standard",
          "id": "2423488000000095055"
        },
        {
          "api_name": "testing_layout",
          "name": "testing layout",
          "id": "2423488000000771002"
        }
      ]
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: The Field Id is Invalid

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "The Field Id is Invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

Error response with code INVALID_MODULE: the module name given seems to be invalid

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

### Status `400` — `application/json` — RequiredParamMissingResponse1

Error response with code REQUIRED_PARAM_MISSING: One of the expected parameter is missing

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

### Status `400` — `application/json` — FeatureNotSupportedResponse1

Error response with code FEATURE_NOT_SUPPORTED: Your License does not support this feature

```json
{
  "code": "FEATURE_NOT_SUPPORTED",
  "details": {},
  "message": "Your License does not support this feature",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Error response with code NO_PERMISSION: permission denied

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
