#!/bin/bash


for run in {1..10}
do
        # Echo current date to stdout
        echo "printing Present Time -" `date`
        # Echo 'error!' to stderr
        echo 'error!' >&2
        sleep 2
done

bash -c "sleep 1 && exit 0"
bash -c "sleep 5 && exit 0"
bash -c "sleep 1 && exit 1"
sh -c "sleep 10 && exit 1"
bash -c "if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1"
bash -c "if [ -f lock ]; then exit 1; fi; sleep 10 && touch lock && exit 1"

