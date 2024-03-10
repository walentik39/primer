#include <stdio.h> // printf(3)
#include <sys/types.h> // open(2)
#include <sys/stat.h> // open(2)
#include <fcntl.h>  // open(2)
#include <errno.h>  // errno
#include <string.h> // strerror(3)
#include <unistd.h> // close(2)
#include <dirent.h>
#define BUF_SIZE 4096
int main(int argc, char* argv[])
{
        // Открываем на чтение. Без флага O_DIRECTORY будет ошибка.
        int fd = open(argv[1], O_DIRECTORY | O_RDONLY);
        if(fd < 0) {
                printf("Cannot open %s: %s\n", argv[1], strerror(errno));
                return 1;
        }
        unsigned char buf[BUF_SIZE];
        while(1) {
                struct dirent dir;
                /* Считываем по одному полю */
                ssize_t count = read(fd, &dir.d_fileno, sizeof(dir.d_fileno));
                /* Обработка ошибок один раз для читаемости */
                if(count < 0) {
                        printf("Read error: %s\n",  strerror(errno));
                        return 2;
                }
                if(count == 0) break;
                count += read(fd, &dir.d_reclen, sizeof(dir.d_reclen));
                count += read(fd, &dir.d_type, sizeof(dir.d_type));
                count += read(fd, &dir.d_namlen, sizeof(dir.d_namlen));
                count += read(fd, &dir.d_name, dir.d_reclen - count);
                dir.d_name[dir.d_namlen] = '\0';
                printf("Entry:\n");
                printf("\td_fileno: %lu\n", dir.d_fileno);
                printf("\td_reclen: %u (read: %zd)\n", dir.d_reclen, count);
                printf("\td_type: %u\n", dir.d_type);
                printf("\td_namelen: %u\n", dir.d_namlen);
                printf("\td_name: %s\n", dir.d_name);
        }
        close(fd);
        return 0;
}
