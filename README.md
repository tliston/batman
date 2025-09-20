# Batman

A while back, I wrote a fascinating tool that allows a very low-powered device to act as a honeypot on steroids. It listens and responds on every TCP and UDP port, listens for every IP protocol, and logs EVERYTHING.
While it's lots of fun and provides an unprecedented view of the amount and types of Internet attacks, it also has allowed me to see a whole bunch of the weirdness that's out there on the 'net.

One day, while I was watching attack traffic streaming by, I happened to notice something odd:

![a network attack, containing only the phrase, 'batman'](https://github.com/tliston/batman/blob/main/images/batman.png)

Interestingly, I've seen this same traffic, over and over, targeting various ports, but always containing just the phrase, 'batman.'

But obviously, there's a problem with the code of the tool that is creating this traffic.

This script, batman.py, is my attempt to fix that. (I'm such a kind and generous person.)

If you want to use it, you obviously need to update the `target` and `port` variables. In their current incarnation, they allow you to test the code locally.

Speaking of testing it locally, here's a way to do that:

`socat - TCP-LISTEN:5552,fork,reuseaddr`

There... I fixed it.
