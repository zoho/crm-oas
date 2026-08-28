# Examples: getRecordLockingInformationById

**GET /{moduleName}/{recordId}/Locking_Information__s/{lockId}**

## Response examples

### Status `200` — `application/json` — SuccessCase

Successful locking information retrieval by ID

```json
{
  "data": [
    {
      "Locked_By__s": null,
      "Locked_For__s": {
        "module": {
          "api_name": "Leads",
          "id": "1961304000000000125"
        },
        "name": "Test",
        "id": "1961304000010927002"
      },
      "$field_states": null,
      "Locked_Reason__s": null,
      "$editable": false,
      "$sharing_permission": "read_only",
      "Lock_Source__s": "Automatic",
      "Locked_Time__s": "2026-06-28T23:00:07+05:30",
      "Record_Locking_Configuration_Id__s": "1961304000010324013",
      "Record_Locking_Rule_Id__s": "1961304000011000517",
      "id": "1961304000011003523",
      "Feature_Type__s": "record_locking",
      "$zia_visions": null
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataRelationNotFound

Relation not found error

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "relation not found",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidMainModule

Invalid module name error

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

### Status `400` — `application/json` — InvalidDataMainRecordId

Invalid record ID error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "the related id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedLockConfigMissing

Locking configuration missing error

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 2
  },
  "message": "Required Record Locking Configuration is not present",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermission

No permission error

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "resource_path_index": 1
  },
  "message": "Record Locking Configuration is not supported for the profile of the user",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidUrlPattern

Invalid URL pattern error

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```
