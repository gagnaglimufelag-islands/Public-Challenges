# Lost keys

The first step is to mount the images, if using windows you can use tools such as FTK imager for this task. Then it can be seen that there are two volumes in this image. One is open and contains about 100.000 files and the other one that is bitlocker encrypted. According to the description, the decryption key is located somewhere in these files.

Since this is a bitlocker encryption key, it is 48 characters in length and is formatted in 8 blocks of 6 numbers separated with dashes. We can grep all the files recursively to find the key using regex.

This allows us to decrypt the other drive. Once decrypted it appears that there is only a single image on the drive. A closer inspection of the drive with e.g. Autopsy reveals that the key is simply located in the recycle bin on the drive.