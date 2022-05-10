# shortUrl

This is a project I created after coming across [shrtco.de public API](https://shrtco.de/docs/) for shortening long URLs. The API allows you to 
1. Generate short URLs (up to three different options to choose from).
2. Enables you to generate the full URL of a short URL that was generated on their platform.
---
## How it works

1. User provides a long url to start the process
2. The [shrtco.de public API](https://shrtco.de/docs/) server checks the provided URL against a list of blacklisted URLs.
- if the provided URL is not on the list, three different short URLs will be generated
```json
{
    "ok": true,
    "result": {
        "code": "psYiHz",
        "short_link": "shrtco.de/psYiHz",
        "full_short_link": "https://shrtco.de/psYiHz",
        "short_link2": "9qr.de/psYiHz",
        "full_short_link2": "https://9qr.de/psYiHz",
        "short_link3": "shiny.link/psYiHz",
        "full_short_link3": "https://shiny.link/psYiHz",
        "share_link": "shrtco.de/share/psYiHz",
        "full_share_link": "https://shrtco.de/share/psYiHz",
        "original_link": "https://www.facebook.com"
    }
}
```
- else an error message together with the reason for denying the service is provided
```json
{
    "ok": false,
    "error_code": 10,
    "error": "The link you entered is a disallowed link, for more infos see shrtco.de/disallowed",
    "disallowed_reason": "Blacklisted Domain: porn"
}
```
---
I built a simple flask application for the endpoint which can be accessed [here](https://rogueman.pythonanywhere.com/).
