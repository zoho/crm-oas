# Examples: getPickListValues

**GET /settings/fields/{fieldId}/pick_list_values**

## Parameter examples

### `fieldId` (path) — StandardField

Example field ID

```json
"1629307000006596211"
```

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

## Response examples

### Status `200` — `application/json` — MultiplePickListValues

Pick list with multiple values showing used/unused types and color codes

```json
{
  "pick_list_values": [
    {
      "sequence_number": 1,
      "display_value": "-None-",
      "reference_value": "-None-",
      "colour_code": null,
      "actual_value": "-None-",
      "id": "111111000000093642",
      "type": "used",
      "layout_associations": [
        {
          "api_name": "test_1",
          "name": "test 1",
          "id": "111111000000081166"
        },
        {
          "api_name": "Standard__s",
          "name": "Standard",
          "id": "111111000000003592"
        }
      ]
    },
    {
      "sequence_number": 2,
      "display_value": "Option 1",
      "reference_value": "Option 1",
      "colour_code": "#fea36a",
      "actual_value": "Option 1",
      "id": "111111000000093637",
      "type": "used",
      "layout_associations": [
        {
          "api_name": "Standard__s",
          "name": "Standard",
          "id": "111111000000003592"
        },
        {
          "api_name": "test_1",
          "name": "test 1",
          "id": "111111000000081166"
        }
      ]
    },
    {
      "sequence_number": 3,
      "display_value": "Option 2",
      "reference_value": "Option 2",
      "colour_code": "#c9651a",
      "actual_value": "Option 2",
      "id": "111111000000093639",
      "type": "unused",
      "layout_associations": null
    },
    {
      "sequence_number": 4,
      "display_value": "op 3",
      "reference_value": "op 3",
      "colour_code": "#ced9ff",
      "actual_value": "op 3",
      "id": "111111000000093683",
      "type": "used",
      "layout_associations": [
        {
          "api_name": "test_1",
          "name": "test 1",
          "id": "111111000000081166"
        },
        {
          "api_name": "Standard__s",
          "name": "Standard",
          "id": "111111000000003592"
        }
      ]
    }
  ]
}
```

### Status `400` — `application/json` — InvalidFieldId

Invalid field ID in request URL

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module API name in request

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — VersionNotSupported

Unsupported API version in request URL

```json
{
  "code": "VERSION_NOT_SUPPORTED",
  "details": {},
  "message": "api version is not supported",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermission

Missing required permission to access field metadata

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
