flag=$1
for (( i=0; i<${#flag}; i++ )); do
    char="${flag:$i:1}"
    name=`printf "%03d" $i` 
    qrencode -o char_$name.png $char
done

ffmpeg -f image2 -i char_%003d.png $2
rm *.png
