# WAT

We have a PDF with two embedded fonts, OpenSans

```
<</Type /Font
/Subtype /Type0
/BaseFont /MPDFAA+OpenSans-Regular
```

and FlagFont

```
<</Type /Font
/Subtype /Type0
/BaseFont /MPDFAA+FlagFont-Regular
```

The first line is the PDF is rendered with OpenSans (`F2`) but the next two are rendered with FlagFont (`F1`).

```
<</Length 1227>>
stream
2 J
0.57 w
BT /F2 16.00 Tf ET
BT 31.19 794.57 Td ([SOME BYTES]) Tj ET
BT /F1 16.00 Tf ET
BT 31.19 766.22 Td ([SOME BYTES]) Tj ET
BT /F1 1.00 Tf ET
...
```

Changing the first line to flag font, reveals the flag


```
<</Length 1227>>
stream
2 J
0.57 w
BT /F1 16.00 Tf ET
BT 31.19 794.57 Td ([SOME BYTES]) Tj ET
BT /F1 16.00 Tf ET
BT 31.19 766.22 Td ([SOME BYTES]) Tj ET
BT /F1 1.00 Tf ET
...
```

Or in a bash command,

```
sed -i 's/F2/F1/' wat.pdf
```
