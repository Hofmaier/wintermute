#! /bin/sh

for i in `seq 0 1 29`
do
	filename=`printf image%02d.pgm $i`
	dd if=capture.dat bs=614400 count=1 skip=${i}| od -vt u1 ${1} | \
	awk 'BEGIN {
		printf("P3\n");
		printf("640 480\n");
		printf("256\n");
		count = 0
	}
	{
		if (NF > 1) {
			for (i = 2; i <= NF; i+=4) {
				y1 = $i
				u = $(i+1)
				y2 = $(i+2)
				v = $(i+3)
				#printf("%d ", y1)
				#printf("%d ", y2)
				u = (u - 128)
				v = (v - 128)

				r = y1 + v
				g = y1 - 0.51 * v - 0.19 * u
				b = y1 + u
				if (r > 255) { r = 255 }
				if (r < 0) { r = 0 }
				if (g > 255) { g = 255 }
				if (g < 0) { g = 0 }
				if (b > 255) { b = 255 }
				if (b < 0) { b = 0 }
				printf("%d %d %d ", r, g, b)

				r = y2 + v
				g = y2 - 0.51 * v - 0.19 * u
				b = y2 + u
				if (r > 255) { r = 255 }
				if (r < 0) { r = 0 }
				if (g > 255) { g = 255 }
				if (g < 0) { g = 0 }
				if (b > 255) { b = 255 }
				if (b < 0) { b = 0 }
				printf("%d %d %d ", r, g, b)

				count++
			}
			printf("\n")
		}
	}' > ${filename}
done

