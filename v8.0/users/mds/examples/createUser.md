# Examples: createUser

**POST /users**

## Request examples

### `application/json` — UserAdded

Create User Request

```json
{
  "users": [
    {
      "first_name": "rfdc2",
      "email": "user@example.com",
      "role": {
        "name": "CEO",
        "id": "2922942000000015966"
      },
      "profile": {
        "name": "Administrator",
        "id": "2922942000000015972"
      },
      "$invitation_details": {
        "COMPANYLOGOURL": "https://static.zohocdn.com/crm/CRMClient/images/crm_logonew_18ad4a6d3fca927f423b0a15f6dbc241_.svg",
        "COMPANYNAME": "ZohoCRM",
        "DISPLAYNAME": "User 1"
      }
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — UserCreatedSuccessfully

Successful user creation response

```json
{
  "users": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111113000000071587"
      },
      "message": "User added",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MoreThanOneUserCreationAttempt

More than one user object in the request

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 1,
    "api_name": "users",
    "json_path": "$.users"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataErrorResponse

Invalid data in one or more request fields

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "time_zone",
        "json_path": "$.users[0].time_zone"
      },
      "message": "Give a proper time zone value",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataInResponse2

Invalid reporting to user ID or role ID

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "Valid userid should be given"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ReportingToUserIdDeleted

Reporting To user ID refers to a deleted user

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "Reporting_To",
        "json_path": "$.users[0].Reporting_To.id"
      },
      "message": "the id given seems to be already deleted",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidReportingToUser

Invalid Reporting To user ID in request

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "Invalid Reporting Manager"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidProfieIdOrRoleIdOrLocale

Invalid profile ID, role ID, or locale value

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "profile",
        "json_path": "$.users[0].profile"
      },
      "message": "INVALID_DATA",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SpecialCharacterInField

Impermissible special character in a field value

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "first_name",
        "json_path": "$.users[0].first_name"
      },
      "message": "Special Characters Found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — PatternMismatchInField

Shows the error returned when the value provided for a field does not match the expected format or pattern, such as for the time format, distance preference, or status fields.

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "time_format",
        "json_path": "$.users[0].time_format"
      },
      "message": "Pattern not matched",
      "status": "error"
    }
  ],
  "summary": "Field value does not match the expected pattern"
}
```

### Status `400` — `application/json` — NumberAndDecimalSeparatorMismatch

```json
{
  "users": [
    {
      "code": "MAPPING_MISMATCH",
      "details": {
        "mapped_field": {
          "api_name": "number_separator",
          "json_path": "$.users[0].number_separator"
        },
        "api_name": "decimal_separator",
        "json_path": "$.users[0].decimal_separator"
      },
      "message": "the number separator and decimal separator values should not be same",
      "status": "error"
    }
  ],
  "description": "Shows the error returned when the number separator and decimal separator values submitted in the request are identical.",
  "summary": "Number separator and decimal separator values are identical"
}
```

### Status `400` — `application/json` — InvalidNumberSeparator

Invalid number separator value in request

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "number_separator",
        "json_path": "$.users[0].number_separator"
      },
      "message": "Invalid data. Valid values are Comma/Period/Space (Not case-sensitive)",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDecimalSeparator

Invalid decimal separator value in request

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "decimal_separator",
        "json_path": "$.users[0].decimal_separator"
      },
      "message": "Invalid data. Valid values are Comma/Period (Not case-sensitive)",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AddingUserInZohoOne

Attempt to add user in a Zoho One account

```json
{
  "users": [
    {
      "code": "UNAPPROVABLE",
      "details": {},
      "message": "Cannot add user for ZohoOne account from CRM. Kindly add user through ZohoOne",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AddingUserInCrmPlus

Attempt to add user in a CRM Plus account

```json
{
  "users": [
    {
      "code": "UNAPPROVABLE",
      "details": {},
      "message": "Cannot add user for CRMPlus account from CRM. Kindly add user through CRMPlus",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AddingCreatedByOrModifiedByField

Attempt to set read-only Created By or Modified By field

```json
{
  "users": [
    {
      "code": "NOT_SUPPORTED",
      "details": {
        "api_name": "created_by",
        "json_path": "$.users[0].created_by"
      },
      "message": "Created by & Modified by fields cannot be updated by api",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingReportingToFieldWithoutEnablingReportingToFeature

Reporting To field set without enabling the Reporting To feature

```json
{
  "users": [
    {
      "code": "FEATURE_NOT_ENABLED",
      "details": {},
      "message": "ReportingTo Feature is not enabled",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — CreatingDigitalEmployee

Attempt to create a Digital Employee user via API

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "type__s",
        "json_path": "$.users[0].type__s"
      },
      "message": "The specified user type is not allowed",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UserCreationInSandBoxOrg

Attempt to create user in a sandbox organization

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {},
      "message": "You cannot create user in a sandbox org",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Updatingtypefields

Attempt to set a read-only or API-restricted field

```json
{
  "users": [
    {
      "code": "NOT_SUPPORTED",
      "details": {
        "api_name": "type__s",
        "json_path": "$.users[0].type__s"
      },
      "message": "type__s is cannot be updated by api",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UserCreationWithoutUpdatingCompanyDetails

User creation attempted without required company details

```json
{
  "users": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {},
      "message": "Company Name is required",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — CreatingSupportUser

Attempt to create a Support User via API

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "profile"
      },
      "message": "Support user cannot be added",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — CreatingSystemUser

Attempt to create a System User via API

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "profile"
      },
      "message": "System user cannot be added",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UserLimitExceeded

Licensed user limit reached under current plan

```json
{
  "users": [
    {
      "code": "LICENSE_LIMIT_EXCEEDED",
      "details": {},
      "message": "Request exceeds your license limit. Need to upgrade in order to add a user",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — TeamUserLimitExceeded

Team user limit reached under current license

```json
{
  "users": [
    {
      "code": "LICENSE_LIMIT_EXCEEDED",
      "details": {},
      "message": "Request exceeds your license limit. Need to upgrade in order to add a team user",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateEmailInUserCreation

Duplicate email address in user creation request

```json
{
  "users": [
    {
      "code": "DUPLICATE_DATA",
      "details": {},
      "message": "Failed to add user since same email id is already present",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UserInvitationLimitExceeded

Maximum pending user invitations reached

```json
{
  "users": [
    {
      "code": "INVALID_REQUEST",
      "details": {},
      "message": "User cannot be added as the user has already reached the maximum invitation limit",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ShiftEffectiveFromDateMissing

Next shift specified without an effective-from date

```json
{
  "users": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "$next_shift",
          "json_path": "$.users[0].$next_shift"
        },
        "api_name": "$shift_effective_from",
        "json_path": "$.users[0].$shift_effective_from"
      },
      "message": "Dependent Field value should not be null",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidShiftEffectiveFromDate

Invalid shift effective-from date in request

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "$shift_effective_from",
        "json_path": "$.users[0].$shift_effective_from"
      },
      "message": "Shift effective from date should be greater than Current Shift date",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NextShiftWithDateWithMoretimePeriod

Shift effective-from date too far in the future

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "Maximum time period is six months to move shift",
        "api_name": "$shift_effective_from",
        "json_path": "$.users[0].$shift_effective_from"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidCurrenntShiftId

Invalid current shift ID in request

```json
{
  "users": [
    {
      "code": "INVALID_REQUEST",
      "details": {
        "api_name": "$current_shift",
        "json_path": "$.users[0].$current_shift.id"
      },
      "message": "Invalid current shift id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidNextShiftId

Invalid next shift ID in request

```json
{
  "users": [
    {
      "code": "INVALID_REQUEST",
      "details": {
        "api_name": "$next_shift",
        "json_path": "$.users[0].$next_shift.id"
      },
      "message": "Invalid next shift id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SameCurrentAndNextShiftId

Current shift and next shift IDs are identical

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "$next_shift.id",
        "json_path": "$.users[0].$next_shift.id"
      },
      "message": "current shift and next shift should not be same",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — EmailAlradyRegisteredInAnotherDC

Email address registered in another data center

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {},
      "message": "This email address is already registered with another datacenter and cannot be registered with this account's data centre US",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidEmailId

Invalid email address format in request

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "email"
      },
      "message": "Invalid Email Id. Please choose a different email id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ZohoEmailId

Attempt to create user with a Zoho-domain email address

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "email"
      },
      "message": "Email Id should not contain @zoho.com. Please choose a different email id",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionToCreateUser

Insufficient permission to create a user

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Users"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
