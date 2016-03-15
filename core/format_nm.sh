#!/bin/bash 
for i in /tmp/*nm_reco*; do mv "$i" "$(echo $i | tr "'" " ")"; done
