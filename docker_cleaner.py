import os

import docker


def main():
    print("Checking if docker running")
    client = docker.from_env()
    if client:
        images = client.images.list()
        containers = client.containers.list()

        print("Local images of {}".format(images.__len__()))
        print("Local containers of {}".format(containers.__len__()))

        print("Stop all running containers")
        for container in containers:
            container.stop()

        print("Show size before cleaning")
        os.system("docker system df")

        print("Remove all containers, images, networks, ...")
        os.system("docker system prune -a -f")

        print("Show after cleaning")
        os.system("docker system df")


if __name__ == '__main__':
    main()
