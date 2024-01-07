#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdbool.h>


#define FLAG_SIZE 64

bool win1 = false;
bool win2 = false;
bool win3 = false;
bool win4 = false;
bool win5 = false;
bool win6 = false;
bool win7 = false;
bool win8 = false;
bool win9 = false;
bool win10 = false;
bool win11 = false;
bool win12 = false;
bool win13 = false;
bool win14 = false;
bool win15 = false;
bool win16 = false;
bool win17 = false;
bool win18 = false;
bool win19 = false;
bool win20 = false;
bool win21 = false;
bool win22 = false;
bool win23 = false;
bool win24 = false;
bool win25 = false;
bool win26 = false;
bool win27 = false;
bool win28 = false;
bool win29 = false;
bool win30 = false;
bool win31 = false;
bool win32 = false;
bool win33 = false;
bool win34 = false;
bool win35 = false;
bool win36 = false;
bool win37 = false;
bool win38 = false;
bool win39 = false;
bool win40 = false;
bool win41 = false;
bool win42 = false;
bool win43 = false;
bool win44 = false;
bool win45 = false;
bool win46 = false;
bool win47 = false;
bool win48 = false;
bool win49 = false;
bool win50 = false;
bool win51 = false;
bool win52 = false;
bool win53 = false;
bool win54 = false;
bool win55 = false;
bool win56 = false;
bool win57 = false;
bool win58 = false;
bool win59 = false;
bool win60 = false;
bool win61 = false;
bool win62 = false;
bool win63 = false;
bool win64 = false;
bool win65 = false;
bool win66 = false;
bool win67 = false;
bool win68 = false;
bool win69 = false;
bool win70 = false;
bool win71 = false;
bool win72 = false;
bool win73 = false;
bool win74 = false;
bool win75 = false;
bool win76 = false;
bool win77 = false;
bool win78 = false;
bool win79 = false;
bool win80 = false;
bool win81 = false;
bool win82 = false;
bool win83 = false;
bool win84 = false;
bool win85 = false;
bool win86 = false;
bool win87 = false;
bool win88 = false;
bool win89 = false;
bool win90 = false;
bool win91 = false;
bool win92 = false;
bool win93 = false;
bool win94 = false;
bool win95 = false;
bool win96 = false;
bool win97 = false;
bool win98 = false;
bool win99 = false;
bool win100 = false;
bool win101 = false;
bool win102 = false;
bool win103 = false;
bool win104 = false;
bool win105 = false;
bool win106 = false;
bool win107 = false;
bool win108 = false;
bool win109 = false;
bool win110 = false;
bool win111 = false;
bool win112 = false;
bool win113 = false;
bool win114 = false;
bool win115 = false;
bool win116 = false;
bool win117 = false;
bool win118 = false;
bool win119 = false;
bool win120 = false;
bool win121 = false;
bool win122 = false;
bool win123 = false;
bool win124 = false;
bool win125 = false;
bool win126 = false;
bool win127 = false;
bool win128 = false;
bool win129 = false;
bool win130 = false;
bool win131 = false;
bool win132 = false;
bool win133 = false;
bool win134 = false;
bool win135 = false;
bool win136 = false;
bool win137 = false;
bool win138 = false;
bool win139 = false;
bool win140 = false;
bool win141 = false;
bool win142 = false;
bool win143 = false;
bool win144 = false;
bool win145 = false;
bool win146 = false;
bool win147 = false;
bool win148 = false;
bool win149 = false;
bool win150 = false;
bool win151 = false;
bool win152 = false;
bool win153 = false;
bool win154 = false;
bool win155 = false;
bool win156 = false;
bool win157 = false;
bool win158 = false;
bool win159 = false;
bool win160 = false;
bool win161 = false;
bool win162 = false;
bool win163 = false;
bool win164 = false;
bool win165 = false;
bool win166 = false;
bool win167 = false;
bool win168 = false;
bool win169 = false;
bool win170 = false;
bool win171 = false;
bool win172 = false;
bool win173 = false;
bool win174 = false;
bool win175 = false;
bool win176 = false;
bool win177 = false;
bool win178 = false;
bool win179 = false;
bool win180 = false;
bool win181 = false;
bool win182 = false;
bool win183 = false;
bool win184 = false;
bool win185 = false;
bool win186 = false;
bool win187 = false;
bool win188 = false;
bool win189 = false;
bool win190 = false;
bool win191 = false;
bool win192 = false;
bool win193 = false;
bool win194 = false;
bool win195 = false;
bool win196 = false;
bool win197 = false;
bool win198 = false;
bool win199 = false;
bool win200 = false;
bool win201 = false;
bool win202 = false;
bool win203 = false;
bool win204 = false;
bool win205 = false;
bool win206 = false;
bool win207 = false;
bool win208 = false;
bool win209 = false;
bool win210 = false;
bool win211 = false;
bool win212 = false;
bool win213 = false;
bool win214 = false;
bool win215 = false;
bool win216 = false;
bool win217 = false;
bool win218 = false;
bool win219 = false;
bool win220 = false;
bool win221 = false;
bool win222 = false;
bool win223 = false;
bool win224 = false;
bool win225 = false;
bool win226 = false;
bool win227 = false;
bool win228 = false;
bool win229 = false;
bool win230 = false;
bool win231 = false;
bool win232 = false;
bool win233 = false;
bool win234 = false;
bool win235 = false;
bool win236 = false;
bool win237 = false;
bool win238 = false;
bool win239 = false;
bool win240 = false;
bool win241 = false;
bool win242 = false;
bool win243 = false;
bool win244 = false;
bool win245 = false;
bool win246 = false;
bool win247 = false;
bool win248 = false;
bool win249 = false;
bool win250 = false;
bool win251 = false;
bool win252 = false;
bool win253 = false;
bool win254 = false;
bool win255 = false;
bool win256 = false;
bool win257 = false;
bool win258 = false;
bool win259 = false;
bool win260 = false;
bool win261 = false;
bool win262 = false;
bool win263 = false;
bool win264 = false;
bool win265 = false;
bool win266 = false;
bool win267 = false;
bool win268 = false;
bool win269 = false;
bool win270 = false;
bool win271 = false;
bool win272 = false;
bool win273 = false;
bool win274 = false;
bool win275 = false;
bool win276 = false;
bool win277 = false;
bool win278 = false;
bool win279 = false;
bool win280 = false;
bool win281 = false;
bool win282 = false;
bool win283 = false;
bool win284 = false;
bool win285 = false;
bool win286 = false;
bool win287 = false;
bool win288 = false;
bool win289 = false;
bool win290 = false;
bool win291 = false;
bool win292 = false;
bool win293 = false;
bool win294 = false;
bool win295 = false;
bool win296 = false;
bool win297 = false;
bool win298 = false;
bool win299 = false;
bool win300 = false;
bool win301 = false;
bool win302 = false;
bool win303 = false;
bool win304 = false;
bool win305 = false;
bool win306 = false;
bool win307 = false;
bool win308 = false;
bool win309 = false;
bool win310 = false;
bool win311 = false;
bool win312 = false;
bool win313 = false;
bool win314 = false;
bool win315 = false;
bool win316 = false;
bool win317 = false;
bool win318 = false;
bool win319 = false;
bool win320 = false;
bool win321 = false;
bool win322 = false;
bool win323 = false;
bool win324 = false;
bool win325 = false;
bool win326 = false;
bool win327 = false;
bool win328 = false;
bool win329 = false;
bool win330 = false;
bool win331 = false;
bool win332 = false;
bool win333 = false;
bool win334 = false;
bool win335 = false;
bool win336 = false;
bool win337 = false;
bool win338 = false;
bool win339 = false;
bool win340 = false;
bool win341 = false;
bool win342 = false;
bool win343 = false;
bool win344 = false;
bool win345 = false;
bool win346 = false;
bool win347 = false;
bool win348 = false;
bool win349 = false;
bool win350 = false;
bool win351 = false;
bool win352 = false;
bool win353 = false;
bool win354 = false;
bool win355 = false;
bool win356 = false;
bool win357 = false;
bool win358 = false;
bool win359 = false;
bool win360 = false;
bool win361 = false;
bool win362 = false;
bool win363 = false;
bool win364 = false;
bool win365 = false;
bool win366 = false;
bool win367 = false;
bool win368 = false;
bool win369 = false;
bool win370 = false;
bool win371 = false;
bool win372 = false;
bool win373 = false;
bool win374 = false;
bool win375 = false;
bool win376 = false;
bool win377 = false;
bool win378 = false;
bool win379 = false;
bool win380 = false;
bool win381 = false;
bool win382 = false;
bool win383 = false;
bool win384 = false;
bool win385 = false;
bool win386 = false;
bool win387 = false;
bool win388 = false;
bool win389 = false;
bool win390 = false;
bool win391 = false;
bool win392 = false;
bool win393 = false;
bool win394 = false;
bool win395 = false;
bool win396 = false;
bool win397 = false;
bool win398 = false;
bool win399 = false;
bool win400 = false;
bool win401 = false;
bool win402 = false;
bool win403 = false;
bool win404 = false;
bool win405 = false;
bool win406 = false;
bool win407 = false;
bool win408 = false;
bool win409 = false;
bool win410 = false;
bool win411 = false;
bool win412 = false;
bool win413 = false;
bool win414 = false;
bool win415 = false;
bool win416 = false;
bool win417 = false;
bool win418 = false;
bool win419 = false;
bool win420 = false;
bool win421 = false;
bool win422 = false;
bool win423 = false;
bool win424 = false;
bool win425 = false;
bool win426 = false;
bool win427 = false;
bool win428 = false;
bool win429 = false;
bool win430 = false;
bool win431 = false;
bool win432 = false;
bool win433 = false;
bool win434 = false;
bool win435 = false;
bool win436 = false;
bool win437 = false;
bool win438 = false;
bool win439 = false;
bool win440 = false;
bool win441 = false;
bool win442 = false;
bool win443 = false;
bool win444 = false;
bool win445 = false;
bool win446 = false;
bool win447 = false;
bool win448 = false;
bool win449 = false;
bool win450 = false;
bool win451 = false;
bool win452 = false;
bool win453 = false;
bool win454 = false;
bool win455 = false;
bool win456 = false;
bool win457 = false;
bool win458 = false;
bool win459 = false;
bool win460 = false;
bool win461 = false;
bool win462 = false;
bool win463 = false;
bool win464 = false;
bool win465 = false;
bool win466 = false;
bool win467 = false;
bool win468 = false;
bool win469 = false;
bool win470 = false;
bool win471 = false;
bool win472 = false;
bool win473 = false;
bool win474 = false;
bool win475 = false;
bool win476 = false;
bool win477 = false;
bool win478 = false;
bool win479 = false;
bool win480 = false;
bool win481 = false;
bool win482 = false;
bool win483 = false;
bool win484 = false;
bool win485 = false;
bool win486 = false;
bool win487 = false;
bool win488 = false;
bool win489 = false;
bool win490 = false;
bool win491 = false;
bool win492 = false;
bool win493 = false;
bool win494 = false;
bool win495 = false;
bool win496 = false;
bool win497 = false;
bool win498 = false;
bool win499 = false;
bool win500 = false;
bool win501 = false;
bool win502 = false;
bool win503 = false;
bool win504 = false;
bool win505 = false;
bool win506 = false;
bool win507 = false;
bool win508 = false;
bool win509 = false;
bool win510 = false;
bool win511 = false;
bool win512 = false;
bool win513 = false;
bool win514 = false;
bool win515 = false;
bool win516 = false;
bool win517 = false;
bool win518 = false;
bool win519 = false;
bool win520 = false;
bool win521 = false;
bool win522 = false;
bool win523 = false;
bool win524 = false;
bool win525 = false;
bool win526 = false;
bool win527 = false;
bool win528 = false;
bool win529 = false;
bool win530 = false;
bool win531 = false;
bool win532 = false;
bool win533 = false;
bool win534 = false;
bool win535 = false;
bool win536 = false;
bool win537 = false;
bool win538 = false;
bool win539 = false;
bool win540 = false;
bool win541 = false;
bool win542 = false;
bool win543 = false;
bool win544 = false;
bool win545 = false;
bool win546 = false;
bool win547 = false;
bool win548 = false;
bool win549 = false;
bool win550 = false;
bool win551 = false;
bool win552 = false;
bool win553 = false;
bool win554 = false;
bool win555 = false;
bool win556 = false;
bool win557 = false;
bool win558 = false;
bool win559 = false;
bool win560 = false;
bool win561 = false;
bool win562 = false;
bool win563 = false;
bool win564 = false;
bool win565 = false;
bool win566 = false;
bool win567 = false;
bool win568 = false;
bool win569 = false;
bool win570 = false;
bool win571 = false;
bool win572 = false;
bool win573 = false;
bool win574 = false;
bool win575 = false;
bool win576 = false;
bool win577 = false;
bool win578 = false;
bool win579 = false;
bool win580 = false;
bool win581 = false;
bool win582 = false;
bool win583 = false;
bool win584 = false;
bool win585 = false;
bool win586 = false;
bool win587 = false;
bool win588 = false;
bool win589 = false;
bool win590 = false;
bool win591 = false;
bool win592 = false;
bool win593 = false;
bool win594 = false;
bool win595 = false;
bool win596 = false;
bool win597 = false;
bool win598 = false;
bool win599 = false;
bool win600 = false;
bool win601 = false;
bool win602 = false;
bool win603 = false;
bool win604 = false;
bool win605 = false;
bool win606 = false;
bool win607 = false;
bool win608 = false;
bool win609 = false;
bool win610 = false;
bool win611 = false;
bool win612 = false;
bool win613 = false;
bool win614 = false;
bool win615 = false;
bool win616 = false;
bool win617 = false;
bool win618 = false;
bool win619 = false;
bool win620 = false;
bool win621 = false;
bool win622 = false;
bool win623 = false;
bool win624 = false;
bool win625 = false;
bool win626 = false;
bool win627 = false;
bool win628 = false;
bool win629 = false;
bool win630 = false;
bool win631 = false;
bool win632 = false;
bool win633 = false;
bool win634 = false;
bool win635 = false;
bool win636 = false;
bool win637 = false;
bool win638 = false;
bool win639 = false;
bool win640 = false;
bool win641 = false;
bool win642 = false;
bool win643 = false;
bool win644 = false;
bool win645 = false;
bool win646 = false;
bool win647 = false;
bool win648 = false;
bool win649 = false;
bool win650 = false;
bool win651 = false;
bool win652 = false;
bool win653 = false;
bool win654 = false;
bool win655 = false;
bool win656 = false;
bool win657 = false;
bool win658 = false;
bool win659 = false;
bool win660 = false;
bool win661 = false;
bool win662 = false;
bool win663 = false;
bool win664 = false;
bool win665 = false;
bool win666 = false;
bool win667 = false;
bool win668 = false;
bool win669 = false;
bool win670 = false;
bool win671 = false;
bool win672 = false;
bool win673 = false;
bool win674 = false;
bool win675 = false;
bool win676 = false;
bool win677 = false;
bool win678 = false;
bool win679 = false;
bool win680 = false;
bool win681 = false;
bool win682 = false;
bool win683 = false;
bool win684 = false;
bool win685 = false;
bool win686 = false;
bool win687 = false;
bool win688 = false;
bool win689 = false;
bool win690 = false;
bool win691 = false;
bool win692 = false;
bool win693 = false;
bool win694 = false;
bool win695 = false;
bool win696 = false;
bool win697 = false;
bool win698 = false;
bool win699 = false;
bool win700 = false;
bool win701 = false;
bool win702 = false;
bool win703 = false;
bool win704 = false;
bool win705 = false;
bool win706 = false;
bool win707 = false;
bool win708 = false;
bool win709 = false;
bool win710 = false;
bool win711 = false;
bool win712 = false;
bool win713 = false;
bool win714 = false;
bool win715 = false;
bool win716 = false;
bool win717 = false;
bool win718 = false;
bool win719 = false;
bool win720 = false;
bool win721 = false;
bool win722 = false;
bool win723 = false;
bool win724 = false;
bool win725 = false;
bool win726 = false;
bool win727 = false;
bool win728 = false;
bool win729 = false;
bool win730 = false;
bool win731 = false;
bool win732 = false;
bool win733 = false;
bool win734 = false;
bool win735 = false;
bool win736 = false;
bool win737 = false;
bool win738 = false;
bool win739 = false;
bool win740 = false;
bool win741 = false;
bool win742 = false;
bool win743 = false;
bool win744 = false;
bool win745 = false;
bool win746 = false;
bool win747 = false;
bool win748 = false;
bool win749 = false;
bool win750 = false;
bool win751 = false;
bool win752 = false;
bool win753 = false;
bool win754 = false;
bool win755 = false;
bool win756 = false;
bool win757 = false;
bool win758 = false;
bool win759 = false;
bool win760 = false;
bool win761 = false;
bool win762 = false;
bool win763 = false;
bool win764 = false;
bool win765 = false;
bool win766 = false;
bool win767 = false;
bool win768 = false;
bool win769 = false;
bool win770 = false;
bool win771 = false;
bool win772 = false;
bool win773 = false;
bool win774 = false;
bool win775 = false;
bool win776 = false;
bool win777 = false;
bool win778 = false;
bool win779 = false;
bool win780 = false;
bool win781 = false;
bool win782 = false;
bool win783 = false;
bool win784 = false;
bool win785 = false;
bool win786 = false;
bool win787 = false;
bool win788 = false;
bool win789 = false;
bool win790 = false;
bool win791 = false;
bool win792 = false;
bool win793 = false;
bool win794 = false;
bool win795 = false;
bool win796 = false;
bool win797 = false;
bool win798 = false;
bool win799 = false;
bool win800 = false;
bool win801 = false;
bool win802 = false;
bool win803 = false;
bool win804 = false;
bool win805 = false;
bool win806 = false;
bool win807 = false;
bool win808 = false;
bool win809 = false;
bool win810 = false;
bool win811 = false;
bool win812 = false;
bool win813 = false;
bool win814 = false;
bool win815 = false;
bool win816 = false;
bool win817 = false;
bool win818 = false;
bool win819 = false;
bool win820 = false;
bool win821 = false;
bool win822 = false;
bool win823 = false;
bool win824 = false;
bool win825 = false;
bool win826 = false;
bool win827 = false;
bool win828 = false;
bool win829 = false;
bool win830 = false;
bool win831 = false;
bool win832 = false;
bool win833 = false;
bool win834 = false;
bool win835 = false;
bool win836 = false;
bool win837 = false;
bool win838 = false;
bool win839 = false;
bool win840 = false;
bool win841 = false;
bool win842 = false;
bool win843 = false;
bool win844 = false;
bool win845 = false;
bool win846 = false;
bool win847 = false;
bool win848 = false;
bool win849 = false;
bool win850 = false;
bool win851 = false;
bool win852 = false;
bool win853 = false;
bool win854 = false;
bool win855 = false;
bool win856 = false;
bool win857 = false;
bool win858 = false;
bool win859 = false;
bool win860 = false;
bool win861 = false;
bool win862 = false;
bool win863 = false;
bool win864 = false;
bool win865 = false;
bool win866 = false;
bool win867 = false;
bool win868 = false;
bool win869 = false;
bool win870 = false;
bool win871 = false;
bool win872 = false;
bool win873 = false;
bool win874 = false;
bool win875 = false;
bool win876 = false;
bool win877 = false;
bool win878 = false;
bool win879 = false;
bool win880 = false;
bool win881 = false;
bool win882 = false;
bool win883 = false;
bool win884 = false;
bool win885 = false;
bool win886 = false;
bool win887 = false;
bool win888 = false;
bool win889 = false;
bool win890 = false;
bool win891 = false;
bool win892 = false;
bool win893 = false;
bool win894 = false;
bool win895 = false;
bool win896 = false;
bool win897 = false;
bool win898 = false;
bool win899 = false;
bool win900 = false;
bool win901 = false;
bool win902 = false;
bool win903 = false;
bool win904 = false;
bool win905 = false;
bool win906 = false;
bool win907 = false;
bool win908 = false;
bool win909 = false;
bool win910 = false;
bool win911 = false;
bool win912 = false;
bool win913 = false;
bool win914 = false;
bool win915 = false;
bool win916 = false;
bool win917 = false;
bool win918 = false;
bool win919 = false;
bool win920 = false;
bool win921 = false;
bool win922 = false;
bool win923 = false;
bool win924 = false;
bool win925 = false;
bool win926 = false;
bool win927 = false;
bool win928 = false;
bool win929 = false;
bool win930 = false;
bool win931 = false;
bool win932 = false;
bool win933 = false;
bool win934 = false;
bool win935 = false;
bool win936 = false;
bool win937 = false;
bool win938 = false;
bool win939 = false;
bool win940 = false;
bool win941 = false;
bool win942 = false;
bool win943 = false;
bool win944 = false;
bool win945 = false;
bool win946 = false;
bool win947 = false;
bool win948 = false;
bool win949 = false;
bool win950 = false;
bool win951 = false;
bool win952 = false;
bool win953 = false;
bool win954 = false;
bool win955 = false;
bool win956 = false;
bool win957 = false;
bool win958 = false;
bool win959 = false;
bool win960 = false;
bool win961 = false;
bool win962 = false;
bool win963 = false;
bool win964 = false;
bool win965 = false;
bool win966 = false;
bool win967 = false;
bool win968 = false;
bool win969 = false;
bool win970 = false;
bool win971 = false;
bool win972 = false;
bool win973 = false;
bool win974 = false;
bool win975 = false;
bool win976 = false;
bool win977 = false;
bool win978 = false;
bool win979 = false;
bool win980 = false;
bool win981 = false;
bool win982 = false;
bool win983 = false;
bool win984 = false;
bool win985 = false;
bool win986 = false;
bool win987 = false;
bool win988 = false;
bool win989 = false;
bool win990 = false;
bool win991 = false;
bool win992 = false;
bool win993 = false;
bool win994 = false;
bool win995 = false;
bool win996 = false;
bool win997 = false;
bool win998 = false;
bool win999 = false;
bool win1000 = false;

void leap1() {
    win1 = true;
}

void leap2() {
    if (win1) {
        win2 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap3() {
    if (win2) {
        win3 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap4() {
    if (win3) {
        win4 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap5() {
    if (win4) {
        win5 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap6() {
    if (win5) {
        win6 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap7() {
    if (win6) {
        win7 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap8() {
    if (win7) {
        win8 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap9() {
    if (win8) {
        win9 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap10() {
    if (win9) {
        win10 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap11() {
    if (win10) {
        win11 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap12() {
    if (win11) {
        win12 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap13() {
    if (win12) {
        win13 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap14() {
    if (win13) {
        win14 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap15() {
    if (win14) {
        win15 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap16() {
    if (win15) {
        win16 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap17() {
    if (win16) {
        win17 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap18() {
    if (win17) {
        win18 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap19() {
    if (win18) {
        win19 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap20() {
    if (win19) {
        win20 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap21() {
    if (win20) {
        win21 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap22() {
    if (win21) {
        win22 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap23() {
    if (win22) {
        win23 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap24() {
    if (win23) {
        win24 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap25() {
    if (win24) {
        win25 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap26() {
    if (win25) {
        win26 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap27() {
    if (win26) {
        win27 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap28() {
    if (win27) {
        win28 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap29() {
    if (win28) {
        win29 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap30() {
    if (win29) {
        win30 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap31() {
    if (win30) {
        win31 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap32() {
    if (win31) {
        win32 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap33() {
    if (win32) {
        win33 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap34() {
    if (win33) {
        win34 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap35() {
    if (win34) {
        win35 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap36() {
    if (win35) {
        win36 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap37() {
    if (win36) {
        win37 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap38() {
    if (win37) {
        win38 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap39() {
    if (win38) {
        win39 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap40() {
    if (win39) {
        win40 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap41() {
    if (win40) {
        win41 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap42() {
    if (win41) {
        win42 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap43() {
    if (win42) {
        win43 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap44() {
    if (win43) {
        win44 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap45() {
    if (win44) {
        win45 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap46() {
    if (win45) {
        win46 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap47() {
    if (win46) {
        win47 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap48() {
    if (win47) {
        win48 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap49() {
    if (win48) {
        win49 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap50() {
    if (win49) {
        win50 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap51() {
    if (win50) {
        win51 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap52() {
    if (win51) {
        win52 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap53() {
    if (win52) {
        win53 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap54() {
    if (win53) {
        win54 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap55() {
    if (win54) {
        win55 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap56() {
    if (win55) {
        win56 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap57() {
    if (win56) {
        win57 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap58() {
    if (win57) {
        win58 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap59() {
    if (win58) {
        win59 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap60() {
    if (win59) {
        win60 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap61() {
    if (win60) {
        win61 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap62() {
    if (win61) {
        win62 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap63() {
    if (win62) {
        win63 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap64() {
    if (win63) {
        win64 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap65() {
    if (win64) {
        win65 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap66() {
    if (win65) {
        win66 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap67() {
    if (win66) {
        win67 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap68() {
    if (win67) {
        win68 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap69() {
    if (win68) {
        win69 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap70() {
    if (win69) {
        win70 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap71() {
    if (win70) {
        win71 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap72() {
    if (win71) {
        win72 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap73() {
    if (win72) {
        win73 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap74() {
    if (win73) {
        win74 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap75() {
    if (win74) {
        win75 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap76() {
    if (win75) {
        win76 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap77() {
    if (win76) {
        win77 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap78() {
    if (win77) {
        win78 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap79() {
    if (win78) {
        win79 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap80() {
    if (win79) {
        win80 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap81() {
    if (win80) {
        win81 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap82() {
    if (win81) {
        win82 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap83() {
    if (win82) {
        win83 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap84() {
    if (win83) {
        win84 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap85() {
    if (win84) {
        win85 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap86() {
    if (win85) {
        win86 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap87() {
    if (win86) {
        win87 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap88() {
    if (win87) {
        win88 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap89() {
    if (win88) {
        win89 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap90() {
    if (win89) {
        win90 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap91() {
    if (win90) {
        win91 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap92() {
    if (win91) {
        win92 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap93() {
    if (win92) {
        win93 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap94() {
    if (win93) {
        win94 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap95() {
    if (win94) {
        win95 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap96() {
    if (win95) {
        win96 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap97() {
    if (win96) {
        win97 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap98() {
    if (win97) {
        win98 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap99() {
    if (win98) {
        win99 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap100() {
    if (win99) {
        win100 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap101() {
    if (win100) {
        win101 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap102() {
    if (win101) {
        win102 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap103() {
    if (win102) {
        win103 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap104() {
    if (win103) {
        win104 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap105() {
    if (win104) {
        win105 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap106() {
    if (win105) {
        win106 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap107() {
    if (win106) {
        win107 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap108() {
    if (win107) {
        win108 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap109() {
    if (win108) {
        win109 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap110() {
    if (win109) {
        win110 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap111() {
    if (win110) {
        win111 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap112() {
    if (win111) {
        win112 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap113() {
    if (win112) {
        win113 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap114() {
    if (win113) {
        win114 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap115() {
    if (win114) {
        win115 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap116() {
    if (win115) {
        win116 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap117() {
    if (win116) {
        win117 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap118() {
    if (win117) {
        win118 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap119() {
    if (win118) {
        win119 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap120() {
    if (win119) {
        win120 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap121() {
    if (win120) {
        win121 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap122() {
    if (win121) {
        win122 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap123() {
    if (win122) {
        win123 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap124() {
    if (win123) {
        win124 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap125() {
    if (win124) {
        win125 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap126() {
    if (win125) {
        win126 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap127() {
    if (win126) {
        win127 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap128() {
    if (win127) {
        win128 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap129() {
    if (win128) {
        win129 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap130() {
    if (win129) {
        win130 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap131() {
    if (win130) {
        win131 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap132() {
    if (win131) {
        win132 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap133() {
    if (win132) {
        win133 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap134() {
    if (win133) {
        win134 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap135() {
    if (win134) {
        win135 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap136() {
    if (win135) {
        win136 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap137() {
    if (win136) {
        win137 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap138() {
    if (win137) {
        win138 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap139() {
    if (win138) {
        win139 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap140() {
    if (win139) {
        win140 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap141() {
    if (win140) {
        win141 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap142() {
    if (win141) {
        win142 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap143() {
    if (win142) {
        win143 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap144() {
    if (win143) {
        win144 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap145() {
    if (win144) {
        win145 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap146() {
    if (win145) {
        win146 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap147() {
    if (win146) {
        win147 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap148() {
    if (win147) {
        win148 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap149() {
    if (win148) {
        win149 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap150() {
    if (win149) {
        win150 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap151() {
    if (win150) {
        win151 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap152() {
    if (win151) {
        win152 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap153() {
    if (win152) {
        win153 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap154() {
    if (win153) {
        win154 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap155() {
    if (win154) {
        win155 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap156() {
    if (win155) {
        win156 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap157() {
    if (win156) {
        win157 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap158() {
    if (win157) {
        win158 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap159() {
    if (win158) {
        win159 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap160() {
    if (win159) {
        win160 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap161() {
    if (win160) {
        win161 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap162() {
    if (win161) {
        win162 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap163() {
    if (win162) {
        win163 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap164() {
    if (win163) {
        win164 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap165() {
    if (win164) {
        win165 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap166() {
    if (win165) {
        win166 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap167() {
    if (win166) {
        win167 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap168() {
    if (win167) {
        win168 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap169() {
    if (win168) {
        win169 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap170() {
    if (win169) {
        win170 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap171() {
    if (win170) {
        win171 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap172() {
    if (win171) {
        win172 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap173() {
    if (win172) {
        win173 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap174() {
    if (win173) {
        win174 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap175() {
    if (win174) {
        win175 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap176() {
    if (win175) {
        win176 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap177() {
    if (win176) {
        win177 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap178() {
    if (win177) {
        win178 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap179() {
    if (win178) {
        win179 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap180() {
    if (win179) {
        win180 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap181() {
    if (win180) {
        win181 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap182() {
    if (win181) {
        win182 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap183() {
    if (win182) {
        win183 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap184() {
    if (win183) {
        win184 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap185() {
    if (win184) {
        win185 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap186() {
    if (win185) {
        win186 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap187() {
    if (win186) {
        win187 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap188() {
    if (win187) {
        win188 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap189() {
    if (win188) {
        win189 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap190() {
    if (win189) {
        win190 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap191() {
    if (win190) {
        win191 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap192() {
    if (win191) {
        win192 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap193() {
    if (win192) {
        win193 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap194() {
    if (win193) {
        win194 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap195() {
    if (win194) {
        win195 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap196() {
    if (win195) {
        win196 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap197() {
    if (win196) {
        win197 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap198() {
    if (win197) {
        win198 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap199() {
    if (win198) {
        win199 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap200() {
    if (win199) {
        win200 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap201() {
    if (win200) {
        win201 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap202() {
    if (win201) {
        win202 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap203() {
    if (win202) {
        win203 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap204() {
    if (win203) {
        win204 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap205() {
    if (win204) {
        win205 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap206() {
    if (win205) {
        win206 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap207() {
    if (win206) {
        win207 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap208() {
    if (win207) {
        win208 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap209() {
    if (win208) {
        win209 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap210() {
    if (win209) {
        win210 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap211() {
    if (win210) {
        win211 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap212() {
    if (win211) {
        win212 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap213() {
    if (win212) {
        win213 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap214() {
    if (win213) {
        win214 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap215() {
    if (win214) {
        win215 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap216() {
    if (win215) {
        win216 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap217() {
    if (win216) {
        win217 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap218() {
    if (win217) {
        win218 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap219() {
    if (win218) {
        win219 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap220() {
    if (win219) {
        win220 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap221() {
    if (win220) {
        win221 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap222() {
    if (win221) {
        win222 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap223() {
    if (win222) {
        win223 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap224() {
    if (win223) {
        win224 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap225() {
    if (win224) {
        win225 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap226() {
    if (win225) {
        win226 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap227() {
    if (win226) {
        win227 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap228() {
    if (win227) {
        win228 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap229() {
    if (win228) {
        win229 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap230() {
    if (win229) {
        win230 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap231() {
    if (win230) {
        win231 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap232() {
    if (win231) {
        win232 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap233() {
    if (win232) {
        win233 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap234() {
    if (win233) {
        win234 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap235() {
    if (win234) {
        win235 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap236() {
    if (win235) {
        win236 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap237() {
    if (win236) {
        win237 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap238() {
    if (win237) {
        win238 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap239() {
    if (win238) {
        win239 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap240() {
    if (win239) {
        win240 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap241() {
    if (win240) {
        win241 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap242() {
    if (win241) {
        win242 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap243() {
    if (win242) {
        win243 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap244() {
    if (win243) {
        win244 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap245() {
    if (win244) {
        win245 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap246() {
    if (win245) {
        win246 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap247() {
    if (win246) {
        win247 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap248() {
    if (win247) {
        win248 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap249() {
    if (win248) {
        win249 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap250() {
    if (win249) {
        win250 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap251() {
    if (win250) {
        win251 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap252() {
    if (win251) {
        win252 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap253() {
    if (win252) {
        win253 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap254() {
    if (win253) {
        win254 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap255() {
    if (win254) {
        win255 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap256() {
    if (win255) {
        win256 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap257() {
    if (win256) {
        win257 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap258() {
    if (win257) {
        win258 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap259() {
    if (win258) {
        win259 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap260() {
    if (win259) {
        win260 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap261() {
    if (win260) {
        win261 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap262() {
    if (win261) {
        win262 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap263() {
    if (win262) {
        win263 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap264() {
    if (win263) {
        win264 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap265() {
    if (win264) {
        win265 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap266() {
    if (win265) {
        win266 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap267() {
    if (win266) {
        win267 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap268() {
    if (win267) {
        win268 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap269() {
    if (win268) {
        win269 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap270() {
    if (win269) {
        win270 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap271() {
    if (win270) {
        win271 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap272() {
    if (win271) {
        win272 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap273() {
    if (win272) {
        win273 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap274() {
    if (win273) {
        win274 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap275() {
    if (win274) {
        win275 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap276() {
    if (win275) {
        win276 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap277() {
    if (win276) {
        win277 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap278() {
    if (win277) {
        win278 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap279() {
    if (win278) {
        win279 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap280() {
    if (win279) {
        win280 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap281() {
    if (win280) {
        win281 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap282() {
    if (win281) {
        win282 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap283() {
    if (win282) {
        win283 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap284() {
    if (win283) {
        win284 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap285() {
    if (win284) {
        win285 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap286() {
    if (win285) {
        win286 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap287() {
    if (win286) {
        win287 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap288() {
    if (win287) {
        win288 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap289() {
    if (win288) {
        win289 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap290() {
    if (win289) {
        win290 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap291() {
    if (win290) {
        win291 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap292() {
    if (win291) {
        win292 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap293() {
    if (win292) {
        win293 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap294() {
    if (win293) {
        win294 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap295() {
    if (win294) {
        win295 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap296() {
    if (win295) {
        win296 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap297() {
    if (win296) {
        win297 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap298() {
    if (win297) {
        win298 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap299() {
    if (win298) {
        win299 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap300() {
    if (win299) {
        win300 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap301() {
    if (win300) {
        win301 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap302() {
    if (win301) {
        win302 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap303() {
    if (win302) {
        win303 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap304() {
    if (win303) {
        win304 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap305() {
    if (win304) {
        win305 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap306() {
    if (win305) {
        win306 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap307() {
    if (win306) {
        win307 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap308() {
    if (win307) {
        win308 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap309() {
    if (win308) {
        win309 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap310() {
    if (win309) {
        win310 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap311() {
    if (win310) {
        win311 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap312() {
    if (win311) {
        win312 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap313() {
    if (win312) {
        win313 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap314() {
    if (win313) {
        win314 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap315() {
    if (win314) {
        win315 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap316() {
    if (win315) {
        win316 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap317() {
    if (win316) {
        win317 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap318() {
    if (win317) {
        win318 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap319() {
    if (win318) {
        win319 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap320() {
    if (win319) {
        win320 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap321() {
    if (win320) {
        win321 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap322() {
    if (win321) {
        win322 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap323() {
    if (win322) {
        win323 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap324() {
    if (win323) {
        win324 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap325() {
    if (win324) {
        win325 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap326() {
    if (win325) {
        win326 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap327() {
    if (win326) {
        win327 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap328() {
    if (win327) {
        win328 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap329() {
    if (win328) {
        win329 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap330() {
    if (win329) {
        win330 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap331() {
    if (win330) {
        win331 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap332() {
    if (win331) {
        win332 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap333() {
    if (win332) {
        win333 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap334() {
    if (win333) {
        win334 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap335() {
    if (win334) {
        win335 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap336() {
    if (win335) {
        win336 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap337() {
    if (win336) {
        win337 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap338() {
    if (win337) {
        win338 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap339() {
    if (win338) {
        win339 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap340() {
    if (win339) {
        win340 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap341() {
    if (win340) {
        win341 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap342() {
    if (win341) {
        win342 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap343() {
    if (win342) {
        win343 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap344() {
    if (win343) {
        win344 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap345() {
    if (win344) {
        win345 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap346() {
    if (win345) {
        win346 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap347() {
    if (win346) {
        win347 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap348() {
    if (win347) {
        win348 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap349() {
    if (win348) {
        win349 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap350() {
    if (win349) {
        win350 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap351() {
    if (win350) {
        win351 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap352() {
    if (win351) {
        win352 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap353() {
    if (win352) {
        win353 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap354() {
    if (win353) {
        win354 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap355() {
    if (win354) {
        win355 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap356() {
    if (win355) {
        win356 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap357() {
    if (win356) {
        win357 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap358() {
    if (win357) {
        win358 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap359() {
    if (win358) {
        win359 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap360() {
    if (win359) {
        win360 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap361() {
    if (win360) {
        win361 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap362() {
    if (win361) {
        win362 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap363() {
    if (win362) {
        win363 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap364() {
    if (win363) {
        win364 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap365() {
    if (win364) {
        win365 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap366() {
    if (win365) {
        win366 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap367() {
    if (win366) {
        win367 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap368() {
    if (win367) {
        win368 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap369() {
    if (win368) {
        win369 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap370() {
    if (win369) {
        win370 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap371() {
    if (win370) {
        win371 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap372() {
    if (win371) {
        win372 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap373() {
    if (win372) {
        win373 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap374() {
    if (win373) {
        win374 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap375() {
    if (win374) {
        win375 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap376() {
    if (win375) {
        win376 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap377() {
    if (win376) {
        win377 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap378() {
    if (win377) {
        win378 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap379() {
    if (win378) {
        win379 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap380() {
    if (win379) {
        win380 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap381() {
    if (win380) {
        win381 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap382() {
    if (win381) {
        win382 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap383() {
    if (win382) {
        win383 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap384() {
    if (win383) {
        win384 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap385() {
    if (win384) {
        win385 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap386() {
    if (win385) {
        win386 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap387() {
    if (win386) {
        win387 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap388() {
    if (win387) {
        win388 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap389() {
    if (win388) {
        win389 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap390() {
    if (win389) {
        win390 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap391() {
    if (win390) {
        win391 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap392() {
    if (win391) {
        win392 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap393() {
    if (win392) {
        win393 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap394() {
    if (win393) {
        win394 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap395() {
    if (win394) {
        win395 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap396() {
    if (win395) {
        win396 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap397() {
    if (win396) {
        win397 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap398() {
    if (win397) {
        win398 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap399() {
    if (win398) {
        win399 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap400() {
    if (win399) {
        win400 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap401() {
    if (win400) {
        win401 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap402() {
    if (win401) {
        win402 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap403() {
    if (win402) {
        win403 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap404() {
    if (win403) {
        win404 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap405() {
    if (win404) {
        win405 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap406() {
    if (win405) {
        win406 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap407() {
    if (win406) {
        win407 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap408() {
    if (win407) {
        win408 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap409() {
    if (win408) {
        win409 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap410() {
    if (win409) {
        win410 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap411() {
    if (win410) {
        win411 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap412() {
    if (win411) {
        win412 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap413() {
    if (win412) {
        win413 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap414() {
    if (win413) {
        win414 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap415() {
    if (win414) {
        win415 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap416() {
    if (win415) {
        win416 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap417() {
    if (win416) {
        win417 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap418() {
    if (win417) {
        win418 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap419() {
    if (win418) {
        win419 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap420() {
    if (win419) {
        win420 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap421() {
    if (win420) {
        win421 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap422() {
    if (win421) {
        win422 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap423() {
    if (win422) {
        win423 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap424() {
    if (win423) {
        win424 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap425() {
    if (win424) {
        win425 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap426() {
    if (win425) {
        win426 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap427() {
    if (win426) {
        win427 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap428() {
    if (win427) {
        win428 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap429() {
    if (win428) {
        win429 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap430() {
    if (win429) {
        win430 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap431() {
    if (win430) {
        win431 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap432() {
    if (win431) {
        win432 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap433() {
    if (win432) {
        win433 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap434() {
    if (win433) {
        win434 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap435() {
    if (win434) {
        win435 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap436() {
    if (win435) {
        win436 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap437() {
    if (win436) {
        win437 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap438() {
    if (win437) {
        win438 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap439() {
    if (win438) {
        win439 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap440() {
    if (win439) {
        win440 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap441() {
    if (win440) {
        win441 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap442() {
    if (win441) {
        win442 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap443() {
    if (win442) {
        win443 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap444() {
    if (win443) {
        win444 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap445() {
    if (win444) {
        win445 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap446() {
    if (win445) {
        win446 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap447() {
    if (win446) {
        win447 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap448() {
    if (win447) {
        win448 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap449() {
    if (win448) {
        win449 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap450() {
    if (win449) {
        win450 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap451() {
    if (win450) {
        win451 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap452() {
    if (win451) {
        win452 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap453() {
    if (win452) {
        win453 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap454() {
    if (win453) {
        win454 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap455() {
    if (win454) {
        win455 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap456() {
    if (win455) {
        win456 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap457() {
    if (win456) {
        win457 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap458() {
    if (win457) {
        win458 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap459() {
    if (win458) {
        win459 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap460() {
    if (win459) {
        win460 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap461() {
    if (win460) {
        win461 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap462() {
    if (win461) {
        win462 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap463() {
    if (win462) {
        win463 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap464() {
    if (win463) {
        win464 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap465() {
    if (win464) {
        win465 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap466() {
    if (win465) {
        win466 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap467() {
    if (win466) {
        win467 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap468() {
    if (win467) {
        win468 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap469() {
    if (win468) {
        win469 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap470() {
    if (win469) {
        win470 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap471() {
    if (win470) {
        win471 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap472() {
    if (win471) {
        win472 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap473() {
    if (win472) {
        win473 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap474() {
    if (win473) {
        win474 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap475() {
    if (win474) {
        win475 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap476() {
    if (win475) {
        win476 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap477() {
    if (win476) {
        win477 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap478() {
    if (win477) {
        win478 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap479() {
    if (win478) {
        win479 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap480() {
    if (win479) {
        win480 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap481() {
    if (win480) {
        win481 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap482() {
    if (win481) {
        win482 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap483() {
    if (win482) {
        win483 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap484() {
    if (win483) {
        win484 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap485() {
    if (win484) {
        win485 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap486() {
    if (win485) {
        win486 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap487() {
    if (win486) {
        win487 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap488() {
    if (win487) {
        win488 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap489() {
    if (win488) {
        win489 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap490() {
    if (win489) {
        win490 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap491() {
    if (win490) {
        win491 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap492() {
    if (win491) {
        win492 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap493() {
    if (win492) {
        win493 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap494() {
    if (win493) {
        win494 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap495() {
    if (win494) {
        win495 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap496() {
    if (win495) {
        win496 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap497() {
    if (win496) {
        win497 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap498() {
    if (win497) {
        win498 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap499() {
    if (win498) {
        win499 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap500() {
    if (win499) {
        win500 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap501() {
    if (win500) {
        win501 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap502() {
    if (win501) {
        win502 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap503() {
    if (win502) {
        win503 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap504() {
    if (win503) {
        win504 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap505() {
    if (win504) {
        win505 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap506() {
    if (win505) {
        win506 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap507() {
    if (win506) {
        win507 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap508() {
    if (win507) {
        win508 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap509() {
    if (win508) {
        win509 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap510() {
    if (win509) {
        win510 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap511() {
    if (win510) {
        win511 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap512() {
    if (win511) {
        win512 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap513() {
    if (win512) {
        win513 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap514() {
    if (win513) {
        win514 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap515() {
    if (win514) {
        win515 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap516() {
    if (win515) {
        win516 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap517() {
    if (win516) {
        win517 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap518() {
    if (win517) {
        win518 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap519() {
    if (win518) {
        win519 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap520() {
    if (win519) {
        win520 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap521() {
    if (win520) {
        win521 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap522() {
    if (win521) {
        win522 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap523() {
    if (win522) {
        win523 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap524() {
    if (win523) {
        win524 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap525() {
    if (win524) {
        win525 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap526() {
    if (win525) {
        win526 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap527() {
    if (win526) {
        win527 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap528() {
    if (win527) {
        win528 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap529() {
    if (win528) {
        win529 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap530() {
    if (win529) {
        win530 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap531() {
    if (win530) {
        win531 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap532() {
    if (win531) {
        win532 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap533() {
    if (win532) {
        win533 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap534() {
    if (win533) {
        win534 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap535() {
    if (win534) {
        win535 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap536() {
    if (win535) {
        win536 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap537() {
    if (win536) {
        win537 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap538() {
    if (win537) {
        win538 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap539() {
    if (win538) {
        win539 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap540() {
    if (win539) {
        win540 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap541() {
    if (win540) {
        win541 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap542() {
    if (win541) {
        win542 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap543() {
    if (win542) {
        win543 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap544() {
    if (win543) {
        win544 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap545() {
    if (win544) {
        win545 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap546() {
    if (win545) {
        win546 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap547() {
    if (win546) {
        win547 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap548() {
    if (win547) {
        win548 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap549() {
    if (win548) {
        win549 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap550() {
    if (win549) {
        win550 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap551() {
    if (win550) {
        win551 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap552() {
    if (win551) {
        win552 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap553() {
    if (win552) {
        win553 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap554() {
    if (win553) {
        win554 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap555() {
    if (win554) {
        win555 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap556() {
    if (win555) {
        win556 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap557() {
    if (win556) {
        win557 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap558() {
    if (win557) {
        win558 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap559() {
    if (win558) {
        win559 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap560() {
    if (win559) {
        win560 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap561() {
    if (win560) {
        win561 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap562() {
    if (win561) {
        win562 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap563() {
    if (win562) {
        win563 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap564() {
    if (win563) {
        win564 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap565() {
    if (win564) {
        win565 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap566() {
    if (win565) {
        win566 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap567() {
    if (win566) {
        win567 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap568() {
    if (win567) {
        win568 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap569() {
    if (win568) {
        win569 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap570() {
    if (win569) {
        win570 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap571() {
    if (win570) {
        win571 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap572() {
    if (win571) {
        win572 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap573() {
    if (win572) {
        win573 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap574() {
    if (win573) {
        win574 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap575() {
    if (win574) {
        win575 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap576() {
    if (win575) {
        win576 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap577() {
    if (win576) {
        win577 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap578() {
    if (win577) {
        win578 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap579() {
    if (win578) {
        win579 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap580() {
    if (win579) {
        win580 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap581() {
    if (win580) {
        win581 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap582() {
    if (win581) {
        win582 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap583() {
    if (win582) {
        win583 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap584() {
    if (win583) {
        win584 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap585() {
    if (win584) {
        win585 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap586() {
    if (win585) {
        win586 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap587() {
    if (win586) {
        win587 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap588() {
    if (win587) {
        win588 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap589() {
    if (win588) {
        win589 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap590() {
    if (win589) {
        win590 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap591() {
    if (win590) {
        win591 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap592() {
    if (win591) {
        win592 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap593() {
    if (win592) {
        win593 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap594() {
    if (win593) {
        win594 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap595() {
    if (win594) {
        win595 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap596() {
    if (win595) {
        win596 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap597() {
    if (win596) {
        win597 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap598() {
    if (win597) {
        win598 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap599() {
    if (win598) {
        win599 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap600() {
    if (win599) {
        win600 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap601() {
    if (win600) {
        win601 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap602() {
    if (win601) {
        win602 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap603() {
    if (win602) {
        win603 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap604() {
    if (win603) {
        win604 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap605() {
    if (win604) {
        win605 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap606() {
    if (win605) {
        win606 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap607() {
    if (win606) {
        win607 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap608() {
    if (win607) {
        win608 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap609() {
    if (win608) {
        win609 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap610() {
    if (win609) {
        win610 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap611() {
    if (win610) {
        win611 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap612() {
    if (win611) {
        win612 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap613() {
    if (win612) {
        win613 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap614() {
    if (win613) {
        win614 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap615() {
    if (win614) {
        win615 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap616() {
    if (win615) {
        win616 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap617() {
    if (win616) {
        win617 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap618() {
    if (win617) {
        win618 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap619() {
    if (win618) {
        win619 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap620() {
    if (win619) {
        win620 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap621() {
    if (win620) {
        win621 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap622() {
    if (win621) {
        win622 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap623() {
    if (win622) {
        win623 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap624() {
    if (win623) {
        win624 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap625() {
    if (win624) {
        win625 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap626() {
    if (win625) {
        win626 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap627() {
    if (win626) {
        win627 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap628() {
    if (win627) {
        win628 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap629() {
    if (win628) {
        win629 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap630() {
    if (win629) {
        win630 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap631() {
    if (win630) {
        win631 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap632() {
    if (win631) {
        win632 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap633() {
    if (win632) {
        win633 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap634() {
    if (win633) {
        win634 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap635() {
    if (win634) {
        win635 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap636() {
    if (win635) {
        win636 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap637() {
    if (win636) {
        win637 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap638() {
    if (win637) {
        win638 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap639() {
    if (win638) {
        win639 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap640() {
    if (win639) {
        win640 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap641() {
    if (win640) {
        win641 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap642() {
    if (win641) {
        win642 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap643() {
    if (win642) {
        win643 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap644() {
    if (win643) {
        win644 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap645() {
    if (win644) {
        win645 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap646() {
    if (win645) {
        win646 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap647() {
    if (win646) {
        win647 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap648() {
    if (win647) {
        win648 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap649() {
    if (win648) {
        win649 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap650() {
    if (win649) {
        win650 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap651() {
    if (win650) {
        win651 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap652() {
    if (win651) {
        win652 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap653() {
    if (win652) {
        win653 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap654() {
    if (win653) {
        win654 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap655() {
    if (win654) {
        win655 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap656() {
    if (win655) {
        win656 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap657() {
    if (win656) {
        win657 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap658() {
    if (win657) {
        win658 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap659() {
    if (win658) {
        win659 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap660() {
    if (win659) {
        win660 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap661() {
    if (win660) {
        win661 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap662() {
    if (win661) {
        win662 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap663() {
    if (win662) {
        win663 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap664() {
    if (win663) {
        win664 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap665() {
    if (win664) {
        win665 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap666() {
    if (win665) {
        win666 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap667() {
    if (win666) {
        win667 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap668() {
    if (win667) {
        win668 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap669() {
    if (win668) {
        win669 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap670() {
    if (win669) {
        win670 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap671() {
    if (win670) {
        win671 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap672() {
    if (win671) {
        win672 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap673() {
    if (win672) {
        win673 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap674() {
    if (win673) {
        win674 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap675() {
    if (win674) {
        win675 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap676() {
    if (win675) {
        win676 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap677() {
    if (win676) {
        win677 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap678() {
    if (win677) {
        win678 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap679() {
    if (win678) {
        win679 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap680() {
    if (win679) {
        win680 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap681() {
    if (win680) {
        win681 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap682() {
    if (win681) {
        win682 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap683() {
    if (win682) {
        win683 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap684() {
    if (win683) {
        win684 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap685() {
    if (win684) {
        win685 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap686() {
    if (win685) {
        win686 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap687() {
    if (win686) {
        win687 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap688() {
    if (win687) {
        win688 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap689() {
    if (win688) {
        win689 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap690() {
    if (win689) {
        win690 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap691() {
    if (win690) {
        win691 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap692() {
    if (win691) {
        win692 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap693() {
    if (win692) {
        win693 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap694() {
    if (win693) {
        win694 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap695() {
    if (win694) {
        win695 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap696() {
    if (win695) {
        win696 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap697() {
    if (win696) {
        win697 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap698() {
    if (win697) {
        win698 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap699() {
    if (win698) {
        win699 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap700() {
    if (win699) {
        win700 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap701() {
    if (win700) {
        win701 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap702() {
    if (win701) {
        win702 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap703() {
    if (win702) {
        win703 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap704() {
    if (win703) {
        win704 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap705() {
    if (win704) {
        win705 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap706() {
    if (win705) {
        win706 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap707() {
    if (win706) {
        win707 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap708() {
    if (win707) {
        win708 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap709() {
    if (win708) {
        win709 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap710() {
    if (win709) {
        win710 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap711() {
    if (win710) {
        win711 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap712() {
    if (win711) {
        win712 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap713() {
    if (win712) {
        win713 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap714() {
    if (win713) {
        win714 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap715() {
    if (win714) {
        win715 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap716() {
    if (win715) {
        win716 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap717() {
    if (win716) {
        win717 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap718() {
    if (win717) {
        win718 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap719() {
    if (win718) {
        win719 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap720() {
    if (win719) {
        win720 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap721() {
    if (win720) {
        win721 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap722() {
    if (win721) {
        win722 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap723() {
    if (win722) {
        win723 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap724() {
    if (win723) {
        win724 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap725() {
    if (win724) {
        win725 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap726() {
    if (win725) {
        win726 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap727() {
    if (win726) {
        win727 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap728() {
    if (win727) {
        win728 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap729() {
    if (win728) {
        win729 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap730() {
    if (win729) {
        win730 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap731() {
    if (win730) {
        win731 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap732() {
    if (win731) {
        win732 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap733() {
    if (win732) {
        win733 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap734() {
    if (win733) {
        win734 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap735() {
    if (win734) {
        win735 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap736() {
    if (win735) {
        win736 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap737() {
    if (win736) {
        win737 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap738() {
    if (win737) {
        win738 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap739() {
    if (win738) {
        win739 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap740() {
    if (win739) {
        win740 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap741() {
    if (win740) {
        win741 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap742() {
    if (win741) {
        win742 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap743() {
    if (win742) {
        win743 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap744() {
    if (win743) {
        win744 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap745() {
    if (win744) {
        win745 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap746() {
    if (win745) {
        win746 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap747() {
    if (win746) {
        win747 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap748() {
    if (win747) {
        win748 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap749() {
    if (win748) {
        win749 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap750() {
    if (win749) {
        win750 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap751() {
    if (win750) {
        win751 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap752() {
    if (win751) {
        win752 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap753() {
    if (win752) {
        win753 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap754() {
    if (win753) {
        win754 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap755() {
    if (win754) {
        win755 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap756() {
    if (win755) {
        win756 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap757() {
    if (win756) {
        win757 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap758() {
    if (win757) {
        win758 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap759() {
    if (win758) {
        win759 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap760() {
    if (win759) {
        win760 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap761() {
    if (win760) {
        win761 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap762() {
    if (win761) {
        win762 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap763() {
    if (win762) {
        win763 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap764() {
    if (win763) {
        win764 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap765() {
    if (win764) {
        win765 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap766() {
    if (win765) {
        win766 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap767() {
    if (win766) {
        win767 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap768() {
    if (win767) {
        win768 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap769() {
    if (win768) {
        win769 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap770() {
    if (win769) {
        win770 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap771() {
    if (win770) {
        win771 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap772() {
    if (win771) {
        win772 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap773() {
    if (win772) {
        win773 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap774() {
    if (win773) {
        win774 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap775() {
    if (win774) {
        win775 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap776() {
    if (win775) {
        win776 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap777() {
    if (win776) {
        win777 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap778() {
    if (win777) {
        win778 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap779() {
    if (win778) {
        win779 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap780() {
    if (win779) {
        win780 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap781() {
    if (win780) {
        win781 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap782() {
    if (win781) {
        win782 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap783() {
    if (win782) {
        win783 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap784() {
    if (win783) {
        win784 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap785() {
    if (win784) {
        win785 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap786() {
    if (win785) {
        win786 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap787() {
    if (win786) {
        win787 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap788() {
    if (win787) {
        win788 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap789() {
    if (win788) {
        win789 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap790() {
    if (win789) {
        win790 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap791() {
    if (win790) {
        win791 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap792() {
    if (win791) {
        win792 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap793() {
    if (win792) {
        win793 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap794() {
    if (win793) {
        win794 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap795() {
    if (win794) {
        win795 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap796() {
    if (win795) {
        win796 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap797() {
    if (win796) {
        win797 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap798() {
    if (win797) {
        win798 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap799() {
    if (win798) {
        win799 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap800() {
    if (win799) {
        win800 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap801() {
    if (win800) {
        win801 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap802() {
    if (win801) {
        win802 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap803() {
    if (win802) {
        win803 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap804() {
    if (win803) {
        win804 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap805() {
    if (win804) {
        win805 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap806() {
    if (win805) {
        win806 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap807() {
    if (win806) {
        win807 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap808() {
    if (win807) {
        win808 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap809() {
    if (win808) {
        win809 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap810() {
    if (win809) {
        win810 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap811() {
    if (win810) {
        win811 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap812() {
    if (win811) {
        win812 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap813() {
    if (win812) {
        win813 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap814() {
    if (win813) {
        win814 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap815() {
    if (win814) {
        win815 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap816() {
    if (win815) {
        win816 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap817() {
    if (win816) {
        win817 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap818() {
    if (win817) {
        win818 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap819() {
    if (win818) {
        win819 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap820() {
    if (win819) {
        win820 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap821() {
    if (win820) {
        win821 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap822() {
    if (win821) {
        win822 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap823() {
    if (win822) {
        win823 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap824() {
    if (win823) {
        win824 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap825() {
    if (win824) {
        win825 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap826() {
    if (win825) {
        win826 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap827() {
    if (win826) {
        win827 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap828() {
    if (win827) {
        win828 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap829() {
    if (win828) {
        win829 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap830() {
    if (win829) {
        win830 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap831() {
    if (win830) {
        win831 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap832() {
    if (win831) {
        win832 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap833() {
    if (win832) {
        win833 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap834() {
    if (win833) {
        win834 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap835() {
    if (win834) {
        win835 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap836() {
    if (win835) {
        win836 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap837() {
    if (win836) {
        win837 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap838() {
    if (win837) {
        win838 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap839() {
    if (win838) {
        win839 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap840() {
    if (win839) {
        win840 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap841() {
    if (win840) {
        win841 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap842() {
    if (win841) {
        win842 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap843() {
    if (win842) {
        win843 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap844() {
    if (win843) {
        win844 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap845() {
    if (win844) {
        win845 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap846() {
    if (win845) {
        win846 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap847() {
    if (win846) {
        win847 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap848() {
    if (win847) {
        win848 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap849() {
    if (win848) {
        win849 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap850() {
    if (win849) {
        win850 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap851() {
    if (win850) {
        win851 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap852() {
    if (win851) {
        win852 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap853() {
    if (win852) {
        win853 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap854() {
    if (win853) {
        win854 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap855() {
    if (win854) {
        win855 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap856() {
    if (win855) {
        win856 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap857() {
    if (win856) {
        win857 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap858() {
    if (win857) {
        win858 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap859() {
    if (win858) {
        win859 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap860() {
    if (win859) {
        win860 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap861() {
    if (win860) {
        win861 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap862() {
    if (win861) {
        win862 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap863() {
    if (win862) {
        win863 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap864() {
    if (win863) {
        win864 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap865() {
    if (win864) {
        win865 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap866() {
    if (win865) {
        win866 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap867() {
    if (win866) {
        win867 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap868() {
    if (win867) {
        win868 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap869() {
    if (win868) {
        win869 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap870() {
    if (win869) {
        win870 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap871() {
    if (win870) {
        win871 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap872() {
    if (win871) {
        win872 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap873() {
    if (win872) {
        win873 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap874() {
    if (win873) {
        win874 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap875() {
    if (win874) {
        win875 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap876() {
    if (win875) {
        win876 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap877() {
    if (win876) {
        win877 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap878() {
    if (win877) {
        win878 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap879() {
    if (win878) {
        win879 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap880() {
    if (win879) {
        win880 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap881() {
    if (win880) {
        win881 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap882() {
    if (win881) {
        win882 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap883() {
    if (win882) {
        win883 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap884() {
    if (win883) {
        win884 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap885() {
    if (win884) {
        win885 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap886() {
    if (win885) {
        win886 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap887() {
    if (win886) {
        win887 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap888() {
    if (win887) {
        win888 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap889() {
    if (win888) {
        win889 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap890() {
    if (win889) {
        win890 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap891() {
    if (win890) {
        win891 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap892() {
    if (win891) {
        win892 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap893() {
    if (win892) {
        win893 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap894() {
    if (win893) {
        win894 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap895() {
    if (win894) {
        win895 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap896() {
    if (win895) {
        win896 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap897() {
    if (win896) {
        win897 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap898() {
    if (win897) {
        win898 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap899() {
    if (win898) {
        win899 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap900() {
    if (win899) {
        win900 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap901() {
    if (win900) {
        win901 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap902() {
    if (win901) {
        win902 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap903() {
    if (win902) {
        win903 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap904() {
    if (win903) {
        win904 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap905() {
    if (win904) {
        win905 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap906() {
    if (win905) {
        win906 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap907() {
    if (win906) {
        win907 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap908() {
    if (win907) {
        win908 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap909() {
    if (win908) {
        win909 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap910() {
    if (win909) {
        win910 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap911() {
    if (win910) {
        win911 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap912() {
    if (win911) {
        win912 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap913() {
    if (win912) {
        win913 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap914() {
    if (win913) {
        win914 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap915() {
    if (win914) {
        win915 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap916() {
    if (win915) {
        win916 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap917() {
    if (win916) {
        win917 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap918() {
    if (win917) {
        win918 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap919() {
    if (win918) {
        win919 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap920() {
    if (win919) {
        win920 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap921() {
    if (win920) {
        win921 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap922() {
    if (win921) {
        win922 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap923() {
    if (win922) {
        win923 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap924() {
    if (win923) {
        win924 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap925() {
    if (win924) {
        win925 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap926() {
    if (win925) {
        win926 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap927() {
    if (win926) {
        win927 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap928() {
    if (win927) {
        win928 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap929() {
    if (win928) {
        win929 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap930() {
    if (win929) {
        win930 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap931() {
    if (win930) {
        win931 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap932() {
    if (win931) {
        win932 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap933() {
    if (win932) {
        win933 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap934() {
    if (win933) {
        win934 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap935() {
    if (win934) {
        win935 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap936() {
    if (win935) {
        win936 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap937() {
    if (win936) {
        win937 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap938() {
    if (win937) {
        win938 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap939() {
    if (win938) {
        win939 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap940() {
    if (win939) {
        win940 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap941() {
    if (win940) {
        win941 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap942() {
    if (win941) {
        win942 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap943() {
    if (win942) {
        win943 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap944() {
    if (win943) {
        win944 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap945() {
    if (win944) {
        win945 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap946() {
    if (win945) {
        win946 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap947() {
    if (win946) {
        win947 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap948() {
    if (win947) {
        win948 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap949() {
    if (win948) {
        win949 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap950() {
    if (win949) {
        win950 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap951() {
    if (win950) {
        win951 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap952() {
    if (win951) {
        win952 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap953() {
    if (win952) {
        win953 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap954() {
    if (win953) {
        win954 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap955() {
    if (win954) {
        win955 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap956() {
    if (win955) {
        win956 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap957() {
    if (win956) {
        win957 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap958() {
    if (win957) {
        win958 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap959() {
    if (win958) {
        win959 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap960() {
    if (win959) {
        win960 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap961() {
    if (win960) {
        win961 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap962() {
    if (win961) {
        win962 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap963() {
    if (win962) {
        win963 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap964() {
    if (win963) {
        win964 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap965() {
    if (win964) {
        win965 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap966() {
    if (win965) {
        win966 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap967() {
    if (win966) {
        win967 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap968() {
    if (win967) {
        win968 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap969() {
    if (win968) {
        win969 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap970() {
    if (win969) {
        win970 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap971() {
    if (win970) {
        win971 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap972() {
    if (win971) {
        win972 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap973() {
    if (win972) {
        win973 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap974() {
    if (win973) {
        win974 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap975() {
    if (win974) {
        win975 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap976() {
    if (win975) {
        win976 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap977() {
    if (win976) {
        win977 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap978() {
    if (win977) {
        win978 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap979() {
    if (win978) {
        win979 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap980() {
    if (win979) {
        win980 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap981() {
    if (win980) {
        win981 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap982() {
    if (win981) {
        win982 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap983() {
    if (win982) {
        win983 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap984() {
    if (win983) {
        win984 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap985() {
    if (win984) {
        win985 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap986() {
    if (win985) {
        win986 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap987() {
    if (win986) {
        win987 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap988() {
    if (win987) {
        win988 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap989() {
    if (win988) {
        win989 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap990() {
    if (win989) {
        win990 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap991() {
    if (win990) {
        win991 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap992() {
    if (win991) {
        win992 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap993() {
    if (win992) {
        win993 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap994() {
    if (win993) {
        win994 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap995() {
    if (win994) {
        win995 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap996() {
    if (win995) {
        win996 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap997() {
    if (win996) {
        win997 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap998() {
    if (win997) {
        win998 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap999() {
    if (win998) {
        win999 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void leap1000() {
    if (win999) {
        win1000 = true;
    }
    else {
        printf("Failed Horribly!");
    }
}

void display_flag() {
    char flag[FLAG_SIZE];
    FILE *file;
    file = fopen("flag.txt", "r");
    if (file == NULL) {
        printf("'flag.txt' missing in the current directory!\n");
        exit(0);
    }

    fgets(flag, sizeof(flag), file);

    if (win1 && win2) {
        printf("%s", flag);
        return;
    }
    else {
        printf("Failed Horribly!");
    }
}

void get_name() {
  char buf[16];
  printf("Enter your name> ");
  return gets(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  get_name();
}
