# Examples: getAuditLogExportsById

**GET /settings/audit_log_export/{id}**

## Response examples

### Status `200` — `application/json` — Success

Successful retrieval of an audit log export job by ID

```json
{
  "audit_log_export": [
    {
      "criteria": {
        "field": {
          "api_name": "done_by"
        },
        "comparator": "equal",
        "value": [
          {
            "id": "123456",
            "name": "John Doe"
          }
        ]
      },
      "id": "1234567890",
      "status": "finished",
      "created_by": {
        "name": "John Doe",
        "id": "123456"
      },
      "download_links": [
        "https://example.com/download/1234567890"
      ],
      "job_start_time": "2023-01-01T00:00:00Z",
      "job_end_time": "2023-01-01T01:00:00Z",
      "expiry_date": "2023-01-08T00:00:00Z"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermission

User does not have the required profile permission

```json
{
  "status": "error",
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "details": {
    "permissions": [
      "profile permission"
    ]
  }
}
```

### Status `404` — `application/json` — NotFound

Export job ID not found

```json
{
  "code": "INVALID_URL_PATTERN",
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error",
  "details": {}
}
```
