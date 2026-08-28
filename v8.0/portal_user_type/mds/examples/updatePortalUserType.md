# Examples: updatePortalUserType

**PUT /settings/portals/{portal}/user_type/{userTypeId}**

## Request examples

### `application/json` — SamplePutRequest

Update portal user type

```json
{
  "user_type": [
    {
      "name": "Client Portal Updated",
      "active": true,
      "modules": [
        {
          "shared_type": "private",
          "permissions": {
            "view": true,
            "edit": true,
            "edit_shared_records": false,
            "create": true,
            "delete": true
          },
          "id": "111113000000002666",
          "filters": [
            {
              "id": "111113000000005092"
            }
          ],
          "layouts": [
            {
              "id": "111113000000003678",
              "_default_view": {
                "id": "111113000000003678",
                "type": "layout"
              }
            }
          ],
          "views": {
            "id": "111113000000070019",
            "type": "canvas_view"
          }
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success200

Portal user type updated successfully

```json
{
  "user_type": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111113000000168122"
      },
      "message": "Portal user type updated successfully.",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse1

API not supported for client portal user.

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

API not supported in sandbox.

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

API not supported.

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

No portal exists with the given portal name

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "No portal exists with the given portal name.",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Deletion of portal user type is not allowed, as user type contains users, which need to be transferred to other user type.

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

SAML configured for portal so phone field was not allowed for user types

```json
{
  "user_type": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.user_type[0].invitation_field.id"
      },
      "message": "SAML configured for portal so phone field was not allowed for user types",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse2

Change of personality module of default user type is not allowed

```json
{
  "user_type": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "personality_module",
        "json_path": "$.user_type[0].personality_module"
      },
      "message": "Change of personality module of default user type is not allowed.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse2

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

### Status `400` — `application/json` — InvalidDataResponse3

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

### Status `400` — `application/json` — InvalidDataResponse4

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

### Status `400` — `application/json` — InvalidDataResponse5

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "active",
        "maximum_length": 5,
        "json_path": "$.user_type[*].active"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse6

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "active",
        "minimum_length": 4,
        "json_path": "$.user_type[*].active"
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

### Status `400` — `application/json` — InvalidDataResponse8

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

### Status `400` — `application/json` — InvalidDataResponse9

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "modules",
        "maximum_length": 1,
        "json_path": "$.user_type[*].modules"
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
        "api_name": "shared_type",
        "expected_data_type": "text",
        "json_path": "$.user_type[*].modules[*].shared_type"
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
        "api_name": "shared_type",
        "maximum_length": 7,
        "json_path": "$.user_type[*].modules[*].shared_type"
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
        "api_name": "shared_type",
        "minimum_length": 6,
        "json_path": "$.user_type[*].modules[*].shared_type"
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
        "api_name": "shared_type",
        "supported_values": [
          "public",
          "private"
        ],
        "json_path": "$.user_type[*].modules[*].shared_type"
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
        "api_name": "permissions",
        "expected_data_type": "jsonobject",
        "json_path": "$.user_type[*].modules[*].permissions"
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
        "api_name": "permissions",
        "maximum_length": 1,
        "json_path": "$.user_type[*].modules[*].permissions"
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
        "api_name": "view",
        "expected_data_type": "boolean",
        "json_path": "$.user_type[*].modules[*].permissions.view"
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
        "api_name": "view",
        "maximum_length": 5,
        "json_path": "$.user_type[*].modules[*].permissions.view"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse18

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "view",
        "minimum_length": 2,
        "json_path": "$.user_type[*].modules[*].permissions.view"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse19

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
          "true",
          "false"
        ],
        "json_path": "$.user_type[*].modules[*].permissions.view"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse20

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

### Status `400` — `application/json` — InvalidDataResponse21

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

### Status `400` — `application/json` — InvalidDataResponse22

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

### Status `400` — `application/json` — InvalidDataResponse23

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

### Status `400` — `application/json` — InvalidDataResponse24

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "edit_shared_records",
        "supported_values": [
          "true",
          "false"
        ],
        "json_path": "$.user_type[*].modules[*].permissions.edit_shared_records"
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
        "api_name": "create",
        "expected_data_type": "boolean",
        "json_path": "$.user_type[*].modules[*].permissions.create"
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
        "api_name": "create",
        "maximum_length": 5,
        "json_path": "$.user_type[*].modules[*].permissions.create"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse27

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

### Status `400` — `application/json` — InvalidDataResponse28

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

### Status `400` — `application/json` — InvalidDataResponse29

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

### Status `400` — `application/json` — InvalidDataResponse30

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

### Status `400` — `application/json` — InvalidDataResponse31

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

### Status `400` — `application/json` — InvalidDataResponse32

Invalid data

```json
{
  "user_type": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "filters",
        "maximum_length": 1,
        "json_path": "$.user_type[*].modules[*].filters"
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
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.user_type[*].modules[*].filters[*].id"
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
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.user_type[*].modules[*].filters[*].id"
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
        "api_name": "layouts",
        "expected_data_type": "jsonarray",
        "json_path": "$.user_type[*].modules[*].layouts"
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
        "api_name": "layouts",
        "maximum_length": 1,
        "json_path": "$.user_type[*].modules[*].layouts"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse37

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
        "json_path": "$.user_type[*].modules[*].layouts[*].id"
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
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.user_type[*].modules[*].layouts[*].id"
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
        "api_name": "_default_view",
        "expected_data_type": "jsonobject",
        "json_path": "$.user_type[*].modules[*].layouts[*]._default_view"
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
        "api_name": "_default_view",
        "maximum_length": 1,
        "json_path": "$.user_type[*].modules[*].layouts[*]._default_view"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse41

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
        "json_path": "$.user_type[*].modules[*].layouts[*]._default_view.id"
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
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.user_type[*].modules[*].layouts[*]._default_view.id"
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
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.user_type[*].modules[*].layouts[*]._default_view.type"
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
        "api_name": "type",
        "maximum_length": 6,
        "json_path": "$.user_type[*].modules[*].layouts[*]._default_view.type"
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
        "api_name": "type",
        "supported_values": [
          "wizard",
          "layout"
        ],
        "json_path": "$.user_type[*].modules[*].layouts[*]._default_view.type"
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
        "api_name": "views",
        "expected_data_type": "jsonobject",
        "json_path": "$.user_type[*].modules[*].views"
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
        "api_name": "views",
        "maximum_length": 1,
        "json_path": "$.user_type[*].modules[*].views"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse48

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
        "json_path": "$.user_type[*].modules[*].views.id"
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
        "api_name": "id",
        "maximum_length": 18,
        "json_path": "$.user_type[*].modules[*].views.id"
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
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.user_type[*].modules[*].views.type"
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
        "api_name": "type",
        "maximum_length": 11,
        "json_path": "$.user_type[*].modules[*].views.type"
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
        "api_name": "type",
        "supported_values": [
          "canvas_view",
          "custom_view"
        ],
        "json_path": "$.user_type[*].modules[*].views.type"
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
