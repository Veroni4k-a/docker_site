 docker logs my-running-site
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/09/24 07:47:22 [notice] 1#1: using the "epoll" event method
2025/09/24 07:47:22 [notice] 1#1: nginx/1.29.1
2025/09/24 07:47:22 [notice] 1#1: built by gcc 14.2.0 (Alpine 14.2.0) 
2025/09/24 07:47:22 [notice] 1#1: OS: Linux 6.14.0-29-generic
2025/09/24 07:47:22 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/09/24 07:47:22 [notice] 1#1: start worker processes
2025/09/24 07:47:22 [notice] 1#1: start worker process 30
2025/09/24 07:47:22 [notice] 1#1: start worker process 31
2025/09/24 07:47:22 [notice] 1#1: start worker process 32
2025/09/24 07:47:22 [notice] 1#1: start worker process 33
172.17.0.1 - - [24/Sep/2025:07:47:33 +0000] "GET / HTTP/1.1" 200 548 "-" "curl/8.5.0" "-"
172.17.0.1 - - [24/Sep/2025:07:47:44 +0000] "GET / HTTP/1.1" 200 548 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
172.17.0.1 - - [24/Sep/2025:07:47:44 +0000] "GET /style.css HTTP/1.1" 200 520 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/24 07:47:44 [error] 33#33: *4 open() "/usr/share/nginx/html/docker-logo.png" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /docker-logo.png HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [24/Sep/2025:07:47:44 +0000] "GET /docker-logo.png HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/24 07:47:44 [error] 33#33: *4 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [24/Sep/2025:07:47:44 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
172.17.0.1 - - [24/Sep/2025:07:51:25 +0000] "GET / HTTP/1.1" 200 548 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
172.17.0.1 - - [24/Sep/2025:07:51:25 +0000] "GET /style.css HTTP/1.1" 200 520 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/24 07:51:25 [error] 30#30: *6 open() "/usr/share/nginx/html/docker-logo.png" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /docker-logo.png HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [24/Sep/2025:07:51:25 +0000] "GET /docker-logo.png HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/25 14:26:36 [notice] 1#1: signal 3 (SIGQUIT) received, shutting down
2025/09/25 14:26:36 [notice] 32#32: gracefully shutting down
2025/09/25 14:26:36 [notice] 31#31: gracefully shutting down
2025/09/25 14:26:36 [notice] 32#32: exiting
2025/09/25 14:26:36 [notice] 31#31: exiting
2025/09/25 14:26:36 [notice] 30#30: gracefully shutting down
2025/09/25 14:26:36 [notice] 30#30: exiting
2025/09/25 14:26:36 [notice] 30#30: exit
2025/09/25 14:26:36 [notice] 33#33: gracefully shutting down
2025/09/25 14:26:36 [notice] 33#33: exiting
2025/09/25 14:26:36 [notice] 33#33: exit
2025/09/25 14:26:36 [notice] 32#32: exit
2025/09/25 14:26:36 [notice] 31#31: exit
2025/09/25 14:26:36 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2025/09/25 14:26:36 [notice] 1#1: worker process 30 exited with code 0
2025/09/25 14:26:36 [notice] 1#1: worker process 31 exited with code 0
2025/09/25 14:26:36 [notice] 1#1: worker process 32 exited with code 0
2025/09/25 14:26:36 [notice] 1#1: signal 29 (SIGIO) received
2025/09/25 14:26:36 [notice] 1#1: signal 17 (SIGCHLD) received from 33
2025/09/25 14:26:36 [notice] 1#1: worker process 33 exited with code 0
2025/09/25 14:26:36 [notice] 1#1: exit
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: IPv6 listen already enabled
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/09/26 07:56:01 [notice] 1#1: using the "epoll" event method
2025/09/26 07:56:01 [notice] 1#1: nginx/1.29.1
2025/09/26 07:56:01 [notice] 1#1: built by gcc 14.2.0 (Alpine 14.2.0) 
2025/09/26 07:56:01 [notice] 1#1: OS: Linux 6.14.0-29-generic
2025/09/26 07:56:01 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/09/26 07:56:01 [notice] 1#1: start worker processes
2025/09/26 07:56:01 [notice] 1#1: start worker process 22
2025/09/26 07:56:01 [notice] 1#1: start worker process 23
2025/09/26 07:56:01 [notice] 1#1: start worker process 24
2025/09/26 07:56:01 [notice] 1#1: start worker process 25
172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET /style.css HTTP/1.1" 200 520 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/26 07:59:31 [error] 23#23: *4 open() "/usr/share/nginx/html/docker-logo.png" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /docker-logo.png HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET /docker-logo.png HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/26 07:59:31 [error] 23#23: *4 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-








docker logs -f my-running-site
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/09/24 07:47:22 [notice] 1#1: using the "epoll" event method
2025/09/24 07:47:22 [notice] 1#1: nginx/1.29.1
2025/09/24 07:47:22 [notice] 1#1: built by gcc 14.2.0 (Alpine 14.2.0) 
2025/09/24 07:47:22 [notice] 1#1: OS: Linux 6.14.0-29-generic
2025/09/24 07:47:22 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/09/24 07:47:22 [notice] 1#1: start worker processes
2025/09/24 07:47:22 [notice] 1#1: start worker process 30
2025/09/24 07:47:22 [notice] 1#1: start worker process 31
2025/09/24 07:47:22 [notice] 1#1: start worker process 32
2025/09/24 07:47:22 [notice] 1#1: start worker process 33
172.17.0.1 - - [24/Sep/2025:07:47:33 +0000] "GET / HTTP/1.1" 200 548 "-" "curl/8.5.0" "-"
172.17.0.1 - - [24/Sep/2025:07:47:44 +0000] "GET / HTTP/1.1" 200 548 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
172.17.0.1 - - [24/Sep/2025:07:47:44 +0000] "GET /style.css HTTP/1.1" 200 520 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/24 07:47:44 [error] 33#33: *4 open() "/usr/share/nginx/html/docker-logo.png" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /docker-logo.png HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [24/Sep/2025:07:47:44 +0000] "GET /docker-logo.png HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/24 07:47:44 [error] 33#33: *4 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [24/Sep/2025:07:47:44 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
172.17.0.1 - - [24/Sep/2025:07:51:25 +0000] "GET / HTTP/1.1" 200 548 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
172.17.0.1 - - [24/Sep/2025:07:51:25 +0000] "GET /style.css HTTP/1.1" 200 520 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/24 07:51:25 [error] 30#30: *6 open() "/usr/share/nginx/html/docker-logo.png" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /docker-logo.png HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [24/Sep/2025:07:51:25 +0000] "GET /docker-logo.png HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/25 14:26:36 [notice] 1#1: signal 3 (SIGQUIT) received, shutting down
2025/09/25 14:26:36 [notice] 32#32: gracefully shutting down
2025/09/25 14:26:36 [notice] 31#31: gracefully shutting down
2025/09/25 14:26:36 [notice] 32#32: exiting
2025/09/25 14:26:36 [notice] 31#31: exiting
2025/09/25 14:26:36 [notice] 30#30: gracefully shutting down
2025/09/25 14:26:36 [notice] 30#30: exiting
2025/09/25 14:26:36 [notice] 30#30: exit
2025/09/25 14:26:36 [notice] 33#33: gracefully shutting down
2025/09/25 14:26:36 [notice] 33#33: exiting
2025/09/25 14:26:36 [notice] 33#33: exit
2025/09/25 14:26:36 [notice] 32#32: exit
2025/09/25 14:26:36 [notice] 31#31: exit
2025/09/25 14:26:36 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2025/09/25 14:26:36 [notice] 1#1: worker process 30 exited with code 0
2025/09/25 14:26:36 [notice] 1#1: worker process 31 exited with code 0
2025/09/25 14:26:36 [notice] 1#1: worker process 32 exited with code 0
2025/09/25 14:26:36 [notice] 1#1: signal 29 (SIGIO) received
2025/09/25 14:26:36 [notice] 1#1: signal 17 (SIGCHLD) received from 33
2025/09/25 14:26:36 [notice] 1#1: worker process 33 exited with code 0
2025/09/25 14:26:36 [notice] 1#1: exit
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: IPv6 listen already enabled
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2025/09/26 07:56:01 [notice] 1#1: using the "epoll" event method
2025/09/26 07:56:01 [notice] 1#1: nginx/1.29.1
2025/09/26 07:56:01 [notice] 1#1: built by gcc 14.2.0 (Alpine 14.2.0) 
2025/09/26 07:56:01 [notice] 1#1: OS: Linux 6.14.0-29-generic
2025/09/26 07:56:01 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025/09/26 07:56:01 [notice] 1#1: start worker processes
2025/09/26 07:56:01 [notice] 1#1: start worker process 22
2025/09/26 07:56:01 [notice] 1#1: start worker process 23
2025/09/26 07:56:01 [notice] 1#1: start worker process 24
2025/09/26 07:56:01 [notice] 1#1: start worker process 25
172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET /style.css HTTP/1.1" 200 520 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/26 07:59:31 [error] 23#23: *4 open() "/usr/share/nginx/html/docker-logo.png" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /docker-logo.png HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET /docker-logo.png HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/26 07:59:31 [error] 23#23: *4 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"



docker logs --tail 10 my-running-site
2025/09/26 07:56:01 [notice] 1#1: start worker process 22
2025/09/26 07:56:01 [notice] 1#1: start worker process 23
2025/09/26 07:56:01 [notice] 1#1: start worker process 24
2025/09/26 07:56:01 [notice] 1#1: start worker process 25
172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET /style.css HTTP/1.1" 200 520 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/26 07:59:31 [error] 23#23: *4 open() "/usr/share/nginx/html/docker-logo.png" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /docker-logo.png HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET /docker-logo.png HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025/09/26 07:59:31 [error] 23#23: *4 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"



docker logs -t my-running-site
2025-09-24T07:47:22.245463672Z /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
2025-09-24T07:47:22.245587547Z /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
2025-09-24T07:47:22.246705592Z /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
2025-09-24T07:47:22.265385106Z 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
2025-09-24T07:47:22.275924975Z 10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
2025-09-24T07:47:22.276046647Z /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
2025-09-24T07:47:22.276265492Z /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
2025-09-24T07:47:22.278278025Z /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
2025-09-24T07:47:22.279305689Z /docker-entrypoint.sh: Configuration complete; ready for start up
2025-09-24T07:47:22.293957935Z 2025/09/24 07:47:22 [notice] 1#1: using the "epoll" event method
2025-09-24T07:47:22.293975359Z 2025/09/24 07:47:22 [notice] 1#1: nginx/1.29.1
2025-09-24T07:47:22.293978834Z 2025/09/24 07:47:22 [notice] 1#1: built by gcc 14.2.0 (Alpine 14.2.0) 
2025-09-24T07:47:22.293981320Z 2025/09/24 07:47:22 [notice] 1#1: OS: Linux 6.14.0-29-generic
2025-09-24T07:47:22.293983875Z 2025/09/24 07:47:22 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025-09-24T07:47:22.296779046Z 2025/09/24 07:47:22 [notice] 1#1: start worker processes
2025-09-24T07:47:22.296924654Z 2025/09/24 07:47:22 [notice] 1#1: start worker process 30
2025-09-24T07:47:22.297259763Z 2025/09/24 07:47:22 [notice] 1#1: start worker process 31
2025-09-24T07:47:22.297942704Z 2025/09/24 07:47:22 [notice] 1#1: start worker process 32
2025-09-24T07:47:22.298310463Z 2025/09/24 07:47:22 [notice] 1#1: start worker process 33
2025-09-24T07:47:33.686210454Z 172.17.0.1 - - [24/Sep/2025:07:47:33 +0000] "GET / HTTP/1.1" 200 548 "-" "curl/8.5.0" "-"
2025-09-24T07:47:44.916864130Z 172.17.0.1 - - [24/Sep/2025:07:47:44 +0000] "GET / HTTP/1.1" 200 548 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025-09-24T07:47:44.972142734Z 172.17.0.1 - - [24/Sep/2025:07:47:44 +0000] "GET /style.css HTTP/1.1" 200 520 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025-09-24T07:47:44.973370220Z 2025/09/24 07:47:44 [error] 33#33: *4 open() "/usr/share/nginx/html/docker-logo.png" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /docker-logo.png HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
2025-09-24T07:47:44.973406580Z 172.17.0.1 - - [24/Sep/2025:07:47:44 +0000] "GET /docker-logo.png HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025-09-24T07:47:44.978457625Z 2025/09/24 07:47:44 [error] 33#33: *4 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
2025-09-24T07:47:44.978563842Z 172.17.0.1 - - [24/Sep/2025:07:47:44 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025-09-24T07:51:25.562943636Z 172.17.0.1 - - [24/Sep/2025:07:51:25 +0000] "GET / HTTP/1.1" 200 548 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025-09-24T07:51:25.575183016Z 172.17.0.1 - - [24/Sep/2025:07:51:25 +0000] "GET /style.css HTTP/1.1" 200 520 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025-09-24T07:51:25.577917603Z 2025/09/24 07:51:25 [error] 30#30: *6 open() "/usr/share/nginx/html/docker-logo.png" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /docker-logo.png HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
2025-09-24T07:51:25.578024185Z 172.17.0.1 - - [24/Sep/2025:07:51:25 +0000] "GET /docker-logo.png HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025-09-25T14:26:36.235583930Z 2025/09/25 14:26:36 [notice] 1#1: signal 3 (SIGQUIT) received, shutting down
2025-09-25T14:26:36.235611980Z 2025/09/25 14:26:36 [notice] 32#32: gracefully shutting down
2025-09-25T14:26:36.235616556Z 2025/09/25 14:26:36 [notice] 31#31: gracefully shutting down
2025-09-25T14:26:36.235619808Z 2025/09/25 14:26:36 [notice] 32#32: exiting
2025-09-25T14:26:36.235622657Z 2025/09/25 14:26:36 [notice] 31#31: exiting
2025-09-25T14:26:36.235625292Z 2025/09/25 14:26:36 [notice] 30#30: gracefully shutting down
2025-09-25T14:26:36.235627928Z 2025/09/25 14:26:36 [notice] 30#30: exiting
2025-09-25T14:26:36.235630652Z 2025/09/25 14:26:36 [notice] 30#30: exit
2025-09-25T14:26:36.235633289Z 2025/09/25 14:26:36 [notice] 33#33: gracefully shutting down
2025-09-25T14:26:36.235635962Z 2025/09/25 14:26:36 [notice] 33#33: exiting
2025-09-25T14:26:36.241377698Z 2025/09/25 14:26:36 [notice] 33#33: exit
2025-09-25T14:26:36.241407706Z 2025/09/25 14:26:36 [notice] 32#32: exit
2025-09-25T14:26:36.241429891Z 2025/09/25 14:26:36 [notice] 31#31: exit
2025-09-25T14:26:36.250981250Z 2025/09/25 14:26:36 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2025-09-25T14:26:36.251111546Z 2025/09/25 14:26:36 [notice] 1#1: worker process 30 exited with code 0
2025-09-25T14:26:36.251191002Z 2025/09/25 14:26:36 [notice] 1#1: worker process 31 exited with code 0
2025-09-25T14:26:36.251279600Z 2025/09/25 14:26:36 [notice] 1#1: worker process 32 exited with code 0
2025-09-25T14:26:36.251389878Z 2025/09/25 14:26:36 [notice] 1#1: signal 29 (SIGIO) received
2025-09-25T14:26:36.267710569Z 2025/09/25 14:26:36 [notice] 1#1: signal 17 (SIGCHLD) received from 33
2025-09-25T14:26:36.267833968Z 2025/09/25 14:26:36 [notice] 1#1: worker process 33 exited with code 0
2025-09-25T14:26:36.268029049Z 2025/09/25 14:26:36 [notice] 1#1: exit
2025-09-26T07:56:01.458616565Z /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
2025-09-26T07:56:01.458887158Z /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
2025-09-26T07:56:01.461893889Z /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
2025-09-26T07:56:01.467529209Z 10-listen-on-ipv6-by-default.sh: info: IPv6 listen already enabled
2025-09-26T07:56:01.467882432Z /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
2025-09-26T07:56:01.468272519Z /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
2025-09-26T07:56:01.472432990Z /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
2025-09-26T07:56:01.474688919Z /docker-entrypoint.sh: Configuration complete; ready for start up
2025-09-26T07:56:01.515056329Z 2025/09/26 07:56:01 [notice] 1#1: using the "epoll" event method
2025-09-26T07:56:01.515097327Z 2025/09/26 07:56:01 [notice] 1#1: nginx/1.29.1
2025-09-26T07:56:01.515105933Z 2025/09/26 07:56:01 [notice] 1#1: built by gcc 14.2.0 (Alpine 14.2.0) 
2025-09-26T07:56:01.515111205Z 2025/09/26 07:56:01 [notice] 1#1: OS: Linux 6.14.0-29-generic
2025-09-26T07:56:01.515116075Z 2025/09/26 07:56:01 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2025-09-26T07:56:01.515484799Z 2025/09/26 07:56:01 [notice] 1#1: start worker processes
2025-09-26T07:56:01.515647280Z 2025/09/26 07:56:01 [notice] 1#1: start worker process 22
2025-09-26T07:56:01.515967465Z 2025/09/26 07:56:01 [notice] 1#1: start worker process 23
2025-09-26T07:56:01.516251254Z 2025/09/26 07:56:01 [notice] 1#1: start worker process 24
2025-09-26T07:56:01.516570487Z 2025/09/26 07:56:01 [notice] 1#1: start worker process 25
2025-09-26T07:59:31.353013474Z 172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025-09-26T07:59:31.442572215Z 172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET /style.css HTTP/1.1" 200 520 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025-09-26T07:59:31.443619671Z 2025/09/26 07:59:31 [error] 23#23: *4 open() "/usr/share/nginx/html/docker-logo.png" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /docker-logo.png HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
2025-09-26T07:59:31.443619840Z 172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET /docker-logo.png HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"
2025-09-26T07:59:31.445286116Z 2025/09/26 07:59:31 [error] 23#23: *4 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
2025-09-26T07:59:31.445318710Z 172.17.0.1 - - [26/Sep/2025:07:59:31 +0000] "GET /favicon.ico HTTP/1.1" 404 153 "http://localhost:8080/" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0" "-"

  
  
  
