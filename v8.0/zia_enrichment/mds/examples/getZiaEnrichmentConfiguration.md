# Examples: getZiaEnrichmentConfiguration

**GET /settings/zia/data_enrichment**

## Response examples

### Status `200` — `application/json` — Example

Successful retrieval of data enrichment configurations

```json
{
  "data_enrichment": [
    {
      "id": "111113000000063801",
      "type": "personal",
      "module": {
        "id": "111113000000002411",
        "api_name": "Contacts"
      },
      "status": true,
      "input_data_field_mapping": [
        {
          "enrich_field": {
            "name": "email",
            "display_label": "Email"
          },
          "crm_field": {
            "id": "111113000000004139",
            "api_name": "Email",
            "name": "Email"
          }
        },
        {
          "enrich_field": {
            "name": "org_website",
            "display_label": "Website"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "org_name",
            "display_label": "Organization Name"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "facebook",
            "display_label": "facebook"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "twitter",
            "display_label": "X"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "linkedin",
            "display_label": "LinkedIn"
          },
          "crm_field": null
        }
      ],
      "created_time": "2024-04-15T10:01:22+05:30",
      "created_by": {
        "id": "111113000000053889",
        "name": "Krishna Prakash"
      },
      "modified_time": "2024-04-15T10:01:22+05:30",
      "modified_by": {
        "id": "111113000000053889",
        "name": "Krishna Prakash"
      }
    },
    {
      "id": "111113000000063807",
      "type": "personal",
      "module": {
        "id": "111113000000002413",
        "api_name": "Accounts"
      },
      "status": true,
      "input_data_field_mapping": [
        {
          "enrich_field": {
            "name": "email",
            "display_label": "Email"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "org_website",
            "display_label": "Website"
          },
          "crm_field": {
            "id": "111113000000004033",
            "api_name": "Website",
            "name": "Website"
          }
        },
        {
          "enrich_field": {
            "name": "org_name",
            "display_label": "Organization Name"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "facebook",
            "display_label": "facebook"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "twitter",
            "display_label": "X"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "linkedin",
            "display_label": "LinkedIn"
          },
          "crm_field": null
        }
      ],
      "created_time": "2024-04-15T10:01:38+05:30",
      "created_by": {
        "id": "111113000000053889",
        "name": "Krishna Prakash"
      },
      "modified_time": "2024-04-15T10:01:38+05:30",
      "modified_by": {
        "id": "111113000000053889",
        "name": "Krishna Prakash"
      }
    },
    {
      "id": "111113000000072003",
      "type": "organization",
      "module": {
        "id": "111113000000002409",
        "api_name": "Leads"
      },
      "status": true,
      "input_data_field_mapping": [
        {
          "enrich_field": {
            "name": "org_name",
            "display_label": "Organization Name"
          },
          "crm_field": {
            "id": "111113000000004369",
            "api_name": "Company",
            "name": "Company"
          }
        },
        {
          "enrich_field": {
            "name": "email",
            "display_label": "Email"
          },
          "crm_field": {
            "id": "111113000000004379",
            "api_name": "Email",
            "name": "Email"
          }
        },
        {
          "enrich_field": {
            "name": "org_website",
            "display_label": "Website"
          },
          "crm_field": {
            "id": "111113000000004387",
            "api_name": "Website",
            "name": "Website"
          }
        }
      ],
      "created_time": "2024-04-15T13:07:01+05:30",
      "created_by": {
        "id": "111113000000053889",
        "name": "Krishna Prakash"
      },
      "modified_time": "2024-04-15T13:07:01+05:30",
      "modified_by": {
        "id": "111113000000053889",
        "name": "Krishna Prakash"
      }
    }
  ]
}
```

### Status `400` — `application/json` — Example

Feature not enabled error

```json
{
  "code": "FEATURE_NOT_ENABLED",
  "details": {},
  "message": "Data Enrichment feature not enabled",
  "status": "error"
}
```

### Status `403` — `application/json` — Example

No permission to access feature

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Data_Enrichment",
      "Crm_Implied_View_Data_Enrichment"
    ]
  },
  "message": "No permission to access this feature",
  "status": "error"
}
```
