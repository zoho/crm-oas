# Examples: getZiaOrgEnrichment

**GET /__zia_org_enrichment**

## Response examples

### Status `200` — `application/json` — Example1

Enrichment jobs returned

```json
{
  "__zia_org_enrichment": [
    {
      "id": "111111000000075013",
      "status": "SCHEDULED",
      "created_time": "2023-07-31T01:00:26Z",
      "created_by": {
        "id": "111111000000050755",
        "name": "Krishna Prakash"
      }
    },
    {
      "id": "111111000000075024",
      "status": "SCHEDULED",
      "created_time": "2023-07-31T01:05:15Z",
      "created_by": {
        "id": "111111000000050755",
        "name": "Krishna Prakash"
      }
    },
    {
      "id": "111111000000075026",
      "status": "SCHEDULED",
      "created_time": "2023-07-31T01:05:50Z",
      "created_by": {
        "id": "111111000000050755",
        "name": "Krishna Prakash"
      }
    },
    {
      "id": "111111000000072009",
      "status": "DATA_NOT_FOUND",
      "created_time": "2023-07-28T05:06:40Z",
      "created_by": {
        "id": "111111000000050755",
        "name": "Krishna Prakash"
      }
    }
  ],
  "info": {
    "per_page": 200,
    "count": 15,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — Example1

Feature not supported

```json
{
  "code": "FEATURE_NOT_SUPPORTED",
  "details": {},
  "message": "Your License does not support this feature",
  "status": "error"
}
```

### Status `400` — `application/json` — Example2

Invalid query parameter value

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param": "status",
    "supported_values": [
      "COMPLETED",
      "SCHEDULED",
      "FAILED",
      "RUNNING",
      "DATA_NOT_FOUND",
      "UPDATED"
    ]
  },
  "message": "status value invalid",
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
