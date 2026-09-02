Multiple contacts with different approval states

```json
{
  "__conversion_options": {
    "module_preference": {
      "api_name": "Contacts",
      "id": "1041770000000002179"
    },
    "Contacts": [
      {
        "Full_Name": "abc",
        "Email": null,
        "Layout": {
          "name": "standard",
          "id": "1041770000000000001"
        },
        "Account_Name": null,
        "Locked__s": false,
        "$editable": true,
        "id": "1041770000009243193",
        "$approval_state": "approved",
        "Data_Processing_Basis": "null"
      },
      {
        "Full_Name": "abc",
        "Email": null,
        "Layout": {
          "name": "standard",
          "id": "1041770000000000001"
        },
        "Account_Name": null,
        "Locked__s": false,
        "$editable": true,
        "id": "1041770000009231053",
        "$approval_state": "approval_process_pending",
        "Data_Processing_Basis": "null"
      }
    ],
    "preference_field_matched_value": {
      "Contacts": [
        {
          "field": {
            "api_name": "Full_Name",
            "field_label": "Full Name",
            "unique": null,
            "id": "1041770000000002529"
          },
          "matched_lead_value": "abc"
        }
      ],
      "Accounts": null
    },
    "Accounts": null,
    "modules_with_multiple_layouts": null
  }
}
```
