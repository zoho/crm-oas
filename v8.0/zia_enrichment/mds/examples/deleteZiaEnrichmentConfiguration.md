# Examples: deleteZiaEnrichmentConfiguration

**DELETE /settings/zia/data_enrichment/{id}**

## Response examples

### Status `200` — `application/json` — Example

```json
{
  "data_enrichment": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "5667964000001485102"
      },
      "message": "enrichment deleted Successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Example1

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "the enrichment id given seems to be invalid.",
  "status": "error"
}
```

### Status `400` — `application/json` — Example2

```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Data Enrichment feature not enabled",
  "status": "error"
}
```

### Status `403` — `application/json` — Example

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Data_Enrichment"
    ]
  },
  "message": "No permission to access this feature",
  "status": "error"
}
```
