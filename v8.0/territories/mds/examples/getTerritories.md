# Examples: getTerritories

**GET /settings/territories**

## Response examples

### Status `200` — `application/json` — GetAllTerritories

Get all territories with pagination

```json
{
  "territories": [
    {
      "created_time": "2024-07-09T20:50:29+05:30",
      "permission_type": "read_only",
      "modified_time": "2024-07-09T20:50:29+05:30",
      "manager": {
        "name": "Patricia",
        "id": "2276164000000471001",
        "zuid": "8186088",
        "status": "active"
      },
      "api_name": "zoho",
      "name": "zoho",
      "modified_by": {
        "name": "Patricia",
        "id": "2276164000000471001"
      },
      "description": "Organization Parent Territory",
      "id": "2276164000001054020",
      "reporting_to": null,
      "created_by": {
        "name": "Patricia",
        "id": "2276164000000471001"
      }
    }
  ],
  "info": {
    "per_page": 1,
    "count": 0,
    "page": 1,
    "more_records": false
  }
}
```

### Status `200` — `application/json` — GetTerritoriesByIncludeParam

Get territories with criteria rules using the include parameter

```json
{
  "territories": [
    {
      "created_time": "2023-06-10T12:17:53+05:30",
      "manager": {
        "name": "J Smith",
        "id": "431581000000278001"
      },
      "account_rule_criteria": {
        "comparator": "equal",
        "field": {
          "api_name": "Billing_City",
          "id": "431581000000000657"
        },
        "value": "Chennai"
      },
      "description": null,
      "lead_rule_criteria": null,
      "reporting_to": {
        "name": "Zoho",
        "id": "431581000000272796"
      },
      "deal_rule_criteria": null,
      "created_by": {
        "name": "Patricia Boyle",
        "id": "431581000000258001"
      },
      "permission_type": "read_write_delete",
      "modified_time": "2023-06-10T12:23:23+05:30",
      "name": "Chennai",
      "modified_by": {
        "name": "Patricia Boyle",
        "id": "431581000000258001"
      },
      "id": "431581000000744113",
      "api_name": "Chennai"
    }
  ],
  "info": {
    "per_page": 1,
    "count": 0,
    "page": 1,
    "more_records": false
  }
}
```

### Status `200` — `application/json` — GetAllByIncludingIdsParam

Get territories filtered by specific IDs

```json
{
  "territories": [
    {
      "created_time": "2024-07-09T20:50:29+05:30",
      "permission_type": "read_only",
      "modified_time": "2024-07-09T20:50:29+05:30",
      "manager": {
        "name": "Patricia",
        "id": "2276164000000471001",
        "zuid": "8186088",
        "status": "active"
      },
      "api_name": "zoho",
      "name": "zoho",
      "modified_by": {
        "name": "Patricia",
        "id": "2276164000000471001"
      },
      "description": "Organization Parent Territory",
      "id": "2276164000001054020",
      "reporting_to": null,
      "created_by": {
        "name": "Patricia",
        "id": "2276164000000471001"
      }
    }
  ]
}
```

### Status `400` — `application/json` — TerritoryNotYetEnabled

Territory management not yet enabled error

```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Territory Management is not enabled",
  "status": "error"
}
```

### Status `400` — `application/json` — TerritoryDisabled

Territory management disabled error

```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Territory Management is disabled",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailure

Authentication failure

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```
