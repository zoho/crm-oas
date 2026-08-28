# Examples: deletePickListValuesByPickListValueid

**DELETE /settings/fields/{fieldId}/pick_list_values/{pickListValueId}**

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
      "code": "SUCCESS",
      "details": {
        "id": "111111000000004126"
      },
      "message": "PickList Option deleted successfully",
      "status": "success"
    }
  ]
}
```

### Status `202` — `application/json` — Success202

Success response for status 202

```json
{
  "pick_list_values": [
    {
      "code": "SCHEDULED",
      "details": {
        "job_id": "1111130000001941380"
      },
      "message": "Picklist Option deletion scheduled successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: pickList option is not available

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 4
  },
  "message": "pickList option is not available",
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

### Status `400` — `application/json` — InvalidDataResponse2

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

### Status `400` — `application/json` — NotAllowedResponse1

Error response with code NOT_ALLOWED: Restricted Option cannot be deleted

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 4
  },
  "message": "Restricted Option cannot be deleted",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse2

Error response with code NOT_ALLOWED: The picklist option is used in features

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "_associations": [
      {
        "resources": [
          {
            "name": "Lead Nurturing blueprint",
            "id": "1560451000004719301",
            "_details": null
          }
        ],
        "type": "blueprint"
      },
      {
        "resources": [
          {
            "name": "CadenceTest1",
            "id": "1560451000004719986",
            "_details": null
          }
        ],
        "type": "cadences"
      }
    ],
    "resource_path_index": 4
  },
  "message": "The picklist option is used in features",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse3

Error response with code NOT_ALLOWED: Global picklist option cannot be deleted

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 4
  },
  "message": "Global picklist option cannot be deleted",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse4

Error response with code NOT_ALLOWED: PickList field should have at least one option in the layouts

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 4
  },
  "message": "PickList field should have at least one option in the layouts",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse5

Error response with code NOT_ALLOWED: PickList field should be in at most one layout or in unused state in all layouts

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 4
  },
  "message": "PickList field should be in at most one layout or in unused state in all layouts",
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
