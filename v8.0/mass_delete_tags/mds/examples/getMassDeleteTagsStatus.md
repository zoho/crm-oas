# Examples: getMassDeleteTagsStatus

**GET /settings/tags/actions/mass_delete**

## Response examples

### Status `200` — `application/json` — Sample

An example of in-progress mass delete tag job status.

```json
{
  "mass_delete": [
    {
      "job_id": "job_789",
      "status": "in_progress",
      "created_time": "2025-11-21T18:00:00Z"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidJobId

Invalid job ID supplied as a literal null string

```json
{
  "mass_delete": [
    {
      "code": "INVALID_DATA",
      "status": "error",
      "message": "invalid data",
      "details": {
        "job_id": "null"
      }
    }
  ]
}
```

### Status `400` — `application/json` — JobNotFound

Job ID does not match any scheduled mass delete tag job

```json
{
  "mass_delete": [
    {
      "code": "INVALID_DATA",
      "status": "error",
      "message": "job details not found",
      "details": {
        "job_id": "999999999999999999"
      }
    }
  ]
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

An example of OAuth scope missing the tags read permission.

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "status": "error",
  "message": "invalid oauth scope to access this URL",
  "details": {
    "method": "GET",
    "url": "/crm/v8/settings/tags/actions/mass_delete"
  }
}
```

### Status `403` — `application/json` — NoPermission

User profile lacks the tag management permission

```json
{
  "code": "NO_PERMISSION",
  "status": "error",
  "message": "permission denied",
  "details": {
    "permissions": [
      "Crm_Implied_Edit_Tags"
    ]
  }
}
```
