# A Simple Server with Python Flask

This is a simple skeleton [Flask][flask] server project that works on any of the
devices supported by [balena][balena-link].

This project simply serves up `"Hello World!"` on port `:80` of your balena
device.

## balena Setup & Deployment

To get this project up and running, you will need to signup for a balena account
[here][signup-page] and set up an application and device. You'll find full
details in our [Getting Started tutorial][gettingStarted-link].

Once you have downloaded this project, you can `balena push` it using the
[balenaCLI][balena-cli]. This command will package up and push the code to the
balena builders, where it will be compiled and built and deployed to every
device in the application fleet. When it completes, you'll have your Python code
running on your device and see some logs on your [balenaCloud
dashboard][balena-dashboard].

To give your device a public URL, access the device page on the [balenaCloud
dashboard][balena-dashboard], and choose the Public Device URL toggle.
Alternatively, you can point your browser to your device's IP address.

[flask]:https://www.palletsprojects.com/p/flask/
[signup-page]:https://dashboard.balena-cloud.com/signup
[gettingStarted-link]:https://www.balena.io/docs/learn/getting-started/raspberrypi3/cpp/
[balena-cli]:https://www.balena.io/docs/reference/cli/
[balena-dashboard]:https://dashboard.balena-cloud.com/
