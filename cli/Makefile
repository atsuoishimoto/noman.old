TARGET = embedded_zip_reader
ZIP = noman-ja.zip
ZIP_HEADER = zip_ja.h
SRC = main.c

all: $(TARGET)

# Generate header
$(ZIP_HEADER): $(ZIP)
	xxd -i $< > $@.tmp
	sed 's/^unsigned/static const unsigned/g' $@.tmp > $@
	rm $@.tmp

# Build
$(TARGET): $(SRC) $(ZIP_HEADER)
	gcc -o $@ $(SRC) -lzip

clean:
	rm -f $(TARGET) $(ZIP_HEADER)
