#we can use loops just llisting elements
for fruit in peach oreange apple; do
    echo "I like $fruit"
done

basename index.htm .htm    #take a file and extension and return the name without extension

for file in *.htm; do
    name=$(basename "$file" .HTM)
    mv "$file" "$name.html"
    #echo mv "$file" "$name.html" it will print the rename instead of rename the file
done