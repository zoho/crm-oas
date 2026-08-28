# Examples: getWorkflowRulesCount

**GET /settings/automation/workflow_rules/actions/rules_count**

## Response examples

### Status `200` — `application/json` — Success200

Successful retrieval of workflow rule quota and usage counts


```json
{
  "rules_count": {
    "scheduled_actions_per_rule_limit": 5,
    "total_rules_limit": 2500,
    "active_rules_configured": 2,
    "rules_per_process_limit": 10,
    "total_rules_limit_per_module": 125,
    "active_rules_limit": 2000,
    "total_rules_configured": 2,
    "active_rules_limit_per_module": 75,
    "total_actions_per_rule_limit": 50
  }
}
```

### Status `403` — `application/json` — NoPermissionResponse

Access denied due to missing permission or unsupported edition


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
