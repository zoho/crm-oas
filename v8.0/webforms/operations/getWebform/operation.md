# GET /settings/webforms/{id}
**Operation:** `getWebform` — Retrieve a webform by ID
> To retrieve a specific webform by its ID, use this endpoint in Zoho CRM. The operation returns the configuration and details of a single webform record identified by the required path parameter.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: Specify the unique [Webform ID](webforms.yaml#$.paths./settings/webforms.get).
- `module` (query, string, optional) [enum=['Leads']]: Specify the module API name to filter webforms by the target CRM module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `include_inner_details` (query, string, optional) [enum=['user_type.active']]: Specify whether to include inner details such as portal information in the webforms response. Possible values: true - Include inner details. false - Exclude inner details.
- `from_time` (query, string, optional) [enum=['10-11-2025 12:00:00']]: Specify the start date and time for the analytics data period in ISO 8601 format.
- `to_time` (query, string, optional) [enum=['11-11-2025 12:00:00']]: Specify the end date and time for the analytics data period in ISO 8601 format.

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

**Responses:**

- **200**: Returns the details of the specified webform, including its configuration and associated attributes. — Schema: `GetWebformResponse` [application/json]
    > Represents the detailed response for a single webform retrieval, including configuration and all associated settings.
    schema: `GetWebformResponse`
    - `webforms` (array of object `WebformsNested3`) [maxItems=1] **REQ** — Contains the list of webform detail objects returned for the requested webform.
      schema: `WebformsNested3`
      - `google_site` (null) **REQ** — Represents the URL of the Google Site page where the webform is embedded.
      - `encrypted_form_id` (string) **REQ** [maxLen=255] — Represents the encrypted identifier of the webform, used for generating embed code.
      - `acknowledge_visitor` (object `AcknowledgeVisitorNested`) **REQ** — Represents the auto-response configuration for acknowledging a visitor after webform submission, including the Email Template and reply-to address.
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
      - `button_attributes` (array of object `ButtonAttributesNested`) [maxItems=2, nullable] **REQ** — Contains the list of button attribute configurations for the webform, such as the Submit and Reset buttons.
        schema: `ButtonAttributesNested`
        - `color` (string) **REQ** [maxLen=255] — Specifies the color applied to the button element within the webform.
        - `name` (string) **REQ** [maxLen=255] — Represents the internal name identifier of the button attribute within the webform.
      - `type` (string) **REQ** [maxLen=255] — Represents the type of the form. Possible values: webform - A standard webform. portalform - A portal form for registered portal users.
      - `action_on_submit` (string) **REQ** [maxLen=255] — Represents the action performed after the visitor submits the webform. Possible values: splash_message - Displays a splash message. thank_you_message - Displays a thank-you message. redirect_url - Redirects the visitor to a specified URL.
      - `form_fields` (array of object) [maxItems=7] **REQ** — Contains the list of form field configuration objects included in the webform.
        anyOf:
          - `FormFieldsNested` — Represents the configuration of a field included in the webform, including field reference, visibility, required status, and field type.
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
      - `encrypted_zgid` (string) **REQ** [maxLen=255] — Represents the encrypted organization identifier associated with the webform.
      - `action_value` (string) **REQ** [maxLen=2000] — Represents the value associated with the action performed after webform submission, such as the redirect URL or message content.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the webform.
      - `owner` (object) **REQ** [nullable] — Represents the user assigned as the owner of the webform.
      - `created_time` (string) **REQ** [maxLen=255] — Represents the timestamp of webform creation.
      - `double_optin_details` (object `DoubleOptinDetailsNested`) **REQ** — Represents the double opt-in configuration for a webform, including the confirmation Email Template and confirmation page content.
        schema: `DoubleOptinDetailsNested`
        - `confirm_page_content` (string) **REQ** [maxLen=2000] — Represents the HTML content displayed on the confirmation page shown to the visitor after submitting the webform with double opt-in enabled.
        - `email_template` (object `EmailTemplateNested`) **REQ** — Represents the Email Template used for webform acknowledgment or double opt-in confirmation, including the subject and HTML content.
          schema: `EmailTemplateNested`
          - `subject` (string) **REQ** [maxLen=255] — Represents the subject line of the Email Template used for webform acknowledgment or double opt-in confirmation.
          - `from_address` (object `FromAddressNested`) **REQ** — Represents the sender's email address configuration used in acknowledgment emails sent after webform submission.
          - `content` (string) **REQ** [maxLen=200000] — Represents the HTML body content of the Email Template used for webform acknowledgment or double opt-in confirmation.
      - `analytics_data` (object `AnalyticsDataNested3`) **REQ** — Represents the analytics configuration for a webform, including analytics status, tracking codes, and URL-based analytics settings.
        schema: `AnalyticsDataNested3`
        - `iframe_url_tracking_code` (string) **REQ** [maxLen=2000] — Represents the tracking code embedded within the iframe URL for analytics tracking of the webform.
        - `url_analytics_enabled` (boolean) **REQ** — Indicates whether URL-based analytics tracking is enabled for the webform. Possible values: true - URL-based analytics tracking is active for the form. false - URL-based analytics tracking is inactive for the form.
        - `analytics_enabled` (boolean) **REQ** — Indicates whether analytics tracking is enabled for the webform. Possible values: true - Analytics tracking is active for the webform. false - Analytics tracking is inactive for the webform.
        - `analytics_enabled_time` (string) **REQ** [maxLen=255] — Represents the date and time at which analytics tracking was enabled for the webform.
        - `tracking_code` (string) **REQ** [maxLen=2000] — Represents the analytics tracking code associated with the webform, used to monitor visitor interactions and form submissions.
      - `module` (object `ModuleNested`) **REQ** — Represents the CRM module associated with the webform, including its API name and identifier.
        schema: `ModuleNested`
        - `api_name` (string) **REQ** [maxLen=50] — Represents the display name of the user who created the webform.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the user who created the webform.
      - `suggestion` (null) **REQ** — Represents the AI-generated suggestion for improving the webform's performance.
      - `encrypted_module` (string) **REQ** [maxLen=255] — Represents the encrypted API name of the CRM module associated with the webform.
      - `active` (boolean) **REQ** — Indicates whether the webform is active. Possible values: true - The webform is active. false - The webform is inactive.
      - `adword_enabled` (boolean) **REQ** — Indicates whether Google AdWords tracking is enabled for the webform. Possible values: true - AdWords tracking is active. false - AdWords tracking is inactive.
      - `notify_owner` (object `NotifyOwnerNested`) **REQ** — Represents the notification configuration for the webform owner, including the Email Template and system-mail toggle.
        schema: `NotifyOwnerNested`
        - `name` (string) [maxLen=255] — Represents the name of the Email Template used to notify the webform owner upon form submission.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the Email Template used to notify the webform owner upon form submission.
        - `system_mail` (boolean) [nullable] — Indicates whether the system sends a notification email to the webform owner upon form submission. Possible values: true - The system sends a notification email. false - The system does not send a notification email.
      - `created_by` (object `CreatedByNested3`) **REQ** — Represents the user who created the webform record, including their identifier and display name.
        schema: `CreatedByNested3`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user associated with the creation of the webform record.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the user associated with the creation of the webform record.
      - `form_attributes` (object `FormAttributesNested`) **REQ** — Represents the visual configuration of the webform, including color, width, alignment, font attributes, and display name toggle.
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
      - `location_url` (array of string) [maxItems=2] **REQ** — Contains the list of URLs of the pages where the webform is hosted.
        items: [maxLen=255]
      - `double_optin_enabled` (boolean) **REQ** — Indicates whether double opt-in confirmation is enabled for the webform. Possible values: true - Double opt-in is enabled. false - Double opt-in is disabled.
      - `tags` (array of object `TagsNested`) [maxItems=2] **REQ** — Contains the list of tags associated with the webform.
        schema: `TagsNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the tag associated with the webform.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the tag associated with the webform.
      - `layout` (object `LayoutNested`) **REQ** — Represents the layout associated with the webform, including its identifier, name, and display label.
        schema: `LayoutNested`
        - `display_label` (string) [maxLen=255] — Represents the display label of the layout associated with the webform.
        - `name` (string) [maxLen=255] — Represents the name of the layout associated with the webform.
        - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents the unique identifier of the layout associated with the webform.
      - `approval_request` (boolean) **REQ** — Indicates whether submitted records require manual approval before being added to Zoho CRM. Possible values: true - Manual approval is required. false - Records are added without manual approval.
      - `create_contact` (boolean) **REQ** — Specify whether the system also creates a Contacts record when the webform is submitted. Possible values: true - The system also creates a Contacts record. false - The system creates only a Leads record.
      - `assignment_rule` (object `AssignmentRuleNested`) **REQ** — Represents the Assignment Rule associated with a webform, used to automatically assign submitted records to a CRM user.
        schema: `AssignmentRuleNested`
        - `name` (string) [maxLen=255] — Represents the name of the Assignment Rule associated with the webform.
        - `id` (string) [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — Represents the unique identifier of the Assignment Rule associated with the webform.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the webform.
      - `visitor_tracking` (null) **REQ** — Represents the visitor tracking configuration for the webform.
      - `spam_control` (object `SpamControlNested`) **REQ** — Represents the spam control configuration for the webform, including the spam likelihood threshold.
        schema: `SpamControlNested`
        - `spam_possibility_threshold` (integer/int32) **REQ** — Specifies the spam likelihood threshold value used to filter potentially spam submissions.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: Indicates that no webform was found for the specified ID.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request contains an invalid or missing parameter.
**Resolution:** The caller must ensure that the webform ID supplied in the path is valid and that all required query parameters — including the module name — are present and valid before resubmitting the request. [application/json]
    > Represents the error response returned for a failed GET webform request, expressed as either a wrapped array of webform errors or a generic error response.
    anyOf:
        - `webforms` (array of object `ErrorResponse`) [maxItems=25] **REQ** — Contains the list of error objects returned when the webform request fails validation.
      - `ErrorResponse` — Represents a generic API error response containing an error code, status, message, and details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The user does not have permission to retrieve webform details.\ n**Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `ErrorResponse` [application/json]
    > Represents a generic API error response containing an error code, status, message, and details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.webforms.READ
