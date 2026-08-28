# Examples: listCadencesRecordsCount

**GET /settings/automation/cadences/actions/records_count**

## Response examples

### Status `200` — `application/json` — Success200

Successful Cadence record counts response

```json
{
  "cadences_records_count": [
    {
      "count": 5,
      "cadences": {
        "name": "cadence",
        "id": "111112000000092007"
      }
    },
    {
      "count": 0,
      "cadences": {
        "name": "darft cadence",
        "id": "111112000000092270"
      }
    },
    {
      "count": 1,
      "cadences": {
        "name": "publish cadence",
        "id": "111112000000094004"
      }
    }
  ]
}
```

### Status `207` — `application/json` — Success207

Partial Cadence record counts response

```json
{
  "cadences_records_count": [
    {
      "count": 5,
      "cadences": {
        "name": "cadence",
        "id": "111112000000092007"
      }
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111112000000092000"
      },
      "message": "The id given seems to be invalid.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Invalid Cadence ID error

```json
{
  "cadences_records_count": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111112000000092001"
      },
      "message": "The id given seems to be invalid.",
      "status": "error"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111112000000092000"
      },
      "message": "The id given seems to be invalid.",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse1

No permission to retrieve Cadence record counts error

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_View_Cadences"
    ]
  },
  "message": "No permission",
  "status": "error"
}
```
