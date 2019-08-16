xinetd_cfg = """
service http_org
{{
    type = UNLISTED
    socket_type = stream
    wait = no
    server_args = localhost 5001 {cfg[upstream][connect_host]} 443
    port = 5556
    server = /usr/bin/corkscrew
    user = root
}}
"""
