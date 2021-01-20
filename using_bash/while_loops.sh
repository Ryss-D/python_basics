n=1
while [ $n -le 5 ]; do
    echo "Iterarion number $n"
    ((n+=1))
done

n=0
command=$1 #it means take the first arguments passed
while ! $command && [ $n -le 5 ]; do
    sleep $n
    ((n=n+1))
    echo "Retry #$n"
done;