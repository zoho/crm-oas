# Examples: getWebhookAssociatedModules

**GET /settings/automation/webhooks/actions/associated_modules**

## Response examples

### Status `200` — `application/json` — Success200

Successful response listing modules with associated webhooks

```json
{
  "associated_modules": [
    {
      "api_name": "Leads",
      "id": "4876876000000002175"
    },
    {
      "api_name": "Deals",
      "id": "4876876000000002181"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse1

NO_PERMISSION error for missing Manage Workflow permission

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied__Manage_Workflow"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
