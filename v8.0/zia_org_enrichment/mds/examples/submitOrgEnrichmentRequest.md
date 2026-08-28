# Examples: submitOrgEnrichmentRequest

**POST /__zia_org_enrichment**

## Request examples

### `application/json` — Example1

Schedule enrichment with name, email, and website

```json
{
  "__zia_org_enrichment": [
    {
      "enrich_based_on": {
        "name": "zoho",
        "email": "sales@zohocorp.com",
        "website": "www.zoho.com"
      }
    }
  ]
}
```

## Response examples

### Status `202` — `application/json` — Example

Enrichment job scheduled

```json
{
  "__zia_org_enrichment": [
    {
      "code": "SCHEDULED",
      "details": {
        "id": "917992000008742464"
      },
      "message": "Org Enrichment scheduled successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Example

Invalid value in enrich_based_on

```json
{
  "__zia_org_enrichment": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
        "api_name": "name",
        "json_path": "$.__zia_org_enrichment[0].enrich_based_on.name"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example2

Enrichment limit exceeded

```json
{
  "__zia_org_enrichment": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 1500,
        "limit_due_to": [
          {
            "api_name": "enrich_based_on",
            "json_path": "$.__zia_org_enrichment[0].enrich_based_on"
          }
        ]
      },
      "message": "enrichment data limit exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example3

Expected trigger fields missing

```json
{
  "__zia_org_enrichment": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "name",
            "json_path": "$.__zia_org_enrichment[0].enrich_based_on.name"
          },
          {
            "api_name": "email",
            "json_path": "$.__zia_org_enrichment[0].enrich_based_on.email"
          },
          {
            "api_name": "website",
            "json_path": "$.__zia_org_enrichment[0].enrich_based_on.website"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example4

Module not supported

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "module"
  },
  "message": "The given module is not supported for Org Enrichment",
  "status": "error"
}
```

### Status `400` — `application/json` — Example5

Data enrichment feature not enabled

```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Data Enrichment feature not enabled",
  "status": "error"
}
```

### Status `400` — `application/json` — Example6

Array cardinality exceeded

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "__zia_org_enrichment",
    "json_path": "$.__zia_org_enrichment"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `403` — `application/json` — Example

Permission denied

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "No permission to access this feature",
  "status": "error"
}
```
