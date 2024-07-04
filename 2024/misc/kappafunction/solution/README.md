# Kappafunctions
This is a simple exercise in enumerating a JavaScript context.

A contestant needs to learn how to send simple scripts throught the website and realize which services are available.

The kappafunctions service accepts a script and runs it through a Goja VM. In this case there are no libraries available other than "console". Which allows the contestant to run a script and get output from the VM. 

The flag can be found in a global variable, so a contestant needs to find a way to enumerate all objects in the global context.

One possible solution is the following

```js
console = require("console")
for(const key of Object.getOwnPropertyNames(this)) {
    console.log(key,this[key])
}
```

Which will reveal the flag.