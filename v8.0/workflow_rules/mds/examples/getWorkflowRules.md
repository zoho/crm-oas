# Examples: getWorkflowRules

**GET /settings/automation/workflow_rules**

## Parameter examples

### `filter` (query) — Example

```json
"{\"field\":{\"api_name\":\"name\"},\"comparator\":\"contains\",\"value\":\"Lead Notification\"}"
```

## Response examples

### Status `200` — `application/json` — GetAllResponses

Successful retrieval of the workflow rules list

```json
{
  "workflow_rules": [
    {
      "created_time": "2025-12-03T01:30:24-08:00",
      "execute_when": {
        "details": {
          "trigger_module": {
            "api_name": "Leads",
            "id": "3361265000000000125"
          }
        },
        "type": "create"
      },
      "editable": true,
      "module": {
        "api_name": "Leads",
        "id": "3361265000000000125"
      },
      "deletable": true,
      "description": null,
      "source": "crm",
      "created_by": {
        "name": "B Indumathi",
        "id": "3361265000000535001"
      },
      "last_executed_time": null,
      "modified_time": "2025-12-03T01:30:24-08:00",
      "name": "GetFieldUpdate",
      "modified_by": {
        "name": "B Indumathi",
        "id": "3361265000000535001"
      },
      "lock": {
        "locked_by": null,
        "message": null,
        "status": false
      },
      "id": "3361265000006526160",
      "status": {
        "active": true
      }
    },
    {
      "created_time": "2025-12-03T01:41:35-08:00",
      "execute_when": {
        "details": {
          "trigger_module": {
            "api_name": "Leads",
            "id": "3361265000000000125"
          }
        },
        "type": "create"
      },
      "editable": true,
      "module": {
        "api_name": "Leads",
        "id": "3361265000000000125"
      },
      "deletable": true,
      "description": null,
      "source": "crm",
      "created_by": {
        "name": "B Indumathi",
        "id": "3361265000000535001"
      },
      "last_executed_time": null,
      "modified_time": "2025-12-03T01:48:01-08:00",
      "name": "ConvertGetWF",
      "modified_by": {
        "name": "B Indumathi",
        "id": "3361265000000535001"
      },
      "lock": {
        "locked_by": null,
        "message": null,
        "status": false
      },
      "id": "3361265000006526223",
      "status": {
        "active": false
      }
    }
  ],
  "info": {
    "per_page": 200,
    "count": 2,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — InvalidModuleResponse

INVALID_MODULE error for an unrecognized module parameter value

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

### Status `400` — `application/json` — InvalidParamResponse

INVALID_DATA error for an invalid sort_order parameter value

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "sort_order"
  },
  "message": "The value provided to the param is Invalid",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse

NO_PERMISSION error when workflow rules are unavailable in the current edition

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
