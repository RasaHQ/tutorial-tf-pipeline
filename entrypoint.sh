#!/bin/bash

set -e

function print_help {
    echo "Available options:"
    echo " help                       - Print this help"
    echo " train-nlu                  - Train a dialogue model"
    echo " train-agent                - Train a dialogue model"
    echo " run                        - Run agent"
}

case ${1} in
    train-nlu)
        exec python -m rasa_nlu.train -c config.yml -d data/nlu_data.md -o models/current/nlu_model
        ;;
    train-agent)
        exec python -m rasa_core.train -d ./domain.yml -s data/stories.md -o models/current/dialogue
        ;;        
    run)
        exec python -m rasa_core.run -d models/current/dialogue -u models/current/nlu_model
        ;;        
    *)
        print_help
        ;;
esac

