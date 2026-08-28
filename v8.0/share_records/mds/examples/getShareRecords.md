# Examples: getShareRecords

**GET /{moduleApiName}/{recordId}/actions/share**

## Response examples

### Status `200` — `application/json` — GetShareRecordsSuccess

An example response of active share entries on a record.

```json
{
  "share": [
    {
      "shared_with": {
        "name": "Manager",
        "id": "2922942000000015969",
        "type": "roles"
      },
      "share_related_records": false,
      "shared_through": {
        "module": {
          "name": "Leads",
          "id": "2922942000000000125"
        },
        "id": "2922942000003922003"
      },
      "shared_time": "2025-12-31T13:36:56+05:30",
      "permission": "full_access",
      "shared_by": {
        "name": "we edited1",
        "id": "2922942000000512001",
        "zuid": "76602839"
      },
      "type": "private"
    }
  ]
}
```

### Status `400` — `application/json` — ViewParamWithManageValue

An example of invalid value for the **view** query parameter.

```json
{
  "code": "PATTERN_NOT_MATCHED",
  "details": {
    "api_name": "view"
  },
  "message": "Please check whether the input values are correct",
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

### Status `403` — `application/json` — GetShareRecordsForbidden

An example of permission denied to read share details.

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "permission denied - access the api",
  "status": "error"
}
```

### Status `403` — `application/json` — RecordNoPermission

An example of record-level permission missing.

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_View_Leads"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
