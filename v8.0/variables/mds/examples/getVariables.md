# Examples: getVariables

**GET /settings/variables**

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "variables": [
    {
      "read_only": false,
      "api_name": "NewTEST",
      "name": "NewTEST",
      "description": null,
      "id": "111115000000091005",
      "source": "crm",
      "type": "integer",
      "variable_group": {
        "api_name": "General",
        "id": "111115000000088076"
      },
      "value": ""
    },
    {
      "read_only": false,
      "api_name": "newtotest",
      "name": "newtotest",
      "description": null,
      "id": "111115000000094003",
      "source": "crm",
      "type": "integer",
      "variable_group": {
        "api_name": "General",
        "id": "111115000000088076"
      },
      "value": ""
    },
    {
      "read_only": false,
      "api_name": "NTEST",
      "name": "NTEST",
      "description": null,
      "id": "111115000000091001",
      "source": "crm",
      "type": "integer",
      "variable_group": {
        "api_name": "General",
        "id": "111115000000088076"
      },
      "value": ""
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Error response with code NO_PERMISSION: permission denied

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
