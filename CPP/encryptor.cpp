//Image Read and Write Header files
#define STB_IMAGE_IMPLEMENTATION
#include "stb-library/stb_image.h"

#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb-library/stb_image_write.h"

// Standard libraries
#include <string>
#include <iostream>

typedef uint8_t BYTE;

//FUNCTION HEADERS
void encrypt(std::string INPUT_FILENAME, std::string OUTPUT_FILENAME);
void decrypt(std::string INPUT_FILENAME, std::string OUTPUT_FILENAME);
BYTE gf_inverse(BYTE x);

//MAIN DRIVER PROGRAM
int main(int argc, char** argv) {
	std::string usage = "Usage: <FILE.exe> [[-E/-e/encrypt]/[-D/-d/decrypt]] <INPUT_FILENAME> <OUTPUT_FILENAME>";
    if(argc < 4) {
    	std::cout << "Invalid Command Line Arguments" << std::endl;
    	std::cout << usage << std::endl;
    	return 0;
    }

    std::string func = argv[1];
    std::string in_file = argv[2];
    std::string out_file = argv[3];

    if(func == "-E" || func == "-e" || func == "encrypt") {
    	encrypt(in_file, out_file);
    }
    else if(func == "-D" || func == "-d" || func == "decrypt") {
    	decrypt(in_file, out_file);
	} 
	else {
		std::cout << "Invalid Option" << std::endl;
		std::cout << usage << std::endl;
	}

	return 0;
}

//ALL FUNCTION DEFINITIONS
void encrypt(std::string INPUT_FILENAME, std::string OUTPUT_FILENAME) {
    int width, height, comp;
    unsigned long long i, j, index;
    int val;

    BYTE* rgb_image = stbi_load(INPUT_FILENAME.c_str(), &width, &height, &comp, 0);

    for (i = 0; i < width; i++) {
        for (j = 0; j < height * comp; j++) {
            index = i + j * width;
            val = rgb_image[index];
            val = gf_inverse(val);

			if(i % 2 == 0){
				val = val + i;
			}
			else {
				val = val - i;
			}

			val = val % 256;
			rgb_image[index] = val;
        }
    }

    stbi_write_png(OUTPUT_FILENAME.c_str(), width, height, comp, rgb_image, width * comp);
    stbi_image_free(rgb_image);
}

void decrypt(std::string INPUT_FILENAME, std::string OUTPUT_FILENAME) {
    int width, height, comp;
    unsigned long long i, j, index;
    int val;

    BYTE* rgb_image = stbi_load(INPUT_FILENAME.c_str(), &width, &height, &comp, 0);

    for (i = 0; i < width; i++) {
        for (j = 0; j < height * comp; j++) {
            index = i + j * width;
            val = rgb_image[index];

			if(i % 2 == 0) {
				val = val - i;
			}
			else {
				val = val + i;
			}

			val = val % 256;
			val = gf_inverse(val);
			rgb_image[index] = val;
        }
    }

    stbi_write_png(OUTPUT_FILENAME.c_str(), width, height, comp, rgb_image, width * comp);
    stbi_image_free(rgb_image);
}

int bitlength(int x) {
    int y = 0;
    for (; y < 50; y++) {
        if ((1 << y) - 1 >= x) {
            return y;
        }
    }
    return y;
}

BYTE gf_inverse(BYTE x) {
    uint16_t u1 = 0, u3 = 0x11b, v1 = 1, v3 = x;
    while (v3 != 0) {
        uint16_t t1 = u1, t3 = u3;
        BYTE q = bitlength(u3) - bitlength(v3);

        if (q >= 0) {
            t1 ^= v1 << q;
            t3 ^= v3 << q;
        }
        
        u1 = v1;
        u3 = v3;
        v1 = t1;
        v3 = t3;
    }

    if (u1 >= 0x100) {
        u1 ^= 0x11b;
    }

    return u1;
}
