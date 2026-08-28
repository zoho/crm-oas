# Examples: getVariableAssociations

**GET /settings/variables/{id}/actions/associations**

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "variables_associations": [
    {
      "name": "email_templates",
      "resources": [
        {
          "name": "Variable Email Template",
          "details": {
            "module": {
              "api_name": "Leads",
              "id": "111111000000000042"
            }
          },
          "id": "111111000000058477"
        }
      ]
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
