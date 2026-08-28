# Examples: getRecordLockingInformationOfTheRecord

**GET /{moduleName}/{recordId}/Locking_Information__s**

## Response examples

### Status `200` — `application/json` — SuccessCase

Successful retrieval - manually locked record

```json
{
  "data": [
    {
      "Locked_By__s": {
        "name": "priya v",
        "id": "111111000000047487"
      },
      "$field_states": null,
      "Record_Locking_Rule_Id__s": null,
      "Locked_For__s": {
        "module": {
          "api_name": "Deals",
          "id": "111111000000000048"
        },
        "name": "locked",
        "id": "111111000000053560"
      },
      "Locked_Reason__s": "fff",
      "Record_Locking_Configuration_Id__s": "111111000000053641",
      "$editable": true,
      "id": "111111000000054020",
      "$sharing_permission": "full_access",
      "Lock_Source__s": "Manual",
      "Locked_Time__s": "2021-07-21T18:08:12+05:30",
      "Feature_Type__s": "record_locking",
      "$zia_visions": null
    }
  ],
  "info": {
    "per_page": 200,
    "count": 1,
    "page": 1,
    "more_records": false
  }
}
```

### Status `200` — `application/json` — AutomaticLockCase

Successful retrieval - automatically locked record (locked by a record locking rule)

```json
{
  "data": [
    {
      "Locked_By__s": null,
      "$field_states": null,
      "Record_Locking_Rule_Id__s": "111111000000054290",
      "Locked_For__s": {
        "module": {
          "api_name": "Deals",
          "id": "111111000000000048"
        },
        "name": "locked",
        "id": "111111000000053560"
      },
      "Locked_Reason__s": null,
      "Record_Locking_Configuration_Id__s": "111111000000053641",
      "$editable": false,
      "id": "111111000000054022",
      "$sharing_permission": "read_only",
      "Lock_Source__s": "Automatic",
      "Locked_Time__s": "2021-07-21T18:08:12+05:30",
      "Feature_Type__s": "record_locking",
      "$zia_visions": null
    }
  ],
  "info": {
    "per_page": 200,
    "count": 1,
    "page": 1,
    "more_records": false
  }
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
