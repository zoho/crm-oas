# Examples: getScheduledJobs

**GET /settings/fields/{fieldId}/actions/scheduled_jobs**

## Parameter examples

### `job_id` (query) — Example

```json
"111113000000135098"
```

### `page` (query) — Example

```json
1
```

### `per_page` (query) — Example

```json
200
```

## Response examples

### Status `200` — `application/json` — Success200

Scheduled jobs list retrieved successfully

```json
{
  "scheduled_jobs": [
    {
      "job_id": "3759037000000570605",
      "action": "REPLACE_PICKLIST_OPTION",
      "module": {
        "id": "3759037000000570346",
        "api_name": "Potentials"
      },
      "details": {
        "records": {
          "total": 400,
          "processed": 0,
          "failed": 0
        },
        "workflow_rules": {
          "total": 10,
          "processed": 0,
          "failed": 0
        },
        "field_dependency": {
          "total": 3,
          "processed": 0,
          "failed": 0
        },
        "dashboard_criteria": {
          "total": 5,
          "processed": 0,
          "failed": 0
        }
      },
      "status": "SCHEDULED",
      "message": "Job scheduled"
    },
    {
      "job_id": "3759037000000570606",
      "action": "DELETE_PICKLIST_OPTION",
      "module": {
        "id": "3759037000000570456",
        "api_name": "Leads"
      },
      "details": {
        "records": {
          "total": 400,
          "processed": 300,
          "failed": 100
        },
        "workflow_rules": {
          "total": 10,
          "processed": 10,
          "failed": 0
        },
        "field_dependency": {
          "total": 2,
          "processed": 2,
          "failed": 0
        },
        "dashboard_criteria": {
          "total": 5,
          "processed": 5,
          "failed": 0
        }
      },
      "status": "COMPLETED",
      "message": "Job completed"
    }
  ],
  "info": {
    "page": 1,
    "per_page": 200,
    "count": 10,
    "more_records": true
  }
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

INVALID_MODULE error for an invalid module name

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

### Status `400` — `application/json` — InvalidDataResponse1

INVALID_DATA error for an invalid field ID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "The Field Id is Invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — FeatureNotSupportedResponse1

FEATURE_NOT_SUPPORTED when license does not support this feature

```json
{
  "code": "FEATURE_NOT_SUPPORTED",
  "details": {},
  "message": "Your License does not support this feature",
  "status": "error"
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

REQUIRED_PARAM_MISSING when a required parameter is absent

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

### Status `403` — `application/json` — NoPermissionResponse1

NO_PERMISSION error for insufficient profile permissions

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Role_Prefix_Customize_Zoho_CRM"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
