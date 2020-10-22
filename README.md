<img src="https://i.picsum.photos/id/912/200/200.jpg?hmac=tYYyMFni6bya5yEVkwmmFekjWGedHVByLtPI5q1lcyw" align="right" width="131" />

# SparringAPI

*The perfect sparring for your benchmark/integration tests*

<hr/>

**Changelog**: https://sparringapi.io/changelog.html <br/>
**Documentation**: https://sparringapi.io <br/>

<hr/>


## Installation

This project uses `pipenv` to handle python deps, so if you don't have it installed into your system
you can install it with `pip install pipenv`.

    git clone https://github.com/Email-Meter/sparringapi.git
    cd sparringapi
    pipenv install

## Quickstart

### Run from local

    make dev-server

### Run with docker

    docker build --tag sparringapi:latest .
    docker run --name sparringapi -e PORT=8889 -p 8889:8889 sparringapi
    INFO:     Started server process [1]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://0.0.0.0:8889 (Press CTRL+C to quit)

## Usage

By default if you perform a GET request to `/` you will get a simple JSON response (HTTP 200 OK) with a default latency that will vary from 0 to 1 sec.

### Customizable GET params

#### latency

Specify here the latency in seconds. You can use integers or floats (ie: latency=3, latency=10.60).

    time curl -v http://localhost:8889\?latency\=5.9
    *   Trying ::1...
    * TCP_NODELAY set
    * Connected to localhost (::1) port 8889 (#0)
    > GET /?latency=5.9 HTTP/1.1
    > Host: localhost:8889
    > User-Agent: curl/7.64.1
    > Accept: */*
    >
    < HTTP/1.1 200 OK
    < date: Thu, 22 Oct 2020 14:04:03 GMT
    < server: uvicorn
    < content-length: 15
    < content-type: application/json
    <
    * Connection #0 to host localhost left intact
    {"status":"OK"}* Closing connection 0
    curl -v http://localhost:8889\?latency\=5.9  0.01s user 0.01s system 0% cpu 5.957 total


#### status_code

Sets the response status code. By default will always be HTTP 200 OK, but you can set a different one:

    curl -v http://localhost:8889\?status_code\=418
    *   Trying ::1...
    * TCP_NODELAY set
    * Connected to localhost (::1) port 8889 (#0)
    > GET /?status_code=418 HTTP/1.1
    > Host: localhost:8889
    > User-Agent: curl/7.64.1
    > Accept: */*
    >
    < HTTP/1.1 418
    < date: Thu, 22 Oct 2020 14:11:01 GMT
    < server: uvicorn
    < content-length: 15
    < content-type: application/json
    <
    * Connection #0 to host localhost left intact
    {"status":"OK"}* Closing connection 0

Or even you can set it to *random*. In this mode SparringAPI will simulate a "real" environment. Most of the
requests will be 200 or 201, but you might find some 4XX, 500 and 429 errors.

    curl -v http://localhost:8889\?status_code\=random
    *   Trying ::1...
    * TCP_NODELAY set
    * Connected to localhost (::1) port 8889 (#0)
    > GET /?status_code=random HTTP/1.1
    > Host: localhost:8889
    > User-Agent: curl/7.64.1
    > Accept: */*
    >
    < HTTP/1.1 429 Too Many Requests
    < date: Thu, 22 Oct 2020 14:07:42 GMT
    < server: uvicorn
    < content-length: 15
    < content-type: application/json
    <
    * Connection #0 to host localhost left intact
    {"status":"OK"}* Closing connection 0

## License

sparringapi is licensed under the MIT License.  Please see [LICENSE] for licensing details.


[LICENSE]: https://github.com/dnmellen/sparringapi/blob/master/LICENSE

