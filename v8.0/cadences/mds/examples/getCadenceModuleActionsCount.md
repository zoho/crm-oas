# Examples: getCadenceModuleActionsCount

**GET /settings/automation/cadences/actions/count**

## Response examples

### Status `200` — `application/json` — Success200

Successful Cadence module actions count response

```json
{
  "count": 15
}
```

### Status `400` — `application/json` — RequiredModuleParamMissing

Missing module parameter error

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

### Status `400` — `application/json` — InvalidModuleName

Invalid module name error

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

### Status `403` — `application/json` — NoPermissionResponse1

No permission to access Cadence module actions error

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_View_Cadences"
    ]
  },
  "message": "No permission",
  "status": "error"
}
```
