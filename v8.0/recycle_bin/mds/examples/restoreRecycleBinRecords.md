# Examples: restoreRecycleBinRecords

**POST /settings/recycle_bin/actions/restore**

## Request examples

### `application/json` — RestoreByIds

Restore specific records by IDs

```json
{
  "ids": [
    "111111000000077729",
    "111111000000077734"
  ]
}
```

### `application/json` — RestoreByFilters

Restore records matching filter criteria

```json
{
  "filters": {
    "group_operator": "AND",
    "group": [
      {
        "field": {
          "api_name": "display_name"
        },
        "comparator": "contains",
        "value": "Amazon Marketplace"
      },
      {
        "field": {
          "api_name": "module"
        },
        "comparator": "equal",
        "value": "Leads"
      }
    ]
  }
}
```

### `application/json` — RestoreAll

Restore all records

```json
{
  "restore_all_records": true
}
```

## Response examples

### Status `200` — `application/json` — ImmediateSuccess

Immediate restoration success

```json
{
  "recycle_bin": [
    {
      "status": "success",
      "code": "SUCCESS",
      "message": "record restored",
      "details": {
        "id": "111111000000077729"
      }
    }
  ]
}
```

### Status `202` — `application/json` — ScheduledByIds

Restoration scheduled for specific IDs

```json
{
  "recycle_bin": [
    {
      "code": "SCHEDULED",
      "details": {
        "id": "111111000000077729"
      },
      "message": "record has been scheduled for restoration",
      "status": "success"
    },
    {
      "code": "SCHEDULED",
      "details": {
        "id": "111111000000077734"
      },
      "message": "record has been scheduled for restoration",
      "status": "success"
    }
  ]
}
```

### Status `202` — `application/json` — ScheduledByFilters

Bulk restoration scheduled based on filters

```json
{
  "recycle_bin": [
    {
      "code": "SCHEDULED",
      "details": {},
      "message": "Bulk restoration of records based on filters has been scheduled",
      "status": "success"
    }
  ]
}
```

### Status `202` — `application/json` — ScheduledRestoreAll

All records scheduled for restoration

```json
{
  "recycle_bin": [
    {
      "code": "SCHEDULED",
      "details": {},
      "message": "Bulk restoration of records based on filters has been scheduled",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — MultiStatusResponse

```json
{
  "recycle_bin": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4794080000003274845"
      },
      "message": "record restored",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "1000000000000"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "comparator",
    "json_path": "$.comparator",
    "param_name": "filters"
  },
  "message": "Please provide a valid comparator",
  "status": "error"
}
```
