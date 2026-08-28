# Examples: getLeadConversionOptions

**GET /Leads/{leadId}/__conversion_options**

## Response examples

### Status `200` — `application/json` — ConversionOptionsResponse

Conversion options with matched contacts and accounts

```json
{
  "__conversion_options": {
    "module_preference": {
      "api_name": "Accounts",
      "id": "1041770000000002177"
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
      "Accounts": [
        {
          "field": {
            "api_name": "Account_Name",
            "field_label": "Account Name",
            "unique": null,
            "id": "1041770000000002425"
          },
          "matched_lead_value": "xyz"
        }
      ]
    },
    "Accounts": [
      {
        "Phone": null,
        "Account_Type": null,
        "Locked__s": false,
        "Website": null,
        "Account_Name": "xyz",
        "$editable": true,
        "id": "1041770000009242000",
        "$approval_state": "approved"
      }
    ],
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

### Status `200` — `application/json` — NoMatchingRecordsResponse

Conversion options when no matching contacts or accounts are found

```json
{
  "__conversion_options": {
    "module_preference": null,
    "Contacts": null,
    "preference_field_matched_value": null,
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

### Status `200` — `application/json` — MultipleContactsResponse

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

### Status `200` — `application/json` — MinimalOptionsResponse

Conversion options with only layout information available

```json
{
  "__conversion_options": {
    "module_preference": null,
    "Contacts": null,
    "preference_field_matched_value": null,
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

### Status `200` — `application/json` — ContactWithSpecialStatesResponse

Contact with approval pending, data processing stopped, and record locked

```json
{
  "__conversion_options": {
    "module_preference": {
      "api_name": "Contacts",
      "id": "111111000000000044"
    },
    "Contacts": [
      {
        "Full_Name": "zoho",
        "Email": null,
        "Layout": {
          "name": "standard",
          "id": "111111000000000001"
        },
        "Account_Name": null,
        "$editable": true,
        "$approval_state": "approval_process_pending",
        "Data_Processing_Basis": "Consent - Stop Processing",
        "Locked__s": true,
        "id": "111111000000055377"
      }
    ],
    "preference_field_matched_value": {
      "Contacts": [
        {
          "field": {
            "api_name": "Full_Name",
            "field_label": "Full Name",
            "unique": null,
            "id": "111111000000002478"
          },
          "matched_lead_value": "zoho"
        }
      ],
      "Accounts": null
    },
    "Accounts": null,
    "modules_with_multiple_layouts": null
  }
}
```

### Status `200` — `application/json` — ContactWithAccountSpecialStatesResponse

Contact with associated account, approval pending, data processing stopped, and record locked

```json
{
  "__conversion_options": {
    "module_preference": {
      "api_name": "Contacts",
      "id": "111111000000000044"
    },
    "Contacts": [
      {
        "Full_Name": "zoho",
        "Email": null,
        "Layout": {
          "name": "standard",
          "id": "111111000000000001"
        },
        "Account_Name": {
          "name": "zoho",
          "id": "111111000000055373",
          "Locked__s": false
        },
        "$editable": true,
        "$approval_state": "approval_process_pending",
        "Data_Processing_Basis": "Consent - Stop Processing",
        "Locked__s": true,
        "id": "111111000000055377"
      }
    ],
    "preference_field_matched_value": {
      "Contacts": [
        {
          "field": {
            "api_name": "Full_Name",
            "field_label": "Full Name",
            "unique": null,
            "id": "111111000000002478"
          },
          "matched_lead_value": "zoho"
        }
      ],
      "Accounts": null
    },
    "Accounts": null,
    "modules_with_multiple_layouts": null
  }
}
```

### Status `200` — `application/json` — ContactMinimalFieldsResponse

Contact with minimal fields and approval pending state

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
      ]
    },
    "Accounts": null,
    "modules_with_multiple_layouts": null
  }
}
```

### Status `200` — `application/json` — MultipleContactsWithDifferentStatesResponse

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

### Status `200` — `application/json` — MultipleContactsSimplifiedResponse

Multiple contacts with different approval states - simplified structure

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

### Status `400` — `application/json` — InvalidLeadId

Invalid lead ID provided

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "the given id seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — NotApprovedLead

Lead record is not approved

```json
{
  "code": "NOT_APPROVED",
  "details": {
    "resource_path_index": 1
  },
  "message": "record not approved",
  "status": "error"
}
```

### Status `400` — `application/json` — RecordLocked

Lead record is locked for merging

```json
{
  "code": "RECORD_LOCKED",
  "details": {
    "resource_path_index": 1
  },
  "message": "record under merge is locked",
  "status": "error"
}
```
