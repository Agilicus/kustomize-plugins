envoy_cfg = """
---
static_resources:
  # IP address and ports that Envoy listens to for requests
  listeners:
    - address:
        socket_address:
          address: 0.0.0.0   # because envoy runs inside a docker container
          port_value: 8080
          protocol: TCP
      # defining how to process the requests, filtering
      filter_chains:
        - filters:
            - name: envoy.http_connection_manager  # built-in filter designed for HTTP connections
              typed_config:
                "@type": type.googleapis.com/envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager
                access_log:
                  - name: envoy.file_access_log
                    config:
                      json_format:
                        log_type: ACCESS
                        start_time: '%START_TIME%'
                        method: '%REQ(:METHOD)%'
                        path: '%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)%'
                        protocol: '%PROTOCOL%'
                        response_code: '%RESPONSE_CODE%'
                        response_code_details: '%RESPONSE_CODE_DETAILS%'
                        response_flags: '%RESPONSE_FLAGS%'
                        bytes_received: '%BYTES_RECEIVED%'
                        bytes_sent: '%BYTES_SENT%'
                        duration: '%DURATION%'
                        downstream_local_address: '%DOWNSTREAM_LOCAL_ADDRESS%'
                        downstream_remote_address: '%DOWNSTREAM_REMOTE_ADDRESS%'
                        upstream_service_time: '%RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)%'
                        forwarded_for: '%REQ(X-FORWARDED-FOR)%'
                        user_agent: '%REQ(USER-AGENT)%'
                        request_id: '%REQ(X-REQUEST-ID)%'
                        authority: '%REQ(:AUTHORITY)%'
                        upstream_host: '%UPSTREAM_HOST%'
                        original_dst_host: '%REQ(X-ENVOY-ORIGINAL-DST-HOST)%'
                        upstream_cluster: '%UPSTREAM_CLUSTER%'
                        upstream_local_address: '%UPSTREAM_LOCAL_ADDRESS%'
                        upstream_transport_failure_reason: '%UPSTREAM_TRANSPORT_FAILURE_REASON%'
                        user: '%REQ(X-GATEWAY-USER)%'
                        organisation: '%REQ(X-GATEWAY-ORG)%'
                        token_id: '%REQ(X-GATEWAY-TOKENID)%'
                      path: /dev/fd/1
                http_protocol_options:
                  allow_absolute_url: true
                http_filters:
                  - name: envoy.cors
                  - name: envoy.router
                route_config:
                  name: http-ws
                  virtual_hosts:
                    - domains:
                        - '{cfg[downstream_base_host]}.__ROOT_DOMAIN__'
                      name: gateway
                      routes:
                        - name: main_route
                          match:
                            prefix: "{cfg[prefix]}"
                          route:
                            priority: null
                            timeout: 3.000s
                            weighted_clusters:
                              clusters:
                                - name: "{cfg[cluster_name]}"
                                  weight: 100
                  request_headers_to_remove:
                    - X-B3-Sampled
                    - X-B3-Traceid
                    - X-B3-Spanid
                    - X-Envoy-Expected-Rq-Timeout-Ms
                    - X-Envoy-External-Address
                    - X-Envoy-External-Address
                    - X-Gateway-Org
                    - X-Gateway-Tokenid
                    - X-Gateway-User
                    - X-Istio-Attributes
                    - X-Roles-Matched
                    - X-Token-Valid
                    - X-Whitelisted
                    - X-Forwarded-Proto

                stat_prefix: ingress_http
                use_remote_address: true
          use_proxy_proto: false
      name: tls.listener
    - address:
        socket_address:
          address: 0.0.0.0
          port_value: 8877
          protocol: TCP
      name: health.listener
      filter_chains:
        - filters:
            - typed_config:
                "@type": type.googleapis.com/envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager
                access_log:
                  - config:
                      path: /dev/null
                    name: envoy.file_access_log
                http_filters:
                  - name: envoy.router
                stat_prefix: health_check_http
                route_config:
                  virtual_hosts:
                    - domains:
                        - '*'
                      name: health-check
                      routes:
                        - match:
                            case_sensitive: true
                            prefix: /http-ws/v0/check_alive
                          direct_response:
                            status: 200
                        - match:
                            case_sensitive: true
                            prefix: /http-ws/v0/check_ready
                          direct_response:
                            status: 200
              name: envoy.http_connection_manager
  clusters:
    name: {cfg[cluster_name]}
    connect_timeout: 3s
    lb_policy: ROUND_ROBIN
    type: STRICT_DNS
    transport_socket:
      name: "envoy.transport_sockets.tls"
      typed_config:
        "@type": type.googleapis.com/envoy.api.v2.auth.UpstreamTlsContext
        common_tls_context:
          tls_params:
            tls_maximum_protocol_version: TLSv1_2
          validation_context:
            verify_subject_alt_name: [{cfg[upstream][host]}]
            trusted_ca:
              filename: /etc/ssl/certs/ca-certificates.crt
        sni: {cfg[upstream][host]}
    load_assignment:
      cluster_name: {cfg[cluster_name]}
      endpoints:
        - lb_endpoints:
            - endpoint:
                address:
                  socket_address:
                    address: 127.0.0.1
                    port_value: 5556
                    protocol: TCP
admin:
  access_log_path: "/dev/null"
  address:
    socket_address:
      address: 127.0.0.1
      port_value: 8001
"""
