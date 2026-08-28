# DELETE /users/{user}
**Operation:** `deleteUser` — Delete a user from the organization
> To delete a specific user from your Zoho CRM organization, submit a DELETE request with the target user ID. Only one user can be removed per request, and certain protected user types — including support, system, Digital Employee, and primary contact users — cannot be deleted.

**Parameters:**
- `user` (path, string, required) [maxLen=19]: Specify the unique ID of the user to retrieve, update, or delete.

**Responses:**

- **200**: Returns a success response confirming that the specified user has been deleted from the Zoho CRM organization. [application/json]
    > Represents the success response returned after a user has been deleted from the Zoho CRM organization.
    - `users` (array of object) [maxItems=1] — Represents the list of deletion results for the requested user.
      - `code` (string) [enum=['SUCCESS']] — Indicates the result of the deletion request.
Possible values:
SUCCESS - The API successfully deleted the user.
      - `details` (object) — Represents the details of the deleted user record.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the deleted user.
      - `message` (string) [enum=['User deleted']] — Indicates the outcome of the deletion request.
Possible values:
User deleted - The user was removed from the organization successfully.
      - `status` (string) [enum=['success']] — Indicates the status of the API request.
Possible values:
success - The deletion request was processed successfully.

- **400**: Returns an error response when the user deletion request cannot be processed due to invalid data, a protected user type, insufficient privileges, a duplicate deletion, or an invalid request. [application/json]
    > Represents one of several 400 error responses returned when the user deletion request is invalid or cannot be completed.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Indicates the error code for this error condition.
Possible values:
INVALID_DATA - The provided user ID is invalid.
        - `details` (object) — Represents additional information about the INVALID_DATA error.
          - `resource_path_index` (integer/int32) — Represents the index of the resource path that caused the INVALID_DATA error.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Indicates the error message describing why the request failed.
Possible values:
the id given seems to be invalid - The supplied user ID does not correspond to a valid user.
        - `status` (string) **REQ** [enum=['error']] — Indicates the status of the API request.
Possible values:
error - The request failed.
        - `users` (array of object) [maxItems=1] **REQ** — Represents the list of error results for the deletion request.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Indicates the error code for this error condition.
Possible values:
NOT_ALLOWED - The requested operation is not permitted.
          - `details` (object) — Represents additional information about the NOT_ALLOWED error.
          - `message` (string) **REQ** [enum=['You cannot delete user in a sandbox org']] — Indicates the error message describing why the operation was not permitted.
Possible values:
You cannot delete user in a sandbox org - The user cannot be deleted because the organization is a sandbox.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the API request.
Possible values:
error - The request failed.
        - `users` (array of object) [maxItems=1] **REQ** — Represents the list of error results for the deletion request.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Indicates the error code for this error condition.
Possible values:
NOT_ALLOWED - The requested operation is not permitted.
          - `details` (object) — Represents additional information about the NOT_ALLOWED error.
            - `resource_path_index` (integer/int32) — Represents the index of the resource path that caused the NOT_ALLOWED error.
          - `message` (string) **REQ** [enum=['Support user cannot be deleted']] — Indicates the error message describing why the operation was not permitted.
Possible values:
Support user cannot be deleted - A support user account cannot be removed from the organization.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the API request.
Possible values:
error - The request failed.
        - `users` (array of object) [maxItems=1] **REQ** — Represents the list of error results for the deletion request.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Indicates the error code for this error condition.
Possible values:
NOT_ALLOWED - The requested operation is not permitted.
          - `details` (object) — Represents additional information about the NOT_ALLOWED error.
            - `resource_path_index` (integer/int32) — Represents the index of the resource path that caused the NOT_ALLOWED error.
          - `message` (string) **REQ** [enum=['System user cannot be deleted']] — Indicates the error message describing why the operation was not permitted.
Possible values:
System user cannot be deleted - A system user account cannot be removed from the organization.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the API request.
Possible values:
error - The request failed.
        - `users` (array of object) [maxItems=1] **REQ** — Represents the list of error results for the deletion request.
          - `code` (string) **REQ** [enum=['AUTHORIZATION_FAILED']] — Indicates the error code for this error condition.
Possible values:
AUTHORIZATION_FAILED - The user does not have sufficient privileges to perform this operation.
          - `details` (object) — Represents additional information about the AUTHORIZATION_FAILED error.
          - `message` (string) **REQ** [enum=['User does not have sufficient previlege to delete users']] — Indicates the error message when the user lacks the necessary privileges to delete users.
Possible values:
User does not have sufficient previlege to delete users - The requesting user does not have permission to delete users.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the API request.
Possible values:
error - The request failed.
        - `users` (array of object) [maxItems=1] **REQ** — Represents the list of error results for the deletion request.
          - `code` (string) **REQ** [enum=['ID_ALREADY_DELETED']] — Indicates the error code for this error condition.
Possible values:
ID_ALREADY_DELETED - The specified user has already been deleted.
          - `details` (object) — Represents additional information about the ID_ALREADY_DELETED error.
            - `json_path` (string) [enum=['$.users[0].id']] — Represents the JSON path of the field that caused the ID_ALREADY_DELETED error.
Possible values:
$.users[0].ID - Identifies the user ID field in the request.
            - `id` (string) [maxLen=19] — Represents the unique ID of the user that caused the ID_ALREADY_DELETED error.
          - `message` (string) **REQ** [enum=['User is already deleted']] — Indicates the error message when the user account has already been deleted.
Possible values:
User is already deleted - The specified user was previously removed from the organization.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the API request.
Possible values:
error - The request failed.
        - `users` (array of object) [maxItems=1] **REQ** — Represents the list of error results for the deletion request.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Indicates the error code for this error condition.
Possible values:
NOT_ALLOWED - The requested operation is not permitted.
          - `details` (object) — Represents additional information about the NOT_ALLOWED error.
            - `resource_path_index` (integer/int32) — Represents the index of the resource path that caused the NOT_ALLOWED error.
          - `message` (string) **REQ** [enum=['Digital Employee cannot be deleted/deactivated/activated']] — Indicates the error message when the user type cannot be deleted.
Possible values:
Digital Employee cannot be deleted/deactivated/activated - A Digital Employee user account cannot be deleted, deactivated, or activated.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the API request.
Possible values:
error - The request failed.
        - `users` (array of object) [maxItems=1] **REQ** — Represents the list of error results for the deletion request.
          - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Indicates the error code for this error condition.
Possible values:
INVALID_REQUEST - The request contains invalid data or violates a business rule.
          - `details` (object) — Represents additional information about the INVALID_REQUEST error.
            - `json_path` (string) [maxLen=100] — Represents the JSON path of the field that caused the INVALID_REQUEST error.
            - `id` (string) [maxLen=19] — Represents the unique ID of the user that caused the INVALID_REQUEST error.
          - `message` (string) **REQ** [enum=['Primary contact cannot be deleted']] — Indicates the error message when the primary contact cannot be deleted.
Possible values:
Primary contact cannot be deleted - The primary contact of the organization cannot be removed.
          - `status` (string) **REQ** [enum=['error']] — Indicates the status of the API request.
Possible values:
error - The request failed.

- **403**: Returns an error response when the caller does not have permission to delete users.
**Resolution:** The CRM administrator must grant the required user management permission to the caller profile in the Zoho CRM organization. [application/json]
    > Represents the error response returned when the caller does not have permission to delete the specified user or when the operation is forbidden for the target organization.
    - `code` (string) [enum=['NO_PERMISSION', 'PERMISSION_DENIED']] — Indicates the error code for this error condition.
Possible values:
NO_PERMISSION - The user lacks the required CRM profile permission.
PERMISSION_DENIED - The user does not have permission to perform this action.
    - `details` (object) — Represents additional information about the permission error.
      - `permissions` (array of string) [maxItems=1] — Represents the list of missing CRM profile permissions that caused the error.
        items: [enum=['Crm_Implied_Manage_Users']]
    - `message` (string) [enum=[3 values]] — Indicates the error message describing the permission error.
Possible values:
permission denied - The user does not have the required permission to delete users.
You can't perform this action over a closed/deleted user - The target user account is closed or already deleted.
User deletion is not allowed for the org because of CrmKeyValue entry RESTRICT_USER_DELETION_FOR_THE_ORG & deleted users count exceeded 10 - The organization has reached the maximum limit for user deletions.
    - `status` (string) [enum=['error']] — Indicates the status of the API request.
Possible values:
error - The request failed.

**Scopes:** ZohoCRM.users.DELETE
