# Examples: getVariableGroups

**GET /settings/variable_groups**

## Response examples

### Status `200` — `application/json` — Success200

Successful list variable groups response

```json
{
  "variable_groups": [
    {
      "display_label": "NewFToNew",
      "api_name": "NewFToNew",
      "name": "NewFToNew",
      "description": null,
      "id": "111114000000473989",
      "source": "crm"
    },
    {
      "display_label": "NewFToNew2",
      "api_name": "NewFToNew2",
      "name": "NewFToNew2",
      "description": null,
      "id": "111114000000473995",
      "source": "crm"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Error response for insufficient permissions

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Variables_Access"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
