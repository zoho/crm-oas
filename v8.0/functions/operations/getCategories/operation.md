# GET /settings/functions/__schemas/categories
**Operation:** `getCategories` — Function Categories
> To retrieve all the [Function](functions.yaml#$.paths./settings/functions.get) categories supported by the current Zoho CRM account and indicate whether each category is available for use.

Different Zoho CRM editions and enabled features support different Function categories. Instead of assuming that a category is available, you can use this API to:

- Discover all the Function categories supported for the current CRM account.
- Check whether a Function category can be used before creating or updating a Function.

For example, if a customer's Zoho CRM edition does not support the **Signals** Function category, the response shows that the category is unavailable.


**Responses:**

- **200**: Returns the list of function categories configured in the Zoho CRM organization. — Schema: `GetcategoriesResponse200` [application/json]
    > Represents the successful response for retrieving the list of available categories in the Zoho CRM organization.
    schema: `GetcategoriesResponse200`
    - `categories` (array of object `GETCategoriesNested`) [maxItems=100] **REQ** — Represents the list of categories available in the Zoho CRM organization.
      schema: `GETCategoriesNested`
      - `allowed` (boolean) **REQ** — Indicates whether functions of this category can be created in the current account. Possible values: **true** - Functions of this category are allowed. **false** - Functions of this category are not allowed.
      - `category` (string) **REQ** [enum=[8 values]] — Represents the category of the function. Possible values: **Button** - A function triggered by a button action. **Automation** - A function triggered by an automation rule. **Schedule** - A function triggered on a scheduled basis. **Related List** - A function associated with a related list. **Standalone** - A function that runs independently. **Signals** - A function triggered by Signals notifications. **Validation Rule** - A function associated with a Validation Rule. **Dynamic** - A function that executes dynamically.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad request received by the server. **Resolution:** The request structure must be corrected before resubmitting. [application/json]
    > Represents the error response returned when the request contains invalid or malformed parameters.
    oneOf:
      - `ErrorResponseNoClientPortalSupport` — The error response returned when the requested API is not supported for client portal users.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — The error code identifying the cause of the failure. Possible values: **API_NOT_SUPPORTED** - The requested API is not supported for the current user type.
        - `details` (object) **REQ** — Additional error details associated with the failure, including information about the unsupported login user type.
          - `unsupported_login_user_type` (string) **REQ** [maxLen=255] — The type of login user that is not supported for this API.
        - `message` (string) **REQ** [enum=['api not supported for client portal user']] — The error message returned when the requested API is not supported for client portal users. Possible values: **api not supported for client portal user** - The API cannot be used by client portal users.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
      - `ErrorResponseFeatureNotSupported` — The error response returned when a requested feature is not supported for the current edition.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_SUPPORTED']] — The error code for this response. Possible values: **FEATURE_NOT_SUPPORTED** - Indicates that the requested feature is not supported for the current edition.
        - `details` (object) **REQ** — Additional details about the error.
        - `message` (string) **REQ** [enum=['Your License does not support this feature']] — The error message returned when the feature is not supported. Possible values: **Your License does not support this feature** - Indicates that the current license does not include the requested feature.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to retrieve function schema categories. **Resolution:** The CRM administrator must grant the required permission to the user's profile. [application/json]
    oneOf:
      - `NoDevPermissionError` — An error response returned when the requesting user lacks the required permission to perform the operation.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — The error code for the permission denial response. Possible values: **NO_PERMISSION** - The requesting user does not have permission to perform the operation.
        - `details` (object) **REQ** — Additional details about the permission denial error, including the permissions required to perform the operation.
          - `permissions` (array of string) [maxItems=25] **REQ** — The list of permissions required to perform the operation that was denied.
            items: [maxLen=255]
        - `message` (string) **REQ** [enum=['permission denied']] — The error message describing the permission denial. Possible values: **permission denied** - Indicates that the requesting user lacks the required permission to perform the operation.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
      - `UserEmailNotConfirmedError` — Represents the error response returned when the requesting user's email address has not been confirmed.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for this response. Possible values: **NO_PERMISSION** - Indicates the operation was not permitted.
        - `details` (object) **REQ** — Represents additional details about the error. This object is empty for this error type.
        - `message` (string) **REQ** [enum=['User email not confirmed']] — Represents the error message for this response. Possible values: **User email not confirmed** - Indicates the user's email address has not been confirmed.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates the request resulted in an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.functions.READ
