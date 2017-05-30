{
  "type": "script",
  "seleniumVersion": "2",
  "formatVersion": 2,
  "steps": [
    {
      "type": "get",
      "url": "http://localhost/addressbook/"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "user"
      },
      "text": "admin"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "user"
      },
      "text": "admin"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "pass"
      },
      "text": "secret"
    },
    {
      "type": "clickElement",
      "locator": {
        "type": "xpath",
        "value": "//form[@id='LoginForm']/input[3]"
      }
    },
    {
      "type": "clickElement",
      "locator": {
        "type": "link text",
        "value": "groups"
      }
    },
    {
      "type": "clickElement",
      "locator": {
        "type": "name",
        "value": "new"
      }
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "group_name"
      },
      "text": "erwf"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "group_header"
      },
      "text": "ssfef"
    },
    {
      "type": "setElementText",
      "locator": {
        "type": "name",
        "value": "group_footer"
      },
      "text": "wfef"
    },
    {
      "type": "clickElement",
      "locator": {
        "type": "name",
        "value": "submit"
      }
    },
    {
      "type": "clickElement",
      "locator": {
        "type": "link text",
        "value": "group page"
      }
    },
    {
      "type": "clickElement",
      "locator": {
        "type": "link text",
        "value": "Logout"
      }
    }
  ],
  "data": {
    "configs": {},
    "source": "none"
  },
  "inputs": [],
  "timeoutSeconds": 60
}