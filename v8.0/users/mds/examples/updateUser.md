# Examples: updateUser

**PUT /users**

## Request examples

### `application/json` — UserAdded

Update user request

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
      }
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — UserUpdatedSuccessfully

User updated successfully

```json
{
  "users": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111113000000071587"
      },
      "message": "User updated",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingMoreThanTenUsers

Updating more than 10 users at once

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 10,
    "api_name": "users",
    "json_path": "$.users"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — UpdatingWithoutUserId

User ID missing in update request

```json
{
  "users": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InValidUserIdResponse

Invalid user ID in update request

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 1
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — DeletedUserUpdate

Updating a deleted user

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 1
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — ActivatingSupportUser

Activating a support user

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "Support user cannot be activated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ActivatingSystemUser

Activating a system user

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "System user cannot be activated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingCreatedByOrModifiedByField

Updating read-only Created By or Modified By field

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

### Status `400` — `application/json` — DeactivatingSupportUser

Deactivating a support user

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "Support user cannot be deactivated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DeactivatingSystemUser

Deactivating a system user

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "System user cannot be deactivated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingDigitalUserStatus

Updating digital employee user status

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "type__s",
        "json_path": "$.users[0].type__s"
      },
      "message": "Digital Employee cannot be Deleted / Deactivated / Activated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingSupportUserDetails

Updating support user details

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "Cannot update the user details of support user",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AssigningSystemProfileToUser

Assigning system profile to a user

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "profile",
        "json_path": "$.users[0].profile"
      },
      "message": "System Profile cannot be assigned to other users",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingDeletedUser

Updating a deleted user

```json
{
  "users": [
    {
      "code": "CANNOT_UPDATE_DELETED_USER",
      "details": {},
      "message": "Deleted user cannot be updated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — CrmPlusUserEmailUpdate

Email update for a CRM Plus user

```json
{
  "users": [
    {
      "code": "EMAIL_UPDATE_NOT_ALOWED",
      "details": {
        "api_name": "email"
      },
      "message": "Crm Plus account is not allowed to edit the email while updating the user info",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ReinvitingConfirmedUser

Re-inviting an already confirmed user

```json
{
  "users": [
    {
      "code": "INVALID_REQUEST",
      "details": {
        "api_name": "reinvite"
      },
      "message": "Reinvite is not allowed for a confirmed user",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingEmailForAConfirmedUser

Updating email for a confirmed user

```json
{
  "users": [
    {
      "code": "EMAIL_UPDATE_NOT_ALOWED",
      "details": {
        "api_name": "email"
      },
      "message": "Cannot update email of a confirmed CRM User",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UserAlreadyExistsInCRMplus

User already exists in CRM Plus

```json
{
  "users": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "email",
        "id": "0987654321"
      },
      "message": "User with same email id is already in CRM Plus",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DeactivatingAlreadyDeactivatedUser

Deactivating an already deactivated user

```json
{
  "users": [
    {
      "code": "ID_ALREADY_DEACTIVATED",
      "details": {
        "api_name": "id",
        "id": "$.users[0].id"
      },
      "message": "User is already deactivated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DigitalUserStatusUpdate

Digital employee user status change

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "0987654321"
      },
      "message": "You are not allowed to perform this operation.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LoggedInUserStatusUpdate

Deactivating the currently logged-in user

```json
{
  "users": [
    {
      "code": "FEATURE_NOT_AVAILABLE",
      "details": {},
      "message": "Share among Subordinates Feature is not available",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UserUpdatingWithNotEligibleReportingTo

Reporting To user not eligible

```json
{
  "users": [
    {
      "code": "CONFLICTING_DATA_FOUND",
      "details": {
        "api_name": "Reporting_To",
        "json_path": "$.users[0].Reporting_To"
      },
      "message": "the user must be updated with new eligible reporting manager because of changing user role",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UserUpdatingWithNotEligibleSubordinates

Role change creates invalid subordinate relationships

```json
{
  "users": [
    {
      "code": "CONFLICTING_DATA_FOUND",
      "details": {
        "api_name": "Reporting_To",
        "json_path": "$.users[0].Reporting_To"
      },
      "message": "the user must be updated with new eligible reporting manager and the subordinates  who are going to report to a user in a role below them, because of new role change are need to transfer to new eligible reporting manager",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingSameUserIdAsReportingTo

Setting self as Reporting To manager

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "ReportingTo Id should not be the same as userId"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingUserWithReportingToWithNotSupportedRoles

Reporting To not supported for the user role

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Reporting_To"
      },
      "message": "Reporting manager should be from parent roles or from the same role to which the current user belongs",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ShareAmongFeatureNotEnabled

Share among subordinates feature not enabled

```json
{
  "users": [
    {
      "code": "INVALID_REQUEST",
      "details": {},
      "message": "You can't perform this action over logged in user",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DeactivatingPrimaryUser

Deactivating the primary user

```json
{
  "users": [
    {
      "code": "INVALID_REQUEST",
      "details": {
        "id": "0987654321",
        "json_path": "$.users[0].id"
      },
      "message": "Primary Contact cannot be deactivated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AlreadyActiveUserActivation

Activating an already active user

```json
{
  "users": [
    {
      "code": "ID_ALREADY_ACTIVE",
      "details": {
        "id": "0987654321",
        "json_path": "$.users[0].id"
      },
      "message": "User is already active",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InsufficientPrevilidgesToUpdateUser

Insufficient authorization to update a user

```json
{
  "users": [
    {
      "code": "AUTHORIZATION_FAILED",
      "details": {},
      "message": "Either trial is expired or user does not have sufficient previlege to perform this action",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LicenseLimitExceededWhileActivatingUser

License limit exceeded while activating a user

```json
{
  "users": [
    {
      "code": "LICENSE_LIMIT_EXCEEDED",
      "details": {},
      "message": "License Limit is Exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MoreThanOneUserUpdationAttempt

Updating more than the maximum allowed users

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

Invalid data in update request

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

Invalid reporting manager or role ID

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

### Status `400` — `application/json` — InvalidProfieIdOrRoleIdOrLocale

Invalid profile ID, role ID, or locale

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

### Status `400` — `application/json` — NumberAndDecimalSeparatorMismatch

Number and decimal separator cannot be the same

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
  ]
}
```

### Status `400` — `application/json` — InvalidNumberSeparator

Invalid number separator

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

Invalid decimal separator

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

### Status `400` — `application/json` — InvalidNameFormat

Invalid name format

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name_format__s",
        "json_path": "$.users[0].name_format__s"
      },
      "message": "Valid name format should be given",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidSortPreference

Invalid sort order preference

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "sort_order_preference__s",
        "json_path": "$.users[0].sort_order_preference__s"
      },
      "message": "Valid sort order preference should be given",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotUpdatingFortheSameUser

Not allowed to update restricted fields for another user

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "name_format__s"
      },
      "message": "Cannot update the name_format__s of another User",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidLanguageCode

Invalid language code

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "language",
        "json_path": "$.users[0].language"
      },
      "message": "Give a proper language code",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SpecialCharacterInField

Special character in a field value

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

Pattern mismatch in field value

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
  ]
}
```

### Status `400` — `application/json` — UpdatingReportingToFieldWithoutEnablingReportingToFeature

Setting Reporting To without enabling the feature

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

### Status `400` — `application/json` — Updatingtypesfields

Updating read-only type field

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

### Status `400` — `application/json` — CreatingSupportOrSystemUser

Changing a user to support or system type

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

### Status `400` — `application/json` — UserLimitExceeded

User limit exceeded

```json
{
  "users": [
    {
      "code": "LICENSE_LIMIT_EXCEEDED",
      "details": {},
      "message": "You are trying to activate more mail addon which exceeds your license limit. If you want to activate mail addon for additional users, please upgrade your license",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateEmailId

Duplicate email address in user update

```json
{
  "users": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "email",
        "json_path": "$.users[0].email"
      },
      "message": "Email already exists",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InSufficientPrivilegesToUpdateUser

Insufficient privileges to update a user

```json
{
  "users": [
    {
      "code": "AUTHORIZATION_FAILED",
      "details": {},
      "message": "Either trial is expired or user does not have sufficiet previlege to perform this action",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingNonSubordinateUser

Updating a non-subordinate user

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "Non subordinate users cannot be updated",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — UpdatingClosedOrDeletedUser

Updating a user in a closed or deleted organization

```json
{
  "users": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].id"
      },
      "message": "You can't perform this action over a closed/deleted user",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidReportingManager

Invalid reporting manager

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.users[0].Reporting_To.id"
      },
      "message": "the reporting manager must be superior in reporting hierarchy",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidCurrenntShiftId

Invalid current shift ID

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

Invalid next shift ID

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

Current and next shift IDs cannot be the same

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

### Status `400` — `application/json` — ShiftEffectiveFromDateMissing

Missing shift effective-from date

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

Invalid shift effective-from date

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

Shift effective-from date exceeds maximum period

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

### Status `403` — `application/json` — NoPermissionToCreateUser

No permission to update a user

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
