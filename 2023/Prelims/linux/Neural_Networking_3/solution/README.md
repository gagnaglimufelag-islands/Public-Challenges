## Neural Network 3
We quickly find a directory named `flag3`. This directory is filled with a number of random directories and files.
Each file contains a string that looks like a flag but isn't??? However if we grep for the flag format by using 
the following grep command: `grep -r gg{` within the `flag3` directory we only get one file.

```bash
grep -r gg{
rmmxF7LnulcPoX1AEtkk/SeiTUtjGK9:gg{I_H4X0R3D_TH3_31G3n_M4TR1X_AND_4LL_1_G0T_W45_TH15_L0U5Y_5TR1NG}
```

Now why is this? If we `cat` the file we found and some other file with the `-A` we will quickly see the differece

```bash
cat -A rmmxF7LnulcPoX1AEtkk/SeiTUtjGK9 4BbIR81abg
gg{I_H4X0R3D_TH3_31G3n_M4TR1X_AND_4LL_1_G0T_W45_TH15_L0U5Y_5TR1NG}$
gM-bM-^@M-^NM-bM-^@M-^Ng{I_H4X0R3D_TH3_MlUFx_M4TR1X_AND_4LL_1_G0T_W45_TH15_L0U5Y_5TR1NG}$
```

There are a number of zero width whitespaces between the g's in the flag in all files except for one.
