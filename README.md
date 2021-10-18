# A Simple Server with Python Flask

[![balena deploy button](https://www.balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/balena-io-examples/balena-python-hello-world)

This is a simple skeleton [Flask][flask] server project that works on any of the devices supported by [balena][balena-link].

This project serves up a Welcome page on port `:80` of your balena device.

To get this project up and running, you will need to signup for a balena account [here][signup-page] and set up a device, have a look at our [Getting Started tutorial][gettingStarted-link]. Once you are set up with balena, you will need to clone this repo locally or you can download this repository. 

After downloading, navigate to the directory and `balena push` using the [balena CLI][balena-cli]. This command will package up and push the code to the balena builders, where it will be compiled and built and deployed to every device in the application fleet. When it completes, you'll have a node.js web server running on your device and see some logs on your [balenaCloud dashboard][balena-dashboard].

```bash
cd balena-python-hello-world/
balena push <FLEET_NAME>
```

To give your device a public URL, access the device page on the [balenaCloud dashboard][balena-dashboard], and choose the _Public Device URL_ toggle. Alternatively, you can point your browser to your device's IP address.

Once the device is updated, check the Public Device URL to find the welcome page showing up from your device. 

[flask]:https://www.palletsprojects.com/p/flask/

[balena-link]:https://balena.io/
[signup-page]:https://dashboard.balena-cloud.com/signup
[gettingStarted-link]:http://balena.io/docs/learn/getting-started/
[balena-cli]:https://www.balena.io/docs/reference/cli/
[balena-dashboard]:https://dashboard.balena-cloud.com/
