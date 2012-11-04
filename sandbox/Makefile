appex : unicapmodule.o
	gcc unicapmodule.o `pkg-config --libs libunicap` -lcfitsio -lpthread -o appex
unicapmodule.o : unicapmodule.c
	gcc `pkg-config --cflags libunicap` -c unicapmodule.c

clean:
	rm *.o appex
