#! /bin/sh

for i in `seq 0 1 29`
do
	filename=`printf image%02d.pgm $i`
	dd if=capture.dat bs=614400 count=1 skip=${i}| od -vt u2 ${1} | \
	awk 'BEGIN {
		printf("P2\n");
		printf("640 480\n");
		printf("65535\n");
		count = 0
	}
	{
		if (NF > 1) {
			for (i = 2; i <= NF; i++) {
				printf("%d ", $i)
				count++
			}
			printf("\n")
		}
	}' > ${filename}
done