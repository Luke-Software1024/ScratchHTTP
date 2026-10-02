# ScratchHTTP
HTTP ~~GET~~ requests in vanilla Scratch 3.0

# How can I do this?
- Create a certificate. Name it `text-server.crt` with the key file named `text-server.key`.
- Install the following dependencies: `flask` `requests` `pillow`
- Simply add `127.0.0.1 translate-service.scratch.mit.edu` to your hosts file (on windows - ~~untested on linux~~ Linux works too - untested on macOS)
- Run `text-server.py`
- Add a security exception for `translate-service.scratch.mit.edu` in your browser; the certificate is self-signed, and therefore, insecure

# How is this possible?

<img width="1920" height="1032" alt="translate" src="https://github.com/user-attachments/assets/781a1d32-397f-4132-9781-8868d796ce4c" />

When the translate feature is used in scratch, It sends an HTTP GET request to "translate-service.scratch.mit.edu".
<img width="1920" height="299" alt="inspect" src="https://github.com/user-attachments/assets/bb1b271d-b414-4247-9393-7b63ea776f58" />

Route the "translate-service.scratch.mit.edu" to localhost in the hosts file.
<img width="666" height="746" alt="hosts-file" src="https://github.com/user-attachments/assets/a7a80540-5406-424f-9731-ffaccf2633d9" />

Create a custom script to take the parameters that Scratch sends and use the string parameter as the url to return the content of.
<img width="1560" height="943" alt="script" src="https://github.com/user-attachments/assets/1d3f40d1-49b0-486e-9348-dfac99d154ea" />

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
