# Examples: deleteShareRecords

**DELETE /{moduleApiName}/{recordId}/actions/share**

## Response examples

### Status `200` — `application/json` — RevokeSharingSuccess

An example response for sharing revoked successfully.

```json
{
  "share": {
    "code": "SUCCESS",
    "details": {
      "id": "2922942000003922003"
    },
    "message": "Sharing Revoked",
    "status": "success"
  }
}
```

### Status `400` — `application/json` — NoSharingThroughTheRecord

An example response for when no sharing exists to revoke.

```json
{
  "code": "CANNOT_PROCESS",
  "details": {},
  "message": "No sharing through this record is available to revoke",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRecordId

An example of invalid record ID in the URL.

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

### Status `400` — `application/json` — InvalidModuleName

An example of invalid module API name in the URL.

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "resource_path_index": 0
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `403` — `application/json` — RevokeSharingForbidden

Permission denied to revoke sharing

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "permission denied - access the api",
  "status": "error"
}
```
