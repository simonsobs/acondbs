#!/bin/bash

##__________________________________________________________________||
if [ -z $ACONDBS_SECRET_KEY ]
then
    if [ -z $ACONDBS_SECRET_KEY_FILE ]
    then
        echo 'Warning: neither $ACONDBS_SECRET_KEY or $ACONDBS_SECRET_KEY_FILE is set!'
    else
        if [ -f $ACONDBS_SECRET_KEY_FILE ]
        then
            export ACONDBS_SECRET_KEY=$(cat $ACONDBS_SECRET_KEY_FILE | tr -d '\n')
        else
            echo "Warning: $ACONDBS_SECRET_KEY_FILE doesn't exist!"
        fi
    fi
fi

if [ -z $ACONDBS_SECRET_KEY ]
then
    echo 'Warning: $ACONDBS_SECRET_KEY is not set!'
fi

##__________________________________________________________________||
if [ -z $GITHUB_AUTH_CLIENT_SECRET ]
then
    if [ -z $GITHUB_AUTH_CLIENT_SECRET_FILE ]
    then
        echo 'Warning: neither $GITHUB_AUTH_CLIENT_SECRET or $GITHUB_AUTH_CLIENT_SECRET_FILE is set!'
    else
        if [ -f $GITHUB_AUTH_CLIENT_SECRET_FILE ]
        then
            export GITHUB_AUTH_CLIENT_SECRET=$(cat $GITHUB_AUTH_CLIENT_SECRET_FILE | tr -d '\n')
        else
            echo "Warning: $GITHUB_AUTH_CLIENT_SECRET_FILE doesn't exist!"
        fi
    fi
fi

if [ -z $GITHUB_AUTH_CLIENT_SECRET ]
then
    echo 'Warning: $GITHUB_AUTH_CLIENT_SECRET is not set!'
fi

##__________________________________________________________________||
command="flask db upgrade"
echo + $command;
eval $command;

command="flask db history"
echo + $command;
eval $command;

command="flask db current"
echo + $command;
eval $command;

##__________________________________________________________________||
# command="flask run -h 0.0.0.0 -p 5000"
command="gunicorn -w 4 -b 0.0.0.0:5000 \"$FLASK_APP\" --log-level debug"
echo + $command;
eval $command;

##__________________________________________________________________||
