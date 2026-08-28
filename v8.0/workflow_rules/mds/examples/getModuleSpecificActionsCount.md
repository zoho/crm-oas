# Examples: getModuleSpecificActionsCount

**GET /settings/automation/workflow_rules/actions/module_specific_count**

## Response examples

### Status `200` — `application/json` — ModuleSpecificActionsCount

Success response for status 200

```json
{
  "module_specific_count": [
    {
      "active_rules_configured": 1,
      "module": {
        "api_name": "Deals",
        "id": "111111000000002399"
      },
      "total_rules_configured": 1
    },
    {
      "active_rules_configured": 1,
      "module": {
        "api_name": "Calls",
        "id": "111111000000002421"
      },
      "total_rules_configured": 1
    },
    {
      "active_rules_configured": 2,
      "module": {
        "api_name": "Leads",
        "id": "111111000000002393"
      },
      "total_rules_configured": 2
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

Error response with code INVALID_MODULE: The value provided to the param is Invalid

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "param_name": "module"
  },
  "message": "The value provided to the param is Invalid",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse

Error response for status 403

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow"
    ]
  },
  "message": "feature not available in this edition",
  "status": "error"
}
```
