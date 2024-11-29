---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
html: true
---

![bg left:40% 80%](./logo-full-transparent.png)

## Developing Open LLM applications with Apache OpenServerless 
# Module 2: Assistants

https://www.nuvolaris.io

---

![bg](https://fakeimg.pl/350x200/ff0000,0/000?text=Agenda&retina=1)


---

# Our Goal: build a Chat accessing an Open LLM

- Prerequisites
- Simple UI
- Accessing the LLM

---

![bg](https://fakeimg.pl/350x200/ff0000,0/000?text=Prerequisites&retina=1)

---

# Starting...

```
$ npx create-assistant-ui@latest web
lot of output ... #YMMM
$ cd web
$ npm run dev
```

- Check `http://locahost:3000`
![bg right 90%](welcome.png)

- If you type something now, you get an error...
  - we need to connect to an LLM

