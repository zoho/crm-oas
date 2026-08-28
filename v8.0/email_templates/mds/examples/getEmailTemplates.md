# Examples: getEmailTemplates

**GET /settings/email_templates**

## Response examples

### Status `200` — `application/json` — Success

Successful email templates list response

```json
{
  "email_templates": [
    {
      "id": "4019123000001797067",
      "name": "Abc12",
      "created_time": "2025-11-27T06:00:00Z",
      "modified_time": "2025-11-27T07:00:00Z",
      "last_usage_time": "2025-11-27T07:00:00Z",
      "category": "normal",
      "folder": {
        "id": "4019123000001797060",
        "name": "Default"
      },
      "module": {
        "api_name": "Inventory",
        "id": "4019123000001797064"
      },
      "created_by": {
        "id": "4019123000001797444",
        "name": "Alice"
      },
      "modified_by": {
        "id": "4019123000001797123",
        "name": "Bob"
      },
      "editor_mode": "plain_text",
      "favorite": false,
      "attachments": [
        {
          "size": "111",
          "file_name": "4019123000001450001.csv",
          "file_id": "v3zom53c15d05e77e43749f5982313b711a61",
          "id": "4019123000001797047"
        }
      ],
      "subject": "Template Subject",
      "associated": false,
      "active": true,
      "consent_linked": false,
      "last_version_statistics": {
        "tracked": 0,
        "delivered": 0,
        "opened": 0,
        "bounced": 0,
        "sent": 0,
        "clicked": 0
      }
    }
  ],
  "info": {
    "per_page": 20,
    "page": 1,
    "count": 1,
    "more_records": true
  }
}
```

### Status `400` — `application/json` — MissingParameter

Invalid sort_order parameter value

```json
{
  "code": "PATTERN_NOT_MATCHED",
  "message": "Please check whether the input values are correct",
  "status": "error",
  "details": {
    "param_name": "sort_order"
  }
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module name in request

```json
{
  "code": "INVALID_DATA",
  "message": "Module not found or not allowed",
  "status": "error",
  "details": {
    "param_name": "module"
  }
}
```
