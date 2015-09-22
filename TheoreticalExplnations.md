# Theoretical Stuff #

Some ideas that come and go while thinking about what's going to
happen next.

## Permissions ##

Initially there's a lot of opportunity to explain how permissions work
on a Unix system.

On the Raspian image, there is a UDev rule which modifies
`/dev/i2c-*` to have `rw` permissions for group
`i2c`. User `pi` is not in that group, which we change very
early on.

  * What happens here?
  * How does this relate to the `open(2)` system call?
  * Elaborate on refcounting semantics of a file decriptor and the `struct file` inside the kernel.
  * Jabber on system calls a lot

How does one impersonate as one particular user?

  * What's the `init` process?
  * `man 2 setuid`
  * Leading to: "What's that `sudo` all the time?"

## Devices and `ioctl(2)` ##

`open(2)` is a system call that works on _anything_ that looks
like a file. Makes up the meat of the Unixen, together with
`read(2)`, `write(2)` and friends. Generic system calls, so to
say.

Hardware is not always so simple. Enter `ioctl(2)`.