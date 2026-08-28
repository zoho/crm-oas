# Examples: getGlobalPickListFieldAssociations

**GET /settings/global_picklists/{id}/actions/associations**

## Parameter examples

### `id` (path) — Example

```json
"111111000000055938"
```

### `page` (query) — Example

```json
1
```

### `per_page` (query) — Example

```json
20
```

### `include_inner_details` (query) — Example

```json
[
  "module.plural_label",
  "module.module_name",
  "layouts.status"
]
```

## Response examples

### Status `200` — `application/json` — Success

Example response for associations

```json
{
  "associations": [
    {
      "field": {
        "api_name": "Pick_List_10",
        "id": "1385208000000973001"
      },
      "module": {
        "plural_label": "tranPlur",
        "api_name": "Leads",
        "module_name": "Leads",
        "id": "1385208000000000125"
      },
      "layouts": [
        {
          "name": "Standard",
          "id": "1385208000000095055",
          "status": "active"
        }
      ]
    }
  ],
  "info": {
    "per_page": 200,
    "count": 1,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — InvalidaId

Invalid ID example

```json
{
  "code": "INVALID_DATA",
  "message": "the id given seems to be invalid",
  "details": {
    "resource_path_index": 2
  },
  "status": "error"
}
```

### Status `400` — `application/json` — DeletionInProgress

Deletion in progress example

```json
{
  "code": "NOT_ALLOWED",
  "message": "global picklist deletion in progress.",
  "details": {
    "resource_path_index": 2
  },
  "status": "error"
}
```

### Status `403` — `application/json` — ErrorExample

```json
{
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "details": {
    "permissions": [
      "Crm_Implied_Customize_Zoho_CRM"
    ]
  },
  "status": "error"
}
```

### Status `500` — `application/json` — ErrorExample

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```
