# Examples: massUpdateRecords

**POST /{module}/actions/mass_update**

## Request examples

### `application/json` — BasicFieldUpdate

Example of updating a single field across multiple records.

```json
{
  "data": [
    {
      "Venue": "Estancia"
    }
  ],
  "ids": [
    "1990117000035808053",
    "1990117000035808020"
  ]
}
```

### `application/json` — NestedObjectUpdate

An example of updating fields that reference nested objects.

```json
{
  "data": [
    {
      "Pipeline": "1990117000027199960",
      "Stage": "Value Proposition",
      "Layout": {
        "id": "1990117000000095023",
        "display_label": "Standard"
      }
    }
  ],
  "ids": [
    "1990117000035107169"
  ]
}
```

### `application/json` — CvidUpdate

An example of scheduling an asynchronous mass update using a Custom View.

```json
{
  "data": [
    {
      "Age": "12121"
    }
  ],
  "cvid": "1990117000000091529"
}
```

## Response examples

### Status `200` — `application/json` — SuccessfulMassUpdate

An example of successful synchronous mass update of a record.

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2025-11-26T14:37:55+05:30",
        "Modified_By": {
          "name": "Dharun Kumar Dharun Kumar 95",
          "id": "1990117000000450001"
        },
        "Created_Time": "2025-11-25T15:07:02+05:30",
        "id": "1990117000035808053",
        "Created_By": {
          "name": "Dharun Kumar Dharun Kumar 95",
          "id": "1990117000000450001"
        }
      },
      "message": "record updated",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — PartialMassUpdate

An example of two records updated successfully and one record failing.

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-08-12T19:02:29+05:30",
        "Modified_By": {
          "name": "Dharun Kumar Dharun Kumar 95",
          "id": "1990117000000450001"
        },
        "Created_Time": "2026-08-04T17:55:37+05:30",
        "id": "1990117000045575047",
        "Created_By": {
          "name": "Dharun Kumar Dharun Kumar 95",
          "id": "1990117000000450001"
        }
      },
      "message": "record updated",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2026-08-12T19:02:29+05:30",
        "Modified_By": {
          "name": "Dharun Kumar Dharun Kumar 95",
          "id": "1990117000000450001"
        },
        "Created_Time": "2026-08-04T17:55:54+05:30",
        "id": "1990117000045575059",
        "Created_By": {
          "name": "Dharun Kumar Dharun Kumar 95",
          "id": "1990117000000450001"
        }
      },
      "message": "record updated",
      "status": "success"
    },
    {
      "code": "RECORD_LOCKED",
      "details": {
        "action": "record_locking",
        "id": "1990117000045639003"
      },
      "message": "Sorry, you cannot perform this operation as the record is locked.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NoRecordsFound

Example of a record ID supplied in the request is invalid.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "19901170000358080"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryFieldMissing

An example of mandatory field missing in the payload.

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {},
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidFieldValue

An example of picklist value not present in the record layout.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Pipeline",
        "id": "1990117000035827873"
      },
      "message": "picklist not found in record layout",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NonSubordinateUser

An example of non-subordinate user assigned to a user lookup field.

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.data[0].User_lookup.id"
      },
      "message": "Non Subordinate User Found",
      "status": "error"
    }
  ]
}
```
