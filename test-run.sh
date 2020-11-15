python app.py & PID=$!
sleep 1m
kill -HUP $PID
