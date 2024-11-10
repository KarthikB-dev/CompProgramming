file="file.txt"
count=1

while read -r line; do
    if [ "$count" -eq "10" ]; then 
        echo -e "$line"
    fi
    count=$(($count + 1))
done <$file 