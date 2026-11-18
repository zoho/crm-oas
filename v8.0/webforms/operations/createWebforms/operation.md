# POST /settings/webforms
**Operation:** `createWebforms` — Create a new webform in Zoho CRM
> 
To create a new webform in Zoho CRM with full configuration, 
including module assignment, layout, form fields, button attributes, 
analytics settings, double opt-in, spam control, visitor tracking, and 
portal form support. A single webform may be submitted per request. 
 
 **Notes:** 
  To assign the owner of the records submitted via Webforms you should either choose to mention specific user details in the **owner** key or mention an assignment rule to assign ownership.


**Parameters:**
- `module` (query, string, required) [enum=['Leads']]: Specify the module API name of the CRM module for which the webform is being created or updated. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.

**Schemas:**
`ErrorResponse`:
  > Represents a generic API error response containing an error code, status, message, and details.
  - `code` (string) **REQ** [enum=[18 values]] — Represents the error code that identifies the type of error returned by the API.
  - `details` (object) **REQ** — Represents additional details providing context about the error, such as the invalid field name or parameter.
  - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the reason for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: error - The request was not successful.
`FromAddressNested`:
  > Represents the sender's email address configuration used in acknowledgment emails sent after webform submission.
  - `api_name` (string) [maxLen=255] — Represents the API name of the sender's email address used in the acknowledgment email for the webform.
  - `name` (string) [maxLen=255] — Represents the display name of the sender configured for the acknowledgment email.
  - `id` (string) [maxLen=255] — Represents the unique identifier of the sender configured for the acknowledgment email.
  - `type` (string) **REQ** [maxLen=255] — Represents the type of sender configured for the acknowledgment email.
  - `email` (string) [maxLen=255] — Represents the sender's email address used in the acknowledgment email for the webform.

**Request Body** — application/json `PostwebformsRequest`
> The request body must contain a webforms array with one object.
  > Represents the request body for creating or updating webforms. The request body must contain a webforms array with one object.
  - `webforms` (array of object `WebformsPostReqBody`) [maxItems=1] **REQ** — Contains the list of webform configuration objects included in the request body.
    schema: `WebformsPostReqBody`
    - `id` (string) [maxLen=255] — Specify the unique identifier of the webform to update.
    - `owner` (object `OwnerNested`) — Owner to whom which form should assign
      schema: `OwnerNested`
      - `id` (string) [maxLen=19] — Represents the unique identifier of the user assigned as the owner of the webform.
    - `double_optin_details` (object `DoubleOptinDetailsNested`) — Contain template details
      schema: `DoubleOptinDetailsNested`
      - `confirm_page_content` (string) **REQ** [maxLen=2000] — Represents the HTML content displayed on the confirmation page shown to the visitor after submitting the webform with double opt-in enabled.
      - `email_template` (object `EmailTemplateNested`) **REQ** — Represents the Email Template used for webform acknowledgment or double opt-in confirmation, including the subject and HTML content.
        schema: `EmailTemplateNested`
        - `subject` (string) **REQ** [maxLen=255] — Represents the subject line of the Email Template used for webform acknowledgment or double opt-in confirmation.
        - `from_address` (object `FromAddressNested`) **REQ** — Represents the sender's email address configuration used in acknowledgment emails sent after webform submission.
        - `content` (string) **REQ** [maxLen=200000] — Represents the HTML body content of the Email Template used for webform acknowledgment or double opt-in confirmation.
    - `analytics_data` (object `AnalyticsDataNestedV2`) — contains analytic data
      schema: `AnalyticsDataNestedV2`
      - `analytics_enabled` (boolean) [nullable] — Indicates whether analytics tracking is enabled for the webform. Possible values: true - Analytics tracking is active for the form. false - Analytics tracking is inactive for the form.
      - `url_analytics_enabled` (boolean) [nullable] — Indicates whether URL-based analytics tracking is enabled for the webform. Possible values: true - URL-based analytics tracking is active for the form. false - URL-based analytics tracking is inactive for the form.
    - `module` (object `ModuleNested`) **REQ** — Details of the module for which form was created (Required)
      schema: `ModuleNested`
      - `api_name` (string) **REQ** [maxLen=50] — Represents the display name of the user who created the webform.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the user who created the webform.
    - `acknowledge_visitor` (object `AcknowledgeVisitorNested`) — To acknowledge the visitor  auto response rule after the submission

      schema: `AcknowledgeVisitorNested`
      - `reply_to_address` (object `ReplyToAddressNested`) **REQ** — Represents the reply-to address configuration for acknowledgment emails sent after webform submission.
        schema: `ReplyToAddressNested`
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the reply-to address configuration.
        - `type` (string) **REQ** [maxLen=255] — Represents the type of the reply-to address used in acknowledgment emails.
        - `email` (string) [maxLen=255] — Represents the reply-to email address for acknowledgment emails sent after webform submission.
        - `api_name` (string) [maxLen=255] — Represents the API name associated with the reply-to address for acknowledgment emails.
      - `template_name` (string) **REQ** [maxLen=255] — Represents the name of the Email Template used to acknowledge the visitor upon webform submission.
      - `auto_response_rule` (object `AutoResponseRuleNested`) **REQ** — Represents the auto-response rule configuration used to send automatic email responses after webform submission.
        schema: `AutoResponseRuleNested`
        - `name` (string) [maxLen=50, nullable] — Represents the name of the auto-response rule associated with the webform.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the auto-response rule associated with the webform.
      - `template_id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the Email Template used to send an acknowledgment message to the visitor upon webform submission.
      - `from_address` (object `FromAddressNested`) **REQ** — Represents the sender's email address configuration used in acknowledgment emails sent after webform submission.
      - `email_meta` (object `EmailMetaNested`) — Represents the email metadata for a webform, including organization email addresses and user lookup email configurations.
        schema: `EmailMetaNested`
        - `userLookupEmailsObj` (object) **REQ** — Represents the user lookup email addresses available for webform email configuration.
        - `otherEmailsObj` (object) **REQ** — Represents other email address objects available for webform email configuration.
        - `orgEmailsArr` (array of object `OrgemailobjNested`) [maxItems=0] **REQ** — Contains the list of organization email addresses available for configuring the from-address of webform notification emails.
          schema: `OrgemailobjNested`
          - `email_id` (string/email) [maxLen=255] — Represents the email address of the organization email account configured for webform notifications.
          - `isaccessible` (boolean) — Indicates whether the organization email account is accessible for use in webform notifications. Possible values: true - The account is accessible. false - The account is not accessible.
          - `name` (string) [maxLen=255] — Represents the display name of the organization email account.
          - `id` (string) [maxLen=255] — Represents the unique identifier of the organization email account.
    - `button_attributes` (array of object `ButtonAttributesNested`) [maxItems=2, nullable] — Specify the button attribute configurations for the webform, such as the Submit and Reset buttons.
      schema: `ButtonAttributesNested`
      - `color` (string) **REQ** [maxLen=255] — Specifies the color applied to the button element within the webform.
      - `name` (string) **REQ** [maxLen=255] — Represents the internal name identifier of the button attribute within the webform.
    - `notify_owner` (object `NotifyOwnerNested`) — We can notify the owner once form submitted by the user through system generated mail or custom template
      schema: `NotifyOwnerNested`
      - `name` (string) [maxLen=255] — Represents the name of the Email Template used to notify the webform owner upon form submission.
      - `id` (string) [maxLen=255] — Represents the unique identifier of the Email Template used to notify the webform owner upon form submission.
      - `system_mail` (boolean) [nullable] — Indicates whether the system sends a notification email to the webform owner upon form submission. Possible values: true - The system sends a notification email. false - The system does not send a notification email.
    - `type` (string) **REQ** [maxLen=255, enum=['webform', 'portalform']] — Specify the type of the form. Possible values: webform - A standard webform. portalform - A portal form for registered portal users.
    - `form_attributes` (object `FormAttributesNested`) — Attributes of the form like font, style,size etc.,
      schema: `FormAttributesNested`
      - `color` (string) **REQ** [maxLen=255] — Specifies the background color of the webform.
      - `width` (integer/int32) **REQ** — Specifies the width of the webform in pixels.
      - `font_attributes` (object `FontAttributesNested`) **REQ** — Represents the font attribute settings applied to the webform text, including font size, color, and family.
        schema: `FontAttributesNested`
        - `size` (integer/int32) **REQ** — Specifies the font size applied to the text in the webform.
        - `color` (string) **REQ** [maxLen=255] — Specifies the font color applied to the text in the webform.
        - `family` (string) **REQ** [maxLen=255] — Specifies the font family applied to the text in the webform.
      - `display_form_name` (boolean) — Indicates whether the form name is displayed on the webform. Possible values: true - The form name is shown. false - The form name is hidden.
      - `align` (string) **REQ** [maxLen=255] — Specifies the horizontal alignment of the webform content.
    - `action_on_submit` (string) **REQ** [maxLen=20, enum=['splash_message', 'thank_you_message', 'redirect_url']] — Specify the action performed after the visitor submits the webform. Possible values: splash_message - Displays a splash message. thank_you_message - Displays a thank-you message. redirect_url - Redirects the visitor to a specified URL.
    - `location_url` (array of string) [maxItems=20] **REQ** — Specify the list of URLs of the pages where the webform is hosted.
      items: [maxLen=2000]
    - `tags` (array of object `TagsNested`) [maxItems=10, nullable] — Specify the list of tags to associate with the webform.
      schema: `TagsNested`
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the tag associated with the webform.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the tag associated with the webform.
    - `double_optin_enabled` (boolean) [nullable] — Specify whether double opt-in confirmation is enabled for the webform. Possible values: true - Double opt-in is enabled. false - Double opt-in is disabled.
    - `layout` (object `LayoutNested`) **REQ** — Layout of the module (Required)
      schema: `LayoutNested`
      - `display_label` (string) [maxLen=255] — Represents the display label of the layout associated with the webform.
      - `name` (string) [maxLen=255] — Represents the name of the layout associated with the webform.
      - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents the unique identifier of the layout associated with the webform.
    - `form_fields` (array of object `FormFieldsNested`) [maxItems=50] **REQ** — Specify the list of form field configurations to include in the webform.
      schema: `FormFieldsNested`
      - `type` (string) **REQ** [maxLen=255, enum=['general', 'advanced', 'portal']] — Represents the type of form field configured on the webform.
      - `help` (object) [nullable] — Represents the help text configuration displayed alongside the field on the webform.
      - `field` (object `FieldNested`) — Represents a CRM field reference configured on the webform, including the field API name, label, and identifier.
        schema: `FieldNested`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM field configured on the webform.
        - `field_label` (string) [maxLen=255] — Represents the display label of the CRM field as shown on the webform.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the CRM field configured on the webform.
      - `hidden` (boolean) [nullable] — Indicates whether the field is hidden on the webform. Possible values: true - The field is hidden. false - The field is visible.
      - `date_format` (string) [maxLen=20, nullable] — Represents the date format applied to date fields on the webform.
      - `required` (boolean) [nullable] — Indicates whether the field is required on the webform. Possible values: true - The field is required. false - The field is not required.
      - `field_name` (string) [maxLen=255, nullable] — Represents the display name of the CRM field as shown on the webform.
      - `site_key` (string) [maxLen=50, nullable] — Represents the site key used to render the reCAPTCHA element on the webform.
      - `secret_key` (string) [maxLen=50, nullable] — Represents the secret key used to verify the reCAPTCHA response for the webform.
      - `recaptcha_label` (string) [maxLen=50, nullable] — Represents the label displayed on the reCAPTCHA element within the webform.
      - `theme` (string) [maxLen=5, enum=['dark', 'light'], nullable] — Represents the visual theme applied to the reCAPTCHA element on the webform.
      - `privacy_value` (string) [maxLen=2000, nullable] — Represents the privacy policy content or URL associated with the privacy field on the webform.
      - `default_value` (string) [maxLen=32000, nullable] — Represents the default value pre-populated in the hidden field on the webform.
      - `field_info` (object `AdvanceFieldNested`) — Represents the configuration of an advanced field associated with a webform.
        schema: `AdvanceFieldNested`
        - `type` (string) **REQ** [maxLen=255] — Specifies the API name that identifies the type of the advanced field configured on the webform.
        - `field_label` (string) [maxLen=255] — Represents the display label of the field as it appears on the webform.
    - `user_type` (object `UserTypeNested`) — portal form details
      schema: `UserTypeNested`
      - `name` (string) [maxLen=50, nullable] — Represents the name of the portal configured for the webform.
      - `active` (boolean) [nullable] — Indicates whether the portal form is active. Possible values: true - The portal form is active. false - The portal form is inactive.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the portal configured for the webform.
    - `assignment_rule` (object `AssignmentRuleNested`) — Contains assignment rule details
      schema: `AssignmentRuleNested`
      - `name` (string) [maxLen=255] — Represents the name of the Assignment Rule associated with the webform.
      - `id` (string) [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — Represents the unique identifier of the Assignment Rule associated with the webform.
    - `create_contact` (boolean) [nullable] — Specify whether the system also creates a Contacts record when the webform is submitted. Possible values: true - The system also creates a Contacts record. false - The system creates only a Leads record.
    - `approval_request` (boolean) [nullable] — Specify whether submitted records require manual approval before being added to Zoho CRM. Possible values: true - Manual approval is required. false - Records are added without manual approval.
    - `name` (string) **REQ** [maxLen=128] — Specify the name of the webform.
    - `action_value` (string) [maxLen=2000, nullable] — Specify the value associated with the action performed after webform submission, such as the redirect URL or message content.
    - `spam_control` (object `SpamControlNested`) — spam control
      schema: `SpamControlNested`
      - `spam_possibility_threshold` (integer/int32) **REQ** — Specifies the spam likelihood threshold value used to filter potentially spam submissions.
    - `visitor_tracking` (object `VisitorTrackingNested`) — To track visitors, record active history and to generate analytics

      schema: `VisitorTrackingNested`
      - `portal_name` (string) **REQ** [maxLen=30] — Represents the name of the visitor tracking integration portal associated with the webform.
      - `tracking_code` (string) [maxLen=30, nullable] — Represents the tracking code used to identify the visitor tracking portal for the webform.

**Responses:**

- **201**: Returns a success response confirming webform creation, including the status, result code, and the unique identifier of the newly created webform. — Schema: `WebformsSuccessResponse` [application/json]
    > Represents the success response for a webform create or update operation, including the result status for each webform.
    schema: `WebformsSuccessResponse`
    - `webforms` (array of object `SuccessResponse`) [maxItems=1] — Contains the list of webform result objects in the success response.
      schema: `SuccessResponse`
      - `code` (string) [enum=['SUCCESS']] — Represents the status code of the API response.
      - `details` (object) — Represents additional details about the API response, such as the ID of the created or modified resource.
      - `message` (string) [maxLen=255] — Represents the response message describing the outcome of the operation.
      - `status` (string) [enum=['success']] — Represents the status of the API response. Possible values: success - The operation was successful.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Invalid or incomplete request data supplied for webform creation.
**Resolution:** The request payload must include all mandatory fields with values that conform to expected formats, contain no duplicate or unsupported data, correctly pair dependent fields, and not exceed the permitted request body size. [application/json]
    > Represents a client error returned when a webform creation request fails. Contains either a WebformsErrorResponse1 or an ErrorResponse object, depending on the nature of the validation or processing error.
    oneOf:
      - `WebformsErrorResponse1` — Represents the top-level error response wrapper returned when one or more webform operations fail, containing per-webform error details.
        - `webforms` (array of object `ErrorResponse`) [maxItems=25] **REQ** — Contains the list of per-webform error result objects in the wrapped error response.
      - `ErrorResponse` — Represents a generic API error response containing an error code, status, message, and details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.webforms.CREATE
