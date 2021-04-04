# Polyglot Currency converter that can be deployed into MetaCall FaaS

<div align="center">
  <a href="https://dev.to/siddhantkcode/polyglot-programming-with-metacall-308m" target="_blank"><img src="https://i.ibb.co/ccynPCb/Currency-Converter.png" alt="Currency Converter with MetaCall" style="max-width:100%; margin: 0 auto;" width="600" height="auto"></a>
</div>

In this example we will see how we can use a Python script for a Node Script to build a **Polyglot Currency converter**. Link to the article: https://dev.to/siddhantkcode/polyglot-programming-with-metacall-308m.

## Install

Install MetaCall CLI:

```sh
curl -sL https://raw.githubusercontent.com/metacall/install/master/install.sh | sh
```

Install application dependencies:

```sh
metacall pip3 install requests==2.20.0
```

## Run the Application

- add your API Key in [main.py](./main.py#L4)

- Run:

```sh
metacall main.js
```

## LICENSE

[Apache License 2.0](./LICENSE)
