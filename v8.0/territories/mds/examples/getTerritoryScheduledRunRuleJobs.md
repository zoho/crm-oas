# Examples: getTerritoryScheduledRunRuleJobs

**GET /settings/territories/actions/scheduled_run_rule_jobs**

## Response examples

### Status `200` — `application/json` — JobStatusInProgress

Run rule job in progress

```json
{
  "scheduled_run_rule_jobs": {
    "status": "IN_PROGRESS",
    "job_id": "482367546723546372",
    "scheduled_time": "2026-03-22T10:30:00+05:30",
    "scheduled_by": {
      "name": "John Doe",
      "id": "3477061000000002001"
    }
  }
}
```

### Status `200` — `application/json` — JobStatusCompleted

Run rule job completed

```json
{
  "scheduled_run_rule_jobs": {
    "status": "COMPLETED",
    "job_id": "482367546723546372",
    "scheduled_time": "2026-03-22T10:30:00+05:30",
    "scheduled_by": {
      "name": "John Doe",
      "id": "3477061000000002001"
    }
  }
}
```

### Status `200` — `application/json` — JobStatusFailed

Run rule job failed

```json
{
  "scheduled_run_rule_jobs": {
    "status": "FAILED",
    "job_id": "482367546723546372",
    "scheduled_time": "2026-03-22T10:30:00+05:30",
    "scheduled_by": {
      "name": "John Doe",
      "id": "3477061000000002001"
    }
  }
}
```

### Status `400` — `application/json` — TerritoryNotYetEnabled

Territory management not yet enabled error

```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Territory Management is not enabled",
  "status": "error"
}
```

### Status `400` — `application/json` — TerritoryDisabled

Territory management disabled error

```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Territory Management is disabled",
  "status": "error"
}
```

### Status `400` — `application/json` — RequiredParamMissing

Required parameter job_id missing from the request

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "job_id"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailure

Authentication failure error

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```
