# Examples: layoutDeactivate

**DELETE /settings/layouts/{id}/actions/activate**

## Parameter examples

### `id` (path) — StandardLayoutId

Standard layout ID

```json
"4831139000000655701"
```

### `id` (path) — CustomLayoutId

Custom layout ID

```json
"4831139000000673152"
```

### `module` (query) — LeadsModule

Standard CRM module - Leads

```json
"Leads"
```

### `module` (query) — ContactsModule

Standard CRM module - Contacts

```json
"Contacts"
```

### `module` (query) — DealsModule

Standard CRM module - Deals

```json
"Deals"
```

### `module` (query) — CustomModule

Custom module example

```json
"Custom_Projects"
```

### `module` (query) — CustomModuleWithNumbers

Custom module with numeric suffix

```json
"Testing_module_1"
```

### `transfer_to` (query) — TransferLayoutId

Target layout ID for configuration transfer

```json
"4831139000000655703"
```

### `transfer_to` (query) — DifferentModuleLayout

Another target layout in the same module

```json
"4831139000000655999"
```

## Response examples

### Status `200` — `application/json` — SuccessfulDeactivation

Layout deactivated successfully

```json
{
  "layouts": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4831139000000653980"
      },
      "message": "layout deactivated",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidLayoutId

Invalid layout ID provided

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "No layout found with given id",
  "status": "error"
}
```

### Status `400` — `application/json` — MissingModuleParam

Required module parameter missing

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

### Status `400` — `application/json` — LayoutHasAssociations

Layout cannot be deactivated due to existing associations

```json
{
  "layouts": [
    {
      "code": "ASSOCIATIONS_EXIST",
      "details": {
        "id": "111111000000101446"
      },
      "message": "Cannot deactivate layout as it is being used in some places",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — TransferToSameLayout

Cannot transfer configuration to the layout being deactivated

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "param_name": "transfer_to"
  },
  "message": "Cannot transfer to the deactivated layout",
  "status": "error"
}
```

### Status `400` — `application/json` — AlreadyDeactivated

Layout is already deactivated

```json
{
  "code": "ALREADY_DEACTIVATED",
  "details": {
    "resource_path_index": 2
  },
  "message": "Cannot deactivate already deactive layout",
  "status": "error"
}
```

### Status `400` — `application/json` — FlatAssociationsExist

Layout has associations (flat response)

```json
{
  "code": "ASSOCIATIONS_EXIST",
  "details": {
    "id": "1000000118778"
  },
  "message": "Cannot deactivate layout as it is being used in some places",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermission

User lacks the required layout customization permission

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

### Status `500` — `application/json` — InternalError

Internal server error during deactivation

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Internal Server Error",
  "status": "error"
}
```
