---
marp: false
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
#backgroundImage: url('https://marp.app/assets/hero-background.jpg')
html: true

---
![bg left:50% 100%](./mastrogpt.png)

# MastroGPT Course
### Developing Open LLM applications with Apache OpenServerless 

https://www.nuvolaris.io

---
![bg left:50% 80%](./1-intro.excalidraw.png)

## 1. Serveless Functions

- #### Enviroment Setup
- #### Serverless Functions
- #### Submitting a Form
- #### Sample: post generator

---
# Required environment

### - NodeJS 
- required to run the frontend
### - Pinocchio
- the user interface
### - Python and `ops` clin
- installed automatically

---
# Installing `nodejs` using `fnm` 1/2

- Linux/Mac:

```bash
curl -fsSL https://fnm.vercel.app/install | bash
source /home/msciab/.bashrc
fnm use --install-if-missing 22
```

### Test
```
$ node -v
v22.12.0
$ npm -v
10.9.0
```

---
# Installing `nodejs` using `fnm` 2/2


- Windows: 
```
winget install Schniz.fnm
fnm env --use-on-cd | Out-String | Invoke-Expression
fnm use --install-if-missing 22
```
### Test
```
$ node -v
v22.12.0
$ npm -v
10.9.0
```

---
# Installing `ops` and `pinocchio`

```
git clone https://github.com/mastrogpt/pinocchio
cd pinocchio
npm install
```

---


