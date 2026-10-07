# ScratchWeb
~~HTTP~~ ~~GET~~ requests in vanilla Scratch 3.0

# How can I do this?
- Create a certificate. Name it `server.crt` with the key file named `server.key`.
- Install the `requirements.txt` dependencies
- Simply add `127.0.0.1 translate-service.scratch.mit.edu` to your hosts file (on windows - ~~untested on linux~~ Linux works too - untested on macOS)
- Run `server.py`
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

Audio is not natively supported anymore. Please use something like [this](https://scratch.mit.edu/projects/1184501461/) to play audio.

## Images

ScratchWeb can convert image files to a Scratch-friendly base64 format.
See `image-client.sb3` for an example.

## WebSockets

ScratchWeb now supports WebSockets!

- URL must start with `ws` or `wss`
- Language is irrelevant
- The body will be sent to the WS server, the response will be received
- Status code is hardcoded to `200`, filetype to `t`
