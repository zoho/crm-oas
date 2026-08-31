```json
{
  "data_enrichment": [
    {
      "id": "917992000008626019",
      "type": "organization",
      "module": {
        "id": "917992000000000125",
        "api_name": "Leads"
      },
      "status": true,
      "output_data_field_mapping": [
        {
          "enrich_field": {
            "name": "name",
            "display_label": "Organization Name"
          },
          "crm_field": {
            "id": "917992000000000555",
            "api_name": "Company",
            "name": "Company"
          }
        },
        {
          "enrich_field": {
            "name": "primary_email",
            "display_label": "Primary Email"
          },
          "crm_field": {
            "id": "917992000000000563",
            "api_name": "Email",
            "name": "Email"
          }
        },
        {
          "enrich_field": {
            "name": "secondary_email",
            "display_label": "Secondary Email"
          },
          "crm_field": {
            "id": "917992000000026003",
            "api_name": "Secondary_Email",
            "name": "Secondary Email"
          }
        },
        {
          "enrich_field": {
            "name": "primary_contact",
            "display_label": "Primary Contact Number"
          },
          "crm_field": {
            "id": "917992000000000565",
            "api_name": "Phone",
            "name": "Phone"
          }
        },
        {
          "enrich_field": {
            "name": "secondary_contact",
            "display_label": "Secondary Contact Number"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "industries",
            "display_label": "Industries"
          },
          "crm_field": {
            "id": "917992000000000577",
            "api_name": "Industry",
            "name": "Industry"
          }
        },
        {
          "enrich_field": {
            "name": "social_media_skype",
            "display_label": "Skype"
          },
          "crm_field": {
            "id": "917992000000000587",
            "api_name": "Skype_ID",
            "name": "Skype ID"
          }
        },
        {
          "enrich_field": {
            "name": "social_media_facebook",
            "display_label": "Facebook"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "social_media_twitter",
            "display_label": "X"
          },
          "crm_field": {
            "id": "917992000000035001",
            "api_name": "Twitter",
            "name": "Twitter"
          }
        },
        {
          "enrich_field": {
            "name": "social_media_other",
            "display_label": "Other social media link"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "website",
            "display_label": "Website"
          },
          "crm_field": {
            "id": "917992000000000571",
            "api_name": "Website",
            "name": "Website"
          }
        },
        {
          "enrich_field": {
            "name": "description",
            "display_label": "About the company"
          },
          "crm_field": {
            "id": "917992000000000613",
            "api_name": "Description",
            "name": "Description"
          }
        },
        {
          "enrich_field": {
            "name": "no_of_employees",
            "display_label": "Employee count"
          },
          "crm_field": {
            "id": "917992000000000579",
            "api_name": "No_of_Employees",
            "name": "No. of Employees"
          }
        },
        {
          "enrich_field": {
            "name": "revenue",
            "display_label": "Annual Revenue"
          },
          "crm_field": {
            "id": "917992000000000581",
            "api_name": "Annual_Revenue",
            "name": "Annual Revenue"
          }
        },
        {
          "enrich_field": {
            "name": "org_type",
            "display_label": "Business Type"
          },
          "crm_field": {
            "id": "917992000000000573",
            "api_name": "Lead_Source",
            "name": "Lead Source"
          }
        },
        {
          "enrich_field": {
            "name": "org_status",
            "display_label": "Business Size"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "years_in_industry",
            "display_label": "Year in business"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "territory_list",
            "display_label": "Business Locations"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "logo",
            "display_label": "LOGO"
          },
          "crm_field": {
            "id": "917992000000179001",
            "api_name": "Record_Image",
            "name": "Lead Image"
          }
        },
        {
          "enrich_field": {
            "name": "business_model",
            "display_label": "Business Model"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "head_quarters_country",
            "display_label": "Headquarters - Country"
          },
          "crm_field": null
        },
        {
          "enrich_field": {
            "name": "address_street",
            "display_label": "Address - Street"
          },
          "crm_field": {
            "id": "917992000000000603",
            "api_name": "Street",
            "name": "Street"
          }
        },
        {
          "enrich_field": {
            "name": "address_state",
            "display_label": "Address - State"
          },
          "crm_field": {
            "id": "917992000000000607",
            "api_name": "State",
            "name": "State"
          }
        },
        {
          "enrich_field": {
            "name": "address_city",
            "display_label": "Address - City"
          },
          "crm_field": {
            "id": "917992000000000605",
            "api_name": "City",
            "name": "City"
          }
        },
        {
          "enrich_field": {
            "name": "address_zip_code",
            "display_label": "Address - Zip Code"
          },
          "crm_field": {
            "id": "917992000000000609",
            "api_name": "Zip_Code",
            "name": "Zip Code"
          }
        },
        {
          "enrich_field": {
            "name": "address_country",
            "display_label": "Address - Country"
          },
          "crm_field": {
            "id": "917992000000000611",
            "api_name": "Country",
            "name": "Country"
          }
        }
      ],
      "input_data_field_mapping": [
        {
          "enrich_field": {
            "name": "org_name",
            "display_label": "Organization Name"
          },
          "crm_field": {
            "id": "917992000000000555",
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
            "id": "917992000000000563",
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
            "id": "917992000000000571",
            "api_name": "Website",
            "name": "Website"
          }
        }
      ],
      "modified_time": "2025-11-13T13:16:04+05:30",
      "modified_by": {
        "id": "917992000000417001",
        "name": "Brendon Caster"
      }
    }
  ]
}
```
