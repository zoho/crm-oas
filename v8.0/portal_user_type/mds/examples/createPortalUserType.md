# Examples: createPortalUserType

**POST /settings/portals/{portal}/user_type**

## Request examples

### `application/json` — SamplePostRequest

Sample request body for creating portal user type

```json
{
  "user_type": [
    {
      "personality_module": {
        "api_name": "Contacts",
        "id": "111113000000002666"
      },
      "name": "Client Portal V8",
      "active": true,
      "invitation_field": {
        "api_name": "Email",
        "id": "111113000000004612"
      },
      "deactive_user_count": 0,
      "modules": [
        {
          "plural_label": "Contacts",
          "shared_type": "private",
          "api_name": "Contacts",
          "permissions": {
            "view": true,
            "edit": true,
            "edit_shared_records": false,
            "create": true,
            "delete": true
          },
          "id": "111113000000002666",
          "filters": null,
          "fields": [
            {
              "read_only": false,
              "api_name": "Last_Name",
              "id": "111113000000004604"
            },
            {
              "read_only": false,
              "api_name": "Full_Name",
              "id": "111113000000004606"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000004660"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000004662"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000004668"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000004696"
            },
            {
              "read_only": false,
              "api_name": "Contact_X_CM01",
              "id": "111113000000131043"
            },
            {
              "read_only": false,
              "api_name": "Last_Enriched_Time__s",
              "id": "111113000000006734"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000003678",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000003678",
                "type": "layout"
              }
            }
          ],
          "views": {
            "id": "111113000000070019",
            "type": "canvas_view"
          }
        },
        {
          "plural_label": "Products",
          "shared_type": "public",
          "api_name": "Products",
          "permissions": {
            "view": true
          },
          "id": "111113000000002768",
          "fields": [
            {
              "read_only": false,
              "api_name": "Product_Name",
              "id": "111113000000005278"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000005308"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000005310"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000005312"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000005332"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000005326"
            }
          ],
          "views": {
            "id": "111113000000053489",
            "type": "custom_view"
          }
        },
        {
          "plural_label": "Custom Module",
          "shared_type": "private",
          "api_name": "Custom_Module",
          "permissions": {
            "view": true,
            "edit": false,
            "edit_shared_records": false,
            "create": false,
            "delete": false
          },
          "id": "111113000000125002",
          "filters": [
            {
              "display_label": "Lookup 1",
              "api_name": "Lookup_1",
              "id": "111113000000127669"
            }
          ],
          "fields": [
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000125065"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000125067"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000125071"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000125093"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000125111"
            },
            {
              "read_only": false,
              "api_name": "Name",
              "id": "111113000000125047"
            },
            {
              "read_only": false,
              "api_name": "Lookup_1",
              "id": "111113000000127669"
            },
            {
              "read_only": false,
              "api_name": "Multi_Select_Lookup_1",
              "id": "111113000000131001"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000125001",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000125001",
                "type": "layout"
              }
            }
          ],
          "views": {
            "id": "111113000000125014",
            "type": "custom_view"
          }
        },
        {
          "plural_label": "Notes",
          "shared_type": "private",
          "api_name": "Notes",
          "permissions": {
            "view": true,
            "delete_attachment": false,
            "edit": false,
            "create": false,
            "create_attachment": false,
            "delete": false
          },
          "id": "111113000000002694",
          "filters": null,
          "layouts": null,
          "views": null
        }
      ]
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — Success201

Portal user type created successfully (201)

```json
{
  "user_type": [
    {
      "default": false,
      "personality_module": {
        "plural_label": "Contacts",
        "api_name": "Contacts",
        "id": "111113000000002666"
      },
      "name": "Client Portal V8",
      "active": true,
      "invitation_field": {
        "api_name": "Email",
        "id": "111113000000004612"
      },
      "id": "111113000000168122",
      "modules": [
        {
          "plural_label": "Contacts",
          "shared_type": "private",
          "api_name": "Contacts",
          "permissions": {
            "view": true,
            "edit": true,
            "edit_shared_records": false,
            "create": true,
            "delete": true
          },
          "id": "111113000000002666",
          "filters": null,
          "fields": [
            {
              "read_only": false,
              "api_name": "Last_Name",
              "id": "111113000000004604"
            },
            {
              "read_only": false,
              "api_name": "Full_Name",
              "id": "111113000000004606"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000004660"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000004662"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000004668"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000004694"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000004696"
            },
            {
              "read_only": false,
              "api_name": "Contact_X_CM01",
              "id": "111113000000131043"
            },
            {
              "read_only": false,
              "api_name": "Last_Enriched_Time__s",
              "id": "111113000000006734"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000003678",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000003678",
                "type": "layout"
              }
            }
          ],
          "views": {
            "id": "111113000000070019",
            "type": "canvas_view"
          }
        },
        {
          "plural_label": "Products",
          "shared_type": "public",
          "api_name": "Products",
          "permissions": {
            "view": true
          },
          "id": "111113000000002768",
          "filters": null,
          "fields": [
            {
              "read_only": false,
              "api_name": "Product_Name",
              "id": "111113000000005278"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000005308"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000005310"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000005312"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000005332"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000005326"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000003684",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000003684",
                "type": "layout"
              }
            }
          ],
          "views": {
            "id": "111113000000053489",
            "type": "custom_view"
          }
        },
        {
          "plural_label": "Custom Module",
          "shared_type": "private",
          "api_name": "Custom_Module",
          "permissions": {
            "view": true,
            "edit": false,
            "edit_shared_records": false,
            "create": false,
            "delete": false
          },
          "id": "111113000000125002",
          "filters": [
            {
              "display_label": "Lookup 1",
              "api_name": "Lookup_1",
              "id": "111113000000127669"
            }
          ],
          "fields": [
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000125065"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000125067"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000125071"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000125093"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000125111"
            },
            {
              "read_only": false,
              "api_name": "Name",
              "id": "111113000000125047"
            },
            {
              "read_only": false,
              "api_name": "Lookup_1",
              "id": "111113000000127669"
            },
            {
              "read_only": false,
              "api_name": "Multi_Select_Lookup_1",
              "id": "111113000000131001"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000125001",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000125001",
                "type": "layout"
              }
            }
          ],
          "views": {
            "id": "111113000000125014",
            "type": "custom_view"
          }
        },
        {
          "plural_label": "Notes",
          "shared_type": "private",
          "api_name": "Notes",
          "permissions": {
            "view": true,
            "delete_attachment": false,
            "edit": false,
            "create": false,
            "create_attachment": false,
            "delete": false
          },
          "id": "111113000000002694",
          "filters": null,
          "fields": [
            {
              "read_only": false,
              "api_name": "Owner",
              "id": "111113000000004322"
            },
            {
              "read_only": false,
              "api_name": "Note_Title",
              "id": "111113000000004324"
            },
            {
              "read_only": false,
              "api_name": "Note_Content",
              "id": "111113000000004326"
            },
            {
              "read_only": false,
              "api_name": "Parent_Id",
              "id": "111113000000004328"
            },
            {
              "read_only": false,
              "api_name": "Created_By",
              "id": "111113000000004330"
            },
            {
              "read_only": false,
              "api_name": "Modified_By",
              "id": "111113000000004332"
            },
            {
              "read_only": false,
              "api_name": "Created_Time",
              "id": "111113000000004334"
            },
            {
              "read_only": false,
              "api_name": "Modified_Time",
              "id": "111113000000004336"
            },
            {
              "read_only": false,
              "api_name": "id",
              "id": "111113000000004338"
            },
            {
              "read_only": false,
              "api_name": "Associated_Id__s",
              "id": "111113000000004340"
            },
            {
              "read_only": false,
              "api_name": "Record_Status__s",
              "id": "111113000000004342"
            }
          ],
          "layouts": null,
          "views": null
        }
      ]
    }
  ]
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse1

API not supported for client portal user

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "unsupported_login_user_type": "Client Portal User"
  },
  "message": "api not supported for client portal user",
  "status": "error"
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse2

API not supported in sandbox

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "unsupported_environment": "sandbox"
  },
  "message": "api not supported in sandbox",
  "status": "error"
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse3

API not supported

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "supported_domains": [
      "eu",
      "com",
      "in",
      "au",
      "ca",
      "cn",
      "jp"
    ]
  },
  "message": "api not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidPortalNameResponse1

No portal exists with the given portal name. (INVALID_DATA)

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "No portal exists with the given portal name.",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Invalid data error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "jsonobject"
  },
  "message": "body",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse1

Layout does not have selected filter in it.

```json
{
  "user_type": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "json_path": "$.user_type[0].modules[0].layouts[0].id"
      },
      "message": "Layout does not have selected filter in it.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

Layouts are missing

```json
{
  "user_type": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "id",
          "json_path": "$.user_type[0].modules[6].id"
        },
        "api_name": "layouts",
        "json_path": "$.user_type[0].modules[6].layouts"
      },
      "message": "layouts are missing.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Required field not found

```json
{
  "user_type": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "permissions",
        "json_path": "$.user_type[0].modules[0].permissions"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LicenseLimitExceededResponse1

License limit exceeded

```json
{
  "user_type": [
    {
      "code": "LICENSE_LIMIT_EXCEEDED",
      "details": {},
      "message": "License limit exceeded.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Required field not found

```json
{
  "user_type": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "shared_type",
        "json_path": "$.user_type[0].modules[0].shared_type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse3

Required field not found

```json
{
  "user_type": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "type",
        "json_path": "$.user_type[0].modules[0].views.type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse4

Required field not found

```json
{
  "user_type": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.user_type[0].modules[0].views.id"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Field is not allowed in portals

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "details": {
        "json_path": "$.user_type[0].modules[2].fields[0].id"
      },
      "message": "Field is not allowed in portals.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

One of the expected parameter is missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "api_name": "read_only"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse5

Personality module and Notes module are mandatory modules

```json
{
  "user_type": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {},
      "message": "Personality module and Notes module are mandatory modules.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "details": {
        "regex": "[^`~!&+%()@#^*'/\";:?<>=\\[\\]{}|-]+",
        "api_name": "name",
        "json_path": "$.user_type[0].name"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse6

Required field is missing

```json
{
  "user_type": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "personality_module",
        "json_path": "$.user_type[*].personality_module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse4

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "personality_module",
        "expected_data_type": "jsonobject",
        "json_path": "$.user_type[*].personality_module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse5

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "personality_module",
        "maximum_length": 1,
        "json_path": "$.user_type[*].personality_module"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.user_type[*].personality_module.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse7

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 50,
        "json_path": "$.user_type[*].personality_module.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse8

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.user_type[*].personality_module.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse9

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.user_type[*].personality_module.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse7

Required field is missing

```json
{
  "user_type": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.user_type[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse10

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.user_type[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse11

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 50,
        "json_path": "$.user_type[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse12

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "minimum_length": 1,
        "json_path": "$.user_type[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse13

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "regex": "^[A-Za-z0-9]{50}$",
        "json_path": "$.user_type[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse14

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "active",
        "expected_data_type": "boolean",
        "json_path": "$.user_type[*].active"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse15

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "active",
        "supported_values": [
          "true",
          "false"
        ],
        "json_path": "$.user_type[*].active"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse8

Required field is missing

```json
{
  "user_type": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "invitation_field",
        "json_path": "$.user_type[*].invitation_field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse16

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "invitation_field",
        "expected_data_type": "jsonobject",
        "json_path": "$.user_type[*].invitation_field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse17

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "invitation_field",
        "maximum_length": 1,
        "json_path": "$.user_type[*].invitation_field"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse18

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.user_type[*].invitation_field.api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse19

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.user_type[*].invitation_field.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse20

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.user_type[*].invitation_field.id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse21

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.user_type[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse22

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.user_type[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse23

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "deactive_user_count",
        "expected_data_type": "integer",
        "json_path": "$.user_type[*].deactive_user_count"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse9

Required field is missing

```json
{
  "user_type": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "modules",
        "json_path": "$.user_type[*].modules"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse24

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "modules",
        "expected_data_type": "jsonarray",
        "json_path": "$.user_type[*].modules"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse25

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "plural_label",
        "expected_data_type": "text",
        "json_path": "$.user_type[*].modules[*].plural_label"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse26

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "plural_label",
        "maximum_length": 5,
        "json_path": "$.user_type[*].modules[*].plural_label"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse10

Required field is missing

```json
{
  "user_type": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "shared_type",
        "json_path": "$.user_type[*].modules[*].shared_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse27

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "shared_type",
        "expected_data_type": "text",
        "json_path": "$.user_type[*].modules[*].shared_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse28

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "shared_type",
        "maximum_length": 7,
        "json_path": "$.user_type[*].modules[*].shared_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse29

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "shared_type",
        "minimum_length": 5,
        "json_path": "$.user_type[*].modules[*].shared_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse30

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "shared_type",
        "supported_values": [
          "private",
          "public"
        ],
        "json_path": "$.user_type[*].modules[*].shared_type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse31

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.user_type[*].modules[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse32

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 5,
        "json_path": "$.user_type[*].modules[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse11

Required field is missing

```json
{
  "user_type": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "permissions",
        "json_path": "$.user_type[*].modules[*].permissions"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse33

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "permissions",
        "expected_data_type": "jsonobject",
        "json_path": "$.user_type[*].modules[*].permissions"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse34

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "permissions",
        "maximum_length": 1,
        "json_path": "$.user_type[*].modules[*].permissions"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse12

Required field is missing

```json
{
  "user_type": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "view",
        "json_path": "$.user_type[*].modules[*].permissions.view"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse35

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "view",
        "expected_data_type": "boolean",
        "json_path": "$.user_type[*].modules[*].permissions.view"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse36

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "view",
        "maximum_length": 4,
        "json_path": "$.user_type[*].modules[*].permissions.view"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse37

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "view",
        "minimum_length": 4,
        "json_path": "$.user_type[*].modules[*].permissions.view"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse38

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "view",
        "supported_values": [
          "true"
        ],
        "json_path": "$.user_type[*].modules[*].permissions.view"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse39

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "edit",
        "expected_data_type": "boolean",
        "json_path": "$.user_type[*].modules[*].permissions.edit"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse40

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "edit",
        "maximum_length": 5,
        "json_path": "$.user_type[*].modules[*].permissions.edit"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse41

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "edit",
        "minimum_length": 4,
        "json_path": "$.user_type[*].modules[*].permissions.edit"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse42

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "edit",
        "supported_values": [
          "true",
          "false"
        ],
        "json_path": "$.user_type[*].modules[*].permissions.edit"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse43

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "edit_shared_records",
        "expected_data_type": "boolean",
        "json_path": "$.user_type[*].modules[*].permissions.edit_shared_records"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse44

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "edit_shared_records",
        "maximum_length": 5,
        "json_path": "$.user_type[*].modules[*].permissions.edit_shared_records"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse45

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "edit_shared_records",
        "minimum_length": 4,
        "json_path": "$.user_type[*].modules[*].permissions.edit_shared_records"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse46

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "create",
        "expected_data_type": "boolean",
        "json_path": "$.user_type[*].modules[*].permissions.create"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse47

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "create",
        "maximum_length": 5,
        "json_path": "$.user_type[*].modules[*].permissions.create"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse48

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "create",
        "minimum_length": 4,
        "json_path": "$.user_type[*].modules[*].permissions.create"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse49

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "create",
        "supported_values": [
          "true",
          "false"
        ],
        "json_path": "$.user_type[*].modules[*].permissions.create"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse50

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "delete",
        "expected_data_type": "boolean",
        "json_path": "$.user_type[*].modules[*].permissions.delete"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse51

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "delete",
        "maximum_length": 5,
        "json_path": "$.user_type[*].modules[*].permissions.delete"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse52

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "delete",
        "minimum_length": 4,
        "json_path": "$.user_type[*].modules[*].permissions.delete"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse53

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "delete",
        "supported_values": [
          "true",
          "false"
        ],
        "json_path": "$.user_type[*].modules[*].permissions.delete"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse54

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "delete_attachment",
        "expected_data_type": "boolean",
        "json_path": "$.user_type[*].modules[*].permissions.delete_attachment"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse55

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "delete_attachment",
        "maximum_length": 5,
        "json_path": "$.user_type[*].modules[*].permissions.delete_attachment"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse56

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "delete_attachment",
        "minimum_length": 4,
        "json_path": "$.user_type[*].modules[*].permissions.delete_attachment"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse57

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "delete_attachment",
        "supported_values": [
          "true",
          "false"
        ],
        "json_path": "$.user_type[*].modules[*].permissions.delete_attachment"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse58

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "create_attachment",
        "expected_data_type": "boolean",
        "json_path": "$.user_type[*].modules[*].permissions.create_attachment"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse59

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "create_attachment",
        "maximum_length": 5,
        "json_path": "$.user_type[*].modules[*].permissions.create_attachment"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse60

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "create_attachment",
        "minimum_length": 4,
        "json_path": "$.user_type[*].modules[*].permissions.create_attachment"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse61

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "create_attachment",
        "supported_values": [
          "true",
          "false"
        ],
        "json_path": "$.user_type[*].modules[*].permissions.create_attachment"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse13

Required field is missing

```json
{
  "user_type": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.user_type[*].modules[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse62

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.user_type[*].modules[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse63

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.user_type[*].modules[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse64

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "filters",
        "expected_data_type": "jsonarray",
        "json_path": "$.user_type[*].modules[*].filters"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse65

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "fields",
        "expected_data_type": "jsonarray",
        "json_path": "$.user_type[*].modules[*].fields"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse66

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "fields",
        "maximum_length": 503,
        "json_path": "$.user_type[*].modules[*].fields"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse67

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "read_only",
        "expected_data_type": "boolean",
        "json_path": "$.user_type[*].modules[*].fields[*].read_only"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse68

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "read_only",
        "maximum_length": 5,
        "json_path": "$.user_type[*].modules[*].fields[*].read_only"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse69

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "read_only",
        "minimum_length": 4,
        "json_path": "$.user_type[*].modules[*].fields[*].read_only"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse70

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "read_only",
        "supported_values": [
          "true",
          "false"
        ],
        "json_path": "$.user_type[*].modules[*].fields[*].read_only"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse71

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.user_type[*].modules[*].fields[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse72

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 50,
        "json_path": "$.user_type[*].modules[*].fields[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse73

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "minimum_length": 1,
        "json_path": "$.user_type[*].modules[*].fields[*].api_name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse74

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.user_type[*].modules[*].fields[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse75

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.user_type[*].modules[*].fields[*].id"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse76

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "layouts",
        "expected_data_type": "jsonarray",
        "json_path": "$.user_type[*].modules[*].layouts"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse77

Invalid data type

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "views",
        "expected_data_type": "jsonobject",
        "json_path": "$.user_type[*].modules[*].views"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse78

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "views",
        "maximum_length": 1,
        "json_path": "$.user_type[*].modules[*].views"
      },
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse1

No permission

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_ClientPortal"
    ]
  },
  "message": "No permission",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse2

NO_PERMISSION

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "NO_PERMISSION",
  "status": "error"
}
```
