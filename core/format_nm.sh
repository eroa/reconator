#!/bin/bash 
<<<<<<< HEAD
for i in "/tmp/\*nm_reco\*"; do mv "$i" "$(echo $i | tr "'" " ")"; done
=======
for i in /tmp/nm_reco_*; do mv "$i" "$(echo $i | tr "\n" " ")" ; done
>>>>>>> d4463d743b564097bd52dd08eafe2e6bfac039c3
