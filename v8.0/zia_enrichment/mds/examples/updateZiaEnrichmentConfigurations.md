# Examples: updateZiaEnrichmentConfigurations

**PUT /settings/zia/data_enrichment/{id}**

## Request examples

### `application/json` — Example

```json
{
  "data_enrichment": [
    {
      "output_data_field_mapping": [
        {
          "enrich_field": {
            "name": "name"
          },
          "crm_field": {
            "id": "917992000000000555",
            "api_name": "Company"
          }
        },
        {
          "enrich_field": {
            "name": "primary_email"
          },
          "crm_field": {
            "id": "917992000000000563",
            "api_name": "Email"
          }
        },
        {
          "enrich_field": {
            "name": "secondary_email"
          },
          "crm_field": {
            "id": "917992000000026003",
            "api_name": "Secondary_Email"
          }
        },
        {
          "enrich_field": {
            "name": "primary_contact"
          },
          "crm_field": {
            "id": "917992000000000565",
            "api_name": "Phone"
          }
        },
        {
          "enrich_field": {
            "name": "industries"
          },
          "crm_field": {
            "id": "917992000000000577",
            "api_name": "Industry"
          }
        },
        {
          "enrich_field": {
            "name": "social_media_skype"
          },
          "crm_field": {
            "id": "917992000000000587",
            "api_name": "Skype_ID"
          }
        },
        {
          "enrich_field": {
            "name": "social_media_twitter"
          },
          "crm_field": {
            "id": "917992000000035001",
            "api_name": "Twitter"
          }
        },
        {
          "enrich_field": {
            "name": "website"
          },
          "crm_field": {
            "id": "917992000000000571",
            "api_name": "Website"
          }
        },
        {
          "enrich_field": {
            "name": "description"
          },
          "crm_field": {
            "id": "917992000000000613",
            "api_name": "Description"
          }
        },
        {
          "enrich_field": {
            "name": "no_of_employees"
          },
          "crm_field": {
            "id": "917992000000000579",
            "api_name": "No_of_Employees"
          }
        },
        {
          "enrich_field": {
            "name": "revenue"
          },
          "crm_field": {
            "id": "917992000000000581",
            "api_name": "Annual_Revenue"
          }
        },
        {
          "enrich_field": {
            "name": "logo"
          },
          "crm_field": {
            "id": "917992000000179001",
            "api_name": "Record_Image"
          }
        },
        {
          "enrich_field": {
            "name": "address_street"
          },
          "crm_field": {
            "id": "917992000000000603",
            "api_name": "Street"
          }
        },
        {
          "enrich_field": {
            "name": "address_state"
          },
          "crm_field": {
            "id": "917992000000000607",
            "api_name": "State"
          }
        },
        {
          "enrich_field": {
            "name": "address_city"
          },
          "crm_field": {
            "id": "917992000000000605",
            "api_name": "City"
          }
        },
        {
          "enrich_field": {
            "name": "address_zip_code"
          },
          "crm_field": {
            "id": "917992000000000609",
            "api_name": "Zip_Code"
          }
        },
        {
          "enrich_field": {
            "name": "address_country"
          },
          "crm_field": {
            "id": "917992000000000611",
            "api_name": "Country"
          }
        },
        {
          "enrich_field": {
            "name": "org_type"
          },
          "crm_field": {
            "id": "917992000000000573",
            "api_name": "Lead_Source"
          }
        }
      ],
      "input_data_field_mapping": [
        {
          "enrich_field": {
            "name": "org_name"
          },
          "crm_field": {
            "id": "917992000000000555",
            "api_name": "Company"
          }
        },
        {
          "enrich_field": {
            "name": "email"
          },
          "crm_field": {
            "id": "917992000000000563",
            "api_name": "Email"
          }
        },
        {
          "enrich_field": {
            "name": "org_website"
          },
          "crm_field": {
            "id": "917992000000000571",
            "api_name": "Website"
          }
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Example

```json
{
  "data_enrichment": [
    {
      "code": "SUCCESS",
      "message": "enrichment updated successfully",
      "details": {
        "id": "{id}",
        "modified_time": "2023-08-10T15:12:10+05:30",
        "modified_by": {
          "id": "{id}",
          "name": "Krishna Prakash B"
        }
      },
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Example1

```json
{
  "data_enrichment": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "jsonarray",
        "api_name": "output_data_field_mapping || input_data_field_mapping",
        "json_path": "$.data_enrichment[0].(output_data_field_mapping || input_data_field_mapping)"
      },
      "message": "Invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example2

```json
{
  "data_enrichment": [
    {
      "code": "INVALID_DATA",
      "message": "the given type seems to be invalid",
      "details": {
        "api_name": "type",
        "json_path": "$.data_enrichment[0].type",
        "supported_values": [
          "organization",
          "personal"
        ]
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example4

```json
{
  "data_enrichment": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.data_enrichment[0].input_data_field_mapping[0].crm_field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.data_enrichment[0].output_data_field_mapping[0].crm_field.api_name"
          }
        ]
      },
      "message": "Crm field cannot be empty",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example6

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
