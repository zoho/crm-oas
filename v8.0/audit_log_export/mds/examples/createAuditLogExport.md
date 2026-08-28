# Examples: createAuditLogExport

**POST /settings/audit_log_export**

## Request examples

### `application/json` — Default

Create audit log export with criteria filters.

```json
{
  "audit_log_export": [
    {
      "criteria": {
        "group_operator": "and",
        "group": [
          {
            "field": {
              "api_name": "module"
            },
            "comparator": "in",
            "value": [
              {
                "api_name": "Leads"
              },
              {
                "api_name": "Contacts"
              }
            ]
          },
          {
            "field": {
              "api_name": "action"
            },
            "comparator": "in",
            "value": [
              "added",
              "updated"
            ]
          }
        ]
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success

Successful audit log export job creation

```json
{
  "audit_log_export": [
    {
      "code": "SCHEDULED",
      "details": {
        "id": "1234567890"
      },
      "message": "Audit log export job scheduled successfully.",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFound

Request body is missing the audit_log_export key

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "status": "error",
  "message": "Required field missing",
  "details": {
    "api_name": "audit_log_export",
    "json_path": "$.audit_log_export[0]"
  }
}
```

### Status `400` — `application/json` — LimitExceeded

More than one audit_log_export item supplied

```json
{
  "audit_log_export": [
    {
      "code": "LIMIT_EXCEEDED",
      "status": "error",
      "message": "The audit_log_export jsonarray size should not exceed one",
      "details": {
        "api_name": "audit_log_export",
        "json_path": "$.audit_log_export[1]",
        "limit": "1"
      }
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowed

Audited time range exceeds 6 months

```json
{
  "audit_log_export": [
    {
      "code": "NOT_ALLOWED",
      "status": "error",
      "message": "Logs only within 6 month intervals are allowed to be fetched",
      "details": {
        "api_name": "value",
        "json_path": "$.audit_log_export[0].criteria.value"
      }
    }
  ]
}
```

### Status `400` — `application/json` — AlreadyScheduled

An export job is already scheduled

```json
{
  "audit_log_export": [
    {
      "code": "ALREADY_SCHEDULED",
      "status": "error",
      "message": "Export is already scheduled",
      "details": {
        "id": "4670092000004613003"
      }
    }
  ]
}
```

### Status `403` — `application/json` — NoPermission

User does not have the required profile permission

```json
{
  "status": "error",
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "details": {
    "permissions": [
      "profile permission"
    ]
  }
}
```
