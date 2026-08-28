# Examples: createFields

**POST /settings/fields**

## Request examples

### `application/json` — FullExample

Creates a single-line text field and a multi-line text area field in one request

```json
{
  "fields": [
    {
      "field_label": "Your Name",
      "data_type": "text",
      "tooltip": {
        "name": "static_text",
        "value": "Enter your name"
      },
      "profiles": [
        {
          "id": "2423488000000015972",
          "permission_type": "read_write"
        },
        {
          "id": "2423488000000015975",
          "permission_type": "read_only"
        }
      ],
      "external": {
        "type": "user",
        "show": false
      },
      "crypt": {
        "mode": "decryption"
      }
    },
    {
      "field_label": "Name",
      "data_type": "textarea",
      "length": 50000,
      "textarea": {
        "type": "rich_text"
      },
      "tooltip": {
        "name": "static_text",
        "value": "Enter your name"
      },
      "profiles": [
        {
          "id": "2423488000000015972",
          "permission_type": "read_write"
        },
        {
          "id": "2423488000000015975",
          "permission_type": "read_write"
        }
      ]
    },
    {
      "field_label": "Email address",
      "data_type": "email",
      "tooltip": {
        "name": "static_text",
        "value": "Enter email address"
      },
      "crypt": {
        "mode": "decryption"
      },
      "unique": {
        "case_sensitive": false
      },
      "hipaa_compliance_enabled": true,
      "private": {
        "type": "High"
      }
    },
    {
      "field_label": "Phone",
      "data_type": "phone",
      "association_details": {
        "related_field": {
          "api_name": "Phone",
          "id": "4832675000000710341"
        },
        "lookup_field": {
          "reference_id": "{{ref8909}}"
        }
      }
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — FullExample

Successful field creation response with IDs for each created field

```json
{
  "fields": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000067259"
      },
      "message": "field created",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "11111200000006724"
      },
      "message": "field created",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000067239"
      },
      "message": "field created",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — PartialSuccess

Mixed result with one field created successfully and one rejected with INVALID_DATA

```json
{
  "fields": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "1947368000002460003"
      },
      "message": "field created",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "data_type",
        "json_path": "$.fields[1].data_type"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ErrorExample

```json
{
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "details": {},
  "status": "error"
}
```

### Status `500` — `application/json` — ErrorExample

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```
