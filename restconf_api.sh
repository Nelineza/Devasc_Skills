#!/bin/bash
if resp_put_code in range(200,300)
    echo "STATUS OK: $resp_put.status_code"
else
    echo "ERROR"
    echo $resp_put.status_code
    echo $resp_put.text
fi