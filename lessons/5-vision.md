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

## Lesson 5

## Vision and Storage 

---
![bg left:50% 80%](assets/mastrogpt.png)

## Vision and Storage

---

![bg](https://fakeimg.pl/700x400/ff0000,0/0A6BAC?retina=1&text=Vision)

---

# How to do Vision with Ollama

- Use a vision model: `llama3.2-vision:11b``

- URL:  `https://<url>/api/chat`
- Post an image in base64 format:

```python
msg = {
    "model": MODEL,
    "messages": [ {
        "role": "user",
        "content": "what is in this image?",
        "images": [img]
    } ]
}
```

---
# Example

```
```

---

# Vision Form

- Form to upload a file:

```python
FORM = [{
    "label": "any pics?",
    "name": "pic",
    "required": "true",
    "type": "file"
}]
```

- Retrieve base64 encoded image:

```python
  if type(inp) is dict and "form" in inp:
    img = inp.get("form", {}).get("pic", "")
```

---

# Vision Form

- A Vision Class

```
!code packages/vision/form/vision.py
!code tests/vision/test_form.py
```

- The Vision Form action
```
!code packages/vision/form/form.py
```
---

![bg 95%](5-vision/form-vision-etc.png)

---

![bg](https://fakeimg.pl/700x400/ff0000,0/0A6BAC?retina=1&text=S3+Storage)

---
# Accessing S3

---

![bg](https://fakeimg.pl/700x400/ff0000,0/0A6BAC?retina=1&text=Vision+on+Store)

