# Examples: createShareRecords

**POST /{moduleApiName}/{recordId}/actions/share**

## Request examples

### `application/json` — CreateShareRecordsRequest

An example response of share a record with a role.

```json
{
  "share": [
    {
      "shared_with": {
        "id": "111111000000000874",
        "type": "roles"
      },
      "share_related_records": false,
      "permission": "full_access",
      "type": "private"
    }
  ],
  "notify_shared_members": false,
  "notify_on_completion": true
}
```

## Response examples

### Status `201` — `application/json` — CreateShareRecordsSuccess

An example of successful share response.

```json
{
  "share": [
    {
      "code": "SUCCESS",
      "details": {},
      "message": "record will be shared successfully",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — CreateShareRecordsPartialSuccess

An example of partial success response with one valid and one invalid entry.

```json
{
  "share": [
    {
      "code": "SUCCESS",
      "details": {},
      "message": "record will be shared successfully",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "shared_with",
        "json_path": "$.share[1].shared_with"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidShareWithValue

`shared_with` value invalid for the given type

```json
{
  "share": [
    {
      "code": "INVALID_DATA",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.share[0].type"
        },
        "api_name": "shared_with",
        "json_path": "$.share[0].shared_with"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidRecordId

Invalid record ID in the URL

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "ENTITY_ID_INVALID",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidShareWithUserId

Invalid user ID in `shared_with`

```json
{
  "share": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.share[0].shared_with.id"
      },
      "message": "invalid user Id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ActivityModuleRelatedIssue

`share_related_records` not supported on the module

```json
{
  "share": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "share_related_records",
        "json_path": "$.share[0].share_related_records"
      },
      "message": "cannot share the related records",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryParamMissing

Mandatory field missing in a share entry

```json
{
  "share": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "permission",
        "json_path": "$.share[0].permission"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NonSubordinateUser

Cannot share with a non-subordinate user

```json
{
  "share": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "shared_with",
        "json_path": "$.share[0].shared_with"
      },
      "message": "cannot share to the user",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — CreateShareRecordsForbidden

An example of permission denied to access the share API.

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "permission denied - access the api",
  "status": "error"
}
```

### Status `403` — `application/json` — SchedularAlreadyRunning

An example of share operation already in progress.

```json
{
  "code": "CANNOT_PROCESS",
  "details": {},
  "message": "Scheduler is running",
  "status": "error"
}
```

### Status `403` — `application/json` — SharingSharedRecord

An example attempt to re-share a shared record.

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "Shared record cannot be shared to other users",
  "status": "error"
}
```

### Status `403` — `application/json` — RecordLevelSharingNotSupportedForModule

An example of record-level sharing unsupported for the module.

```json
{
  "code": "NOT_ALLOWED",
  "details": {},
  "message": "Record Level Sharing is not supported for this module",
  "status": "error"
}
```

### Status `403` — `application/json` — NotifySharedMembersWithoutFeeds

An example of notification requested without Feeds enabled.

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "api_name": "notify_shared_members",
    "json_path": "$.notify_shared_members"
  },
  "message": "Feeds is not enabled for this org",
  "status": "error"
}
```
