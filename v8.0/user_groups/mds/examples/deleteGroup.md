# Examples: deleteGroup

**DELETE /settings/user_groups/{group}**

## Response examples

### Status `200` — `application/json` — SuccessWithId

User group deleted immediately

```json
{
  "user_groups": [
    {
      "code": "SUCCESS",
      "message": "User group deleted successfully",
      "status": "success",
      "details": {
        "id": "3652397000009949005"
      }
    }
  ]
}
```

### Status `200` — `application/json` — ScheduledWithJobId

Deletion scheduled with job ID

```json
{
  "user_groups": [
    {
      "code": "SCHEDULED",
      "message": "User group deletion has been scheduled",
      "status": "scheduled",
      "details": {
        "job_id": "3652397000009950001"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidData

Invalid group ID in request URL

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "The provided group ID is invalid.",
  "status": "error"
}
```

### Status `400` — `application/json` — MissingGroupId

Missing group ID in request URL

```json
{
  "user_groups": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "param_name": "ids"
      },
      "message": "Group ID missing in URL",
      "status": "error"
    }
  ]
}
```

### Status `404` — `application/json` — InvalidData

Invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "The provided group ID is invalid.",
  "status": "error"
}
```
