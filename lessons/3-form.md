---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
color: 266089
html: true

---
![bg left:50% 70%](assets/nuvolaris-logo.png)


### Developing Open LLM applications with

<center>
<img width="100%"src="assets/openserverless-logo.png">
</center>

## Lesson 3

## Form support and Prompt Engineering


---
![bg left:50% 80%](assets/mastrogpt.png)

## Form support and Prompt Engineering

- Authentication

- Using form: post generator

- Prompt Engineering: a web rag

- Exercise: TODO

---

![bg](https://fakeimg.pl/700x400/ff0000,0/0A6BAC?retina=1&text=Authentication)

---
### Authentication

- Actions are normally *not* directly accessible 
   - action invocation must be authenticated with a key
   - the key is stored in `~/.wskprops`
     - you can "source" it

- an action cab be public ("web action")
   - deploy with `--web true`
   - web action invocation is *NOT* authenticated
     - but you can provide **custom** authentication

### Pinocchio supports custom authentication


---
# Some useful **magic** shell tricks

- When you login, a `~/.wskpros` file is created with an API KEY
- You can load the key with `source ~/.wskpros` (in a bash shell)
- you can get the url with `ops url <action>`
  - extract the last line with `| tail +2`
  - store in a variable with `VAR=$(...)`
  - use POST and the flags `blocking=true` and `result=true`

---
## Action authentication

```
code form/hello.py                               # note NO --web true
ops ide devel                                    # deploy everything
ops url form/hello                               # get url
curl https://openserverless.dev/api/v1/namespaces/msciab/actions/form/hello
```

`{"code":"IcWTiEX6DsWKXUmO3AlswEoPvSG5A8wS","error":"The resource requires authentication, which was not supplied with the request"}`

```
source ~/.wskprops                             # loading AUTH
URL=$(ops url form/hello | tail +2)            # get URL
FLAGS="blocking=true&result=true"              # additional flags
curl -u $AUTH -X POST "$URL?$FLAGS"
```

`{"body":"Hello, world"}`

---
## Custom authentication

- Pinocchio uses public **web actions**
  - by default they are **UNPROTECTED**

```
URL=$(ops url form/auth | tail +2)
curl $URL
```

`
{
  "output": "you are authenticated"
}
`

- you can access them freely if you know the URL
  - however it supports an **authentication token**

---

# Pinocchio auth token 

- Invoke from Pinocchio  `Form/Hello`  and check logs
  
`
Token: pinocchio:Z_DaI31ONacHEDjzznBpJW0jDjyBuNWKjDfwZGCm0qY
`

Look in Redis:

```
get msciab:TOKEN:pinocchio
```
`Z_DaI31ONacHEDjzznBpJW0jDjyBuNWKjDfwZGCm0qY`

---
# Auth code

```python
import os, redis
def unauthorized(args):
  [user, secret] = args.get("token", "_:_").split(":")
  rd = redis.from_url(args.get("REDIS_URL", os.getenv("REDIS_URL")))
  check = rd.get(f"{args.get("REDIS_PREFIX", os.getenv("REDIS_PREFIX"))}TOKEN:{user}") or b''
  return check.decode("utf-8") != secret
```

Checking:

```python  
def auth(args):
  if unauthorized(args):
    return { "output": "you are not authenticated" }
  return { "output": "you are authenticated" }
```

---