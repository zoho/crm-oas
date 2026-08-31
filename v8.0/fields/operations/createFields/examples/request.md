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
