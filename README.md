# ScratchHTTP
HTTP ~~GET~~ requests in vanilla Scratch 3.0

# How can I do this?
- Create a certificate. Name it `text-server.crt` with the key file named `text-server.key`.
- Install the following dependencies: `flask` `requests` `pillow`
- Simply add `127.0.0.1 translate-service.scratch.mit.edu` to your hosts file (on windows - ~~untested on linux~~ Linux works too - untested on macOS)
- Run `text-server.py`
- Add a security exception for `translate-service.scratch.mit.edu` in your browser; the certificate is self-signed, and therefore, insecure

# How is this possible?

![Screenshot (19)](https://github.com/mutethecat/ScratchHTTP/assets/71191728/c9948c14-1ffe-44fc-92b9-1a9e0f00f447)
When the translate feature is used in scratch, It sends an HTTP GET request to "translate-service.scratch.mit.edu".

![Screenshot (16)](https://github.com/mutethecat/ScratchHTTP/assets/71191728/23c41d18-7ac6-446a-9f49-108e15b9d77c)
Route the "translate-service.scratch.mit.edu" to localhost in the hosts file.

![Screenshot (15)](https://github.com/mutethecat/ScratchHTTP/assets/71191728/e2bbd37c-5c62-40a4-ade4-986c3efcccb5)
Create a custom script to take the parameters that Scratch sends and use the string parameter as the url to return the content of.

![Screenshot (17)](https://github.com/mutethecat/ScratchHTTP/assets/71191728/d90d53eb-29be-4f64-a751-78911fe6a61d)

# Improvements
Now supporting all of the following request methods:
- GET
- POST
- PUT
- DELETE
- PATCH

## Text Format

### Input Format
```
https://example.com|body
         ^^          ^^
         URL        Body
               If applicable;
                 Leave empty
                 if not used
                (Keep the |)
```

### Output Format
```
200|filetype|body <- Body
 ^     ^^<< Filetype
Status code h = Html
            c = Css
            t = plainText
            i = Image (base64 encoded)
            d = Data (lowercase hex encoded)
```

## Request Methods

Change the target language to select the request method:

|Language|Request|Uses Body?|
|---|---|---|
|Amharic|GET|No|
|Arabic|POST|Yes|
|Azerbaijani|PUT|Yes|
|Basque|DELETE|No|
|Bulgarian|PATCH|Yes|
|Zulu|[Dummy Request]|No|

- The Dummy Request can be used as a "padding" between requests, in case Scratch's caching system is causing unexpected behavior.

## Audio

ScratchHTTP now supports playing back audio!

### Setup differences
- The certificate/key should be named `sound-server.`(`crt`/`key`)
- Add `127.0.0.1 synthesis-service.scratch.mit.edu` to the hosts file
- Likewise, add the security exception for `synthesis-service.scratch.mit.edu`
- Run `sound-server.py` instead of `text-server`

### Usage differences
- Only GET is supported
- You just need to type in the URL; nothing else is needed
- The audio file at the URL will be played back

## Images

ScratchHTTP can convert image files to a Scratch-friendly base64 format.
See `image-client.sb3` for an example.
