# Examples: massDelete

**POST /{module}/actions/mass_delete**

## Request examples

### `application/json` — MultipleIds

An example of mass delete operation using multiple record IDs.

```json
{
  "ids": [
    "1990117000035827873",
    "1990117000035107169",
    "1990117000035107158",
    "1990117000035107147",
    "1990117000035107136",
    "1990117000035107125",
    "1990117000035107114",
    "1990117000035107103",
    "1990117000035107092",
    "1990117000035107081"
  ]
}
```

### `application/json` — CVIDAndTerritory

An example of mass delete operation using Custom View ID and territory filter.

```json
{
  "cvid": "3652397000000538003",
  "territory": {
    "id": "3652397000007622003",
    "include_child": true
  }
}
```

## Response examples

### Status `200` — `application/json` — MultipleRecordsDeleted

An example of multiple records deleted synchronously by record IDs.

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "1990117000035107169"
      },
      "message": "record is deleted",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "1990117000035827873"
      },
      "message": "record is deleted",
      "status": "success"
    }
  ]
}
```

### Status `200` — `application/json` — CVIDMassDeleteScheduled

An example of mass delete job scheduled using Custom View ID.

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "job_id": "1990117000035877396"
      },
      "message": "mass delete scheduled successfully",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — MixedResults

An example of partial success: some records deleted, others failed validation.

```json
{
  "data": [
    {
      "status": "success",
      "code": "SUCCESS",
      "message": "record is deleted",
      "details": {
        "id": "1990117000035107169"
      }
    },
    {
      "status": "error",
      "code": "INVALID_DATA",
      "message": "Record locked or invalid permissions",
      "details": {
        "id": "1990117000035827873"
      }
    }
  ]
}
```

### Status `400` — `application/json` — MissingRequiredField

An example of missing required field (ids or cvid).

```json
{
  "status": "error",
  "code": "MANDATORY_NOT_FOUND",
  "message": "required field not found",
  "details": {
    "api_name": "ids",
    "expected_data_type": "jsonarray"
  }
}
```

### Status `400` — `application/json` — InvalidCvid

Example of an invalid Custom View ID.

```json
{
  "status": "error",
  "code": "INVALID_DATA",
  "message": "the cvid given seems to be invalid",
  "details": {
    "api_name": "cvid",
    "json_path": "$.cvid",
    "id": "3652397000000538003"
  }
}
```

### Status `400` — `application/json` — InvalidDataType

Example of an invalid data type for ids field.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "ids",
    "json_path": "$.ids[0]",
    "id": "1990117000035827873"
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModule

An example of unsupported or invalid module name.

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

### Status `400` — `application/json` — OperationNotSupported

An example of mass delete not supported for this module.

```json
{
  "status": "error",
  "code": "NOT_SUPPORTED",
  "message": "Mass delete is not supported for this module",
  "details": {
    "resource_path_index": 0
  }
}
```

### Status `400` — `application/json` — NoRecordsFound

An example of no records found in the specified Custom View.

```json
{
  "status": "error",
  "code": "NO_RECORDS_FOUND",
  "message": "no record found to update",
  "details": {}
}
```

### Status `403` — `application/json` — NoPermission

Example of missing mass-delete permission for the module.

```json
{
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "status": "error",
  "details": {
    "permissions": [
      "Crm_Implied_Mass_Delete_Leads"
    ]
  }
}
```
