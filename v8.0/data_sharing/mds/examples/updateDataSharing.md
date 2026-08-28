# Examples: updateDataSharing

**PUT /settings/data_sharing**

## Request examples

### `application/json` — UpdateDataSharingRequestBody

Update Data Sharing Request Body

```json
{
  "data_sharing": [
    {
      "share_type": "private",
      "module": {
        "id": "111111000000002652",
        "api_name": "Leads"
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — UpdateDataSharingSuccessResponse

```json
{
  "data_sharing": [
    {
      "code": "SUCCESS",
      "details": {
        "module": "Leads"
      },
      "message": "data sharing settings updated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidSharingType

```json
{
  "data_sharing": [
    {
      "code": "INVALID_DATA",
      "details": {
        "regex": "private|public_read_only|public_read_write|public",
        "api_name": "share_type",
        "json_path": "$.data_sharing[0].share_type"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataType

```json
{
  "data_sharing": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
        "api_name": "api_name",
        "json_path": "$.data_sharing[0].module.api_name"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdateLimitExceeded

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 100,
    "api_name": "data_sharing",
    "json_path": "$.data_sharing"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModuleId

```json
{
  "data_sharing": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "module",
        "json_path": "$.data_sharing[0].module"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — PublicModuleInPortalsError

```json
{
  "data_sharing": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "module",
        "json_path": "$.data_sharing[0].module"
      },
      "message": "Cannot change the data sharing setting as module is made public in portals",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — DataSharingPutForbidden

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Data_Sharing"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
