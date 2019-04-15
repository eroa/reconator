#!/bin/bash 
for i in /tmp/nm_reco_*; do mv "$i" "$(echo $i | tr "\n" " ")" ; done
