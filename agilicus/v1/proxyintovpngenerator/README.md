## ProxyIntoVpnGenerator

This generator creates everything needed to expose an HTTP service behind the VPN
to the public internet with no auth/etc.

Note: this assumes *one* thing about the external environment: that a secret has been
created with the tokens necessary to connect to the upstream.

E.g.

```
---
apiVersion: agilicus/v1
kind: ProxyIntoVpnGenerator
metadata:
  name: oidc
  namespace: egov
spec:
  downstream_base_host: oidc
  upstream:
    host: cityadfs.egov.city
    connect_host: adfs01.egov.city
  prefix: "/adfs"
  org_id: 5QZ9wCU3xwHs4XcKAcGghL
  direct_responses:
    - exact_path: "/adfs/.well-known/openid-configuration"
      inline_body:  '{"issuer":"https:\/\/oidc.cloud.egov.city\/adfs","authorization_endpoint":"https:\/\/oidc.cloud.egov.city\/adfs\/oauth2\/authorize\/","token_endpoint":"https:\/\/oidc.cloud.egov.city\/adfs\/oauth2\/token\/","jwks_uri":"https:\/\/oidc.cloud.egov.city\/adfs\/discovery\/keys","token_endpoint_auth_methods_supported":["client_secret_post","client_secret_basic","private_key_jwt","windows_client_authentication"],"response_types_supported":["code","id_token","code id_token","id_token token","code token","code id_token token"],"response_modes_supported":["query","fragment","form_post"],"grant_types_supported":["authorization_code","refresh_token","client_credentials","urn:ietf:params:oauth:grant-type:jwt-bearer","implicit","password","srv_challenge","urn:ietf:params:oauth:grant-type:device_code","device_code"],"subject_types_supported":["pairwise"],"scopes_supported":["winhello_cert","aza","logon_cert","allatclaims","openid","user_impersonation","profile","vpn_cert","email"],"id_token_signing_alg_values_supported":["RS256"],"token_endpoint_auth_signing_alg_values_supported":["RS256"],"access_token_issuer":"http:\/\/oidc.cloud.egov.city\/adfs\/services\/trust","claims_supported":["aud","iss","iat","exp","auth_time","nonce","at_hash","c_hash","sub","upn","unique_name","pwd_url","pwd_exp","mfa_auth_time","sid"],"microsoft_multi_refresh_token":true,"userinfo_endpoint":"https:\/\/oidc.cloud.egov.city\/adfs\/userinfo","capabilities":[],"end_session_endpoint":"https:\/\/oidc.cloud.egov.city\/adfs\/oauth2\/logout","as_access_token_token_binding_supported":true,"as_refresh_token_token_binding_supported":true,"resource_access_token_token_binding_supported":true,"op_id_token_token_binding_supported":true,"rp_id_token_token_binding_supported":true,"frontchannel_logout_supported":true,"frontchannel_logout_session_supported":true,"device_authorization_endpoint":"https:\/\/oidc.cloud.egov.city\/adfs\/oauth2\/devicecode"}'

  tokens_secret: oidc-tokens-secret
```

## Notes

 * `oidc-tokens-secret` will need to contain a jwt named *adfs01.egov.city.jwt*.
 * The org_id should be the org id for the organisation you're installing into.
 * Anything starting with `prefix` will be forwarded to `connect_host` using the sni specified
   by `host`. If `connect_host` is not specified, it will default to `host`.
 * Internally, anything sent to `host` will be redirect to the proxy for forwarding.
 * `downstream_base_host`.BASE_URL will be exposed to the internet for access to this service.
 * `direct_response` may be used to provide hardcoded values without forwarding to the backend service.


