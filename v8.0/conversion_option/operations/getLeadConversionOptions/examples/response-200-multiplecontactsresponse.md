Conversion options with multiple matching contacts but no accounts

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
          "name": "new",
          "id": "1041770000003952003"
        },
        "Locked__s": false,
        "Account_Name": {
          "name": "xyz",
          "Locked__s": false,
          "id": "1041770000009242000"
        },
        "$editable": true,
        "id": "1041770000009231053",
        "$approval_state": "approved",
        "Data_Processing_Basis": "null"
      },
      {
        "Full_Name": "abc",
        "Email": null,
        "Layout": {
          "name": "new",
          "id": "1041770000003952003"
        },
        "Locked__s": false,
        "Account_Name": null,
        "$editable": true,
        "id": "1041770000009225124",
        "$approval_state": "approved",
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
    "modules_with_multiple_layouts": [
      {
        "api_name": "Contacts",
        "id": "1041770000000002179"
      },
      {
        "api_name": "Deals",
        "id": "1041770000000002181"
      }
    ]
  }
}
```
