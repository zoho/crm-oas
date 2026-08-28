# Examples: activateLayout

**POST /settings/layouts/{id}/actions/activate**

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

## Request examples

### `application/json` — SingleLayoutMixedProfiles

Activate layout with profile additions and removals

```json
{
  "layouts": [
    {
      "id": "4831139000000673152",
      "profiles": [
        {
          "id": "4831139000000650385"
        },
        {
          "id": "4831139000000653716"
        },
        {
          "id": "4831139000000015972",
          "_delete": true
        }
      ]
    }
  ]
}
```

### `application/json` — SingleLayoutAddProfilesOnly

Activate layout with profile additions only

```json
{
  "layouts": [
    {
      "id": "4831139000000673152",
      "profiles": [
        {
          "id": "4831139000000650385"
        },
        {
          "id": "4831139000000653716"
        },
        {
          "id": "4831139000001234567"
        }
      ]
    }
  ]
}
```

### `application/json` — SingleLayoutRemoveProfilesOnly

Activate layout with profile removals only

```json
{
  "layouts": [
    {
      "id": "4831139000000673152",
      "profiles": [
        {
          "id": "4831139000000015972",
          "_delete": true
        },
        {
          "id": "4831139000000015973",
          "_delete": true
        }
      ]
    }
  ]
}
```

### `application/json` — SingleLayoutNoProfiles

Activate layout without profile modifications

```json
{
  "layouts": [
    {
      "id": "4831139000000673152",
      "profiles": []
    }
  ]
}
```

### `application/json` — SingleLayoutWithoutProfilesKey

Activate layout omitting the profiles key

```json
{
  "layouts": [
    {
      "id": "4831139000000673152"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessfulActivation

Layout activated successfully

```json
{
  "layouts": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4831139000000673152"
      },
      "message": "layout activated",
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

### Status `400` — `application/json` — AlreadyActivated

Layout is already activated

```json
{
  "code": "ALREADY_ACTIVATED",
  "details": {
    "resource_path_index": 2
  },
  "message": "Cannot activate already active layout",
  "status": "error"
}
```

### Status `400` — `application/json` — PermissionUpdateNotAllowed

Permission updates not allowed on layout

```json
{
  "layouts": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "action": "set_layout_permissions",
        "id": "4831139000000673152"
      },
      "message": "Cannot perform permission updates as it is not allowed on the layout.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LastProfileRemoval

Cannot remove the only associated profile

```json
{
  "layouts": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "profiles",
        "json_path": "$.layouts[0].profiles"
      },
      "message": "Cannot remove association with profile as it is the only profile associated with layout.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ProfileNotAssociatedWithModule

Profile not associated with the module

```json
{
  "layouts": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.layouts[0].profiles[0].id"
      },
      "message": "Only profiles associated with the module can be assigned for the layout.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LiteProfileOnIntegrationLayout

Lite profile cannot be assigned to integration layout

```json
{
  "layouts": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.layouts[0].profiles[0].id"
      },
      "message": "Integration layout cannot be assigned a lite profile.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ProfileRequiresActiveLayout

Profile must have at least one active layout

```json
{
  "layouts": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.layouts[0].profiles[0].id"
      },
      "message": "Profile must have at least one active layout associated to it.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MaximumLayoutsExceeded

Maximum layouts array length exceeded

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "layouts",
    "json_path": "$.layouts"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — MaxLayoutLimitReached

Maximum active layout limit reached for the module

```json
{
  "layouts": [
    {
      "code": "CANNOT_PROCESS",
      "details": {},
      "message": "Sorry, but you can't activate this layout, as you have already reached the maximum limit of 4 layouts per module.",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermission

User lacks required permissions

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

Internal server error during activation

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Internal Server Error",
  "status": "error"
}
```
